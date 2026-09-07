#!/usr/bin/env python3
"""
Prueft den Referenz-Content gegen die Publish-Gates aus 01-DATA-MODEL.md
und simuliert die Rabbit-Hole-Pfadlogik aus 00-BLUEPRINT.md.

Kein Anwendungscode - ein Pruefwerkzeug fuer die Redaktion.
    python3 tools/validate.py
"""
import json, glob, os, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, "content", "reference")

TIER_GATES = {           # tier: (min_sources, min_links, min_quiz)
    "a_full": (8, 5, 5),
    "b_file": (3, 3, 2),
    "c_index": (1, 1, 0),
}
VALID_STATUS = {"documented", "partly_documented", "contested", "unverified", "debunked"}
DOC_BASIS = "documented_basis"


def load():
    sources = {s["id"]: s for s in json.load(open(f"{REF}/sources.json"))["sources"]}
    files = {}
    for p in sorted(glob.glob(f"{REF}/files/*.json")):
        f = json.load(open(p))
        f["_path"] = os.path.basename(p)
        files[f["file_number"]] = f
    linkdoc = json.load(open(f"{REF}/links.json"))
    return sources, files, linkdoc["links"], linkdoc["direction_semantics"]


def gate_check(sources, files, links):
    """Wendet die Publish-Gates an. Gibt (findings, publishable_set) zurueck."""
    out, ok = [], set()
    deg = defaultdict(int)
    for l in links:
        deg[l["from"]] += 1
        deg[l["to"]] += 1

    for n, f in sorted(files.items()):
        fails = []
        tier = f["tier"]
        min_src, min_link, min_quiz = TIER_GATES[tier]

        used_sources = {e["source_id"] for c in f["claims"] for e in c.get("evidence_items", [])}
        used_sources |= {q["source_id"] for q in f.get("quiz_questions", [])}

        # G-SRC-MIN mit Ausnahme: ein Kern-Claim ohne jede Evidenzgrundlage kann
        # keine 8 Evidenzquellen zitieren - es gibt keine. Stattdessen niedrigere
        # Schwelle plus Pflicht zu Herkunftsquellen (primary_claimant).
        core_claim = next((c for c in f["claims"] if c.get("is_core")), None)
        no_basis = bool(core_claim and core_claim.get("no_evidentiary_basis"))
        eff_min_src = 5 if (no_basis and tier == "a_full") else min_src
        if len(used_sources) < eff_min_src:
            note = " [no_evidentiary_basis: Schwelle 5]" if no_basis else ""
            fails.append(f"G-SRC-MIN: {len(used_sources)}/{eff_min_src} Quellen{note}")
        if no_basis:
            prov = sum(1 for sid in used_sources
                       if sid in sources and sources[sid]["kind"] == "primary_claimant")
            if prov < 2:
                fails.append(f"G-PROVENANCE: {prov}/2 Herkunftsquellen (primary_claimant)")
        if deg[n] < min_link:
            fails.append(f"G-LINK-MIN: {deg[n]}/{min_link} Kanten")
        if len(f.get("quiz_questions", [])) < min_quiz:
            fails.append(f"G-QUIZ-MIN: {len(f.get('quiz_questions', []))}/{min_quiz} Fragen")

        # genau ein Kern-Claim
        cores = [c for c in f["claims"] if c.get("is_core")]
        if len(cores) != 1:
            fails.append(f"G-CORE-ONE: {len(cores)} Kern-Claims (erwartet 1)")

        for c in f["claims"]:
            tag = f"claim#{c['ordinal']}"
            if c["evidence_status"] not in VALID_STATUS:
                fails.append(f"G-STATUS-ENUM: {tag} unbekannter Status")
            if not c.get("status_rationale", "").strip():
                fails.append(f"G-STATUS-WHY: {tag} ohne Begruendung")
            if c["evidence_status"] == "debunked":
                if not any(e["stance"] == "undermines" for e in c.get("evidence_items", [])):
                    fails.append(f"G-DEBUNK-PROOF: {tag} debunked ohne Gegenbeleg")

        # Quellen-Identifier
        for sid in used_sources:
            if sid not in sources:
                fails.append(f"G-SRC-REF: unbekannte Quelle {sid}")
                continue
            s = sources[sid]
            if not any(s.get(k) for k in ("url", "doi", "isbn", "archive_ref")):
                fails.append(f"G-SRC-ID: {sid} ohne aufloesbaren Identifier")

        # Quizfragen brauchen Quellenbeleg und genau eine richtige Antwort
        for i, q in enumerate(f.get("quiz_questions", []), 1):
            if not q.get("source_id"):
                fails.append(f"G-QUIZ-SRC: Frage {i} ohne source_id")
            if sum(1 for o in q["options"] if o["is_correct"]) != 1:
                fails.append(f"G-QUIZ-ONE: Frage {i} hat nicht genau eine richtige Antwort")

        # Harm-Tier-Regeln
        ht = f.get("harm_tier", 0)
        if ht >= 3:
            if not f.get("legal_ok_at"):
                fails.append("G-HARM-3: Rechtspruefung nicht dokumentiert")
            for e in f.get("entities", []):
                if e.get("is_living_private_person") and e["role"] == "alleged_actor":
                    fails.append(f"G-LIVING-PERSON: {e['name']} als alleged_actor")
        if ht >= 2 and "why_it_spread" not in f:
            fails.append("G-HARM-2-LAYOUT: Abschnitt why_it_spread fehlt")

        if fails:
            out.append((n, f["title"], fails))
        else:
            ok.add(n)
    return out, ok


def build_graph(links):
    """Bidirektionale Adjazenz mit Laufrichtung."""
    g = defaultdict(list)
    for l in links:
        g[l["from"]].append((l["to"], l["relation"], "forward", l["strength"]))
        g[l["to"]].append((l["from"], l["relation"], "reverse", l["strength"]))
    return g


def deepest_run(start, files, g, exempt_doc_basis=True):
    """
    Tiefster Pfad ab start nach Blueprint-Regel:
      obscurity(next) >= high_water_mark - 1
      Ausnahme: documented_basis-Kanten sind von der Regel befreit.
    """
    best = []

    def walk(node, visited, hwm, path):
        nonlocal best
        if len(path) > len(best):
            best = list(path)
        cands = []
        for nxt, rel, direction, strength in g[node]:
            if nxt in visited or nxt not in files:
                continue
            obs = files[nxt]["obscurity_score"]
            exempt = exempt_doc_basis and rel == DOC_BASIS
            if not exempt and obs < hwm - 1:
                continue
            cands.append((nxt, rel, direction, strength, obs))
        cands.sort(key=lambda c: (c[1] != DOC_BASIS, -c[3], -c[4]))
        for nxt, rel, direction, strength, obs in cands:
            walk(nxt, visited | {nxt}, max(hwm, obs), path + [(nxt, rel, direction)])

    walk(start, {start}, files[start]["obscurity_score"], [])
    return best


def main():
    sources, files, links, semantics = load()
    print(f"REFERENZ-SET: {len(files)} Files, {len(links)} Kanten, {len(sources)} Quellen\n")

    print("=" * 74)
    print("1. PUBLISH-GATES")
    print("=" * 74)
    findings, ok = gate_check(sources, files, links)
    for n, title, fails in findings:
        print(f"\n  FILE #{n:04d} {title}")
        for x in fails:
            print(f"      BLOCKED  {x}")
    print(f"\n  -> publizierbar: {len(ok)}/{len(files)}"
          f"   blockiert: {len(findings)}/{len(files)}")

    print("\n" + "=" * 74)
    print("2. STATUS- UND HARM-VERTEILUNG")
    print("=" * 74)
    st, ht = defaultdict(int), defaultdict(int)
    for f in files.values():
        core = next(c for c in f["claims"] if c.get("is_core"))
        st[core["evidence_status"]] += 1
        ht[f.get("harm_tier", 0)] += 1
    print("  Kern-Status:", dict(sorted(st.items())))
    print("  Harm-Tier:  ", dict(sorted(ht.items())))
    print("  Claims gesamt:", sum(len(f["claims"]) for f in files.values()),
          "| Quizfragen:", sum(len(f.get("quiz_questions", [])) for f in files.values()))

    print("\n" + "=" * 74)
    print("3. GRAPH: KOMPONENTEN UND ISOLIERTE KNOTEN")
    print("=" * 74)
    g = build_graph(links)
    seen, comps = set(), []
    for n in files:
        if n in seen:
            continue
        stack, comp = [n], []
        seen.add(n)
        while stack:
            cur = stack.pop()
            comp.append(cur)
            for nxt, *_ in g[cur]:
                if nxt not in seen and nxt in files:
                    seen.add(nxt)
                    stack.append(nxt)
        comps.append(sorted(comp))
    for i, c in enumerate(comps, 1):
        print(f"  Komponente {i}: {c}")
    iso = [n for n in files if not g[n]]
    print(f"  isolierte Knoten: {iso if iso else 'keine'}")

    print("\n" + "=" * 74)
    print("4. RABBIT HOLE: TIEFSTER PFAD JE STARTKNOTEN")
    print("=" * 74)
    print(f"  Regel: obscurity(next) >= high_water_mark - 1, "
          f"'{DOC_BASIS}' ausgenommen")
    print(f"  Entry-Schwelle laut Blueprint: max_depth >= 6\n")
    entries = []
    for n in sorted(files):
        with_ex = deepest_run(n, files, g, True)
        without = deepest_run(n, files, g, False)
        mark = "ENTRY" if len(with_ex) >= 6 else "  -  "
        if len(with_ex) >= 6:
            entries.append(n)
        print(f"  [{mark}] #{n:04d} {files[n]['title'][:34]:34} "
              f"depth={len(with_ex)}  ohne doc_basis-Ausnahme={len(without)}")

    print(f"\n  -> qualifizierte Einstiegspunkte: {len(entries)}/{len(files)}  {entries}")

    if entries:
        s = entries[0]
        path = deepest_run(s, files, g, True)
        print(f"\n  Beispielpfad ab FILE #{s:04d}:")
        hwm = files[s]["obscurity_score"]
        print(f"     L0  #{s:04d} {files[s]['title']}  (obs {hwm})")
        for i, (nid, rel, direction) in enumerate(path, 1):
            label = semantics[rel][f"label_{direction}"]
            hwm = max(hwm, files[nid]["obscurity_score"])
            print(f"     L{i}  #{nid:04d} {files[nid]['title'][:30]:30} "
                  f"(obs {files[nid]['obscurity_score']}, hwm {hwm})  via {label}")
        print("     BOTTOM REACHED")

    print("\n" + "=" * 74)
    print("5. VERWAISTE QUELLEN")
    print("=" * 74)
    used = set()
    for f in files.values():
        used |= {e["source_id"] for c in f["claims"] for e in c.get("evidence_items", [])}
        used |= {q["source_id"] for q in f.get("quiz_questions", [])}
    unused = sorted(set(sources) - used)
    print(f"  {len(unused)} ungenutzt: {unused if unused else 'keine'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
