# SCHREIBSTANDARD FÜR AUTOR:INNEN

Ergänzt die [Redaktionsordnung](02-EDITORIAL-POLICY.md) um das Handwerkliche.
Die zehn Files unter [`content/reference/files/`](../content/reference/files/)
sind die Arbeitsvorlage — dieses Dokument erklärt, warum sie so aussehen.

---

## 1. DIE REIHENFOLGE DER ARBEIT

Falsch ist es, den Text zuerst zu schreiben und die Quellen danach zu suchen.
Das erzeugt Sätze, für die es keinen Beleg gibt, und die fallen später niemandem
mehr auf.

```
1. Quellen sammeln und lesen        ← zuerst, immer
2. Claims herausschälen             ← was wird eigentlich behauptet?
3. Belege den Claims zuordnen       ← supports / undermines / context
4. Status vergeben + begründen      ← die eigentliche redaktionelle Leistung
5. Erst jetzt: Fließtext schreiben
6. Verkanten (im Cluster)
7. Quizfragen aus verifizierten Sätzen ableiten
```

Wer bei Schritt 5 anfängt, schreibt eine Reportage. Wir schreiben eine Akte.

---

## 2. DER HOOK (`summary`)

Ein bis zwei Sätze. Er trägt die Node Card im Rabbit Hole und entscheidet über
Weiterlesen oder Abbruch. Er enthält **eine konkrete, belegte, überraschende
Tatsache** — nicht die Zusammenfassung der Theorie.

> ❌ *„Manche Menschen glauben, die Regierung habe Gedankenkontrolle erforscht."*
>
> ✅ *„Between 1953 and 1973 the CIA funded experiments at more than 80
> institutions — universities, hospitals, prisons and pharmaceutical companies —
> testing drugs, hypnosis and sensory deprivation on human subjects, some of whom
> were never told. In 1973 the Director of Central Intelligence ordered the files
> destroyed."*

Der zweite Hook nennt Zahlen, Zeitraum, Institutionen und endet auf der
stärksten Einzeltatsache. Er behauptet nichts, was nicht belegt ist.

**Test:** Streiche den Hook auf eine Zeile zusammen. Bleibt eine überprüfbare
Tatsache übrig? Wenn nur eine Stimmung übrig bleibt, ist er noch nicht fertig.

---

## 3. CLAIMS ZERLEGEN

Der häufigste handwerkliche Fehler ist ein zu großer Kern-Claim. Eine Behauptung
ist zerlegt, wenn jeder Teil **für sich** einen Status tragen kann.

Beispiel aus [`FILE-0002`](../content/reference/files/FILE-0002-operation-northwoods.json):

| Claim | Status |
|---|---|
| Die US-Regierung hat Pläne erstellt, Anschläge auf eigene Bürger zu inszenieren | 🔵 PARTLY DOCUMENTED |
| Operation Northwoods wurde ausgeführt | 🔴 DEBUNKED |
| Weil Northwoods existierte, waren spätere Anschläge ebenfalls inszeniert | 🟡 UNVERIFIED *(no evidentiary basis)* |

Ein einziger Status auf „Operation Northwoods" hätte alle drei Aussagen
gleichgesetzt. Genau das darf nicht passieren.

**Faustregel:** 3–5 Claims je Tier-A-File. Weniger als 3 heißt meistens, dass
noch nicht sauber zerlegt wurde.

**Der dritte Claim ist fast immer der wichtigste.** Er fängt den
Schlussfolgerungssprung ab — den Schritt von „das ist passiert" zu „also ist
auch jenes passiert". Dieser Sprung ist der Ort, an dem die meisten
Verschwörungserzählungen ihre Kraft gewinnen, und er braucht einen eigenen
Claim mit eigenem Status.

---

## 4. STATUS-BEGRÜNDUNG (`status_rationale`)

Pflichtfeld. Zwei bis vier Sätze, die sagen **warum**, nicht **dass**.

> ❌ *„Die Behauptung ist widerlegt."*
>
> ✅ *„The originating study was retracted in full and found by investigation to
> contain altered data; its lead author was struck off for serious professional
> misconduct. The hypothesis was independently tested in cohorts and meta-analyses
> covering more than two million children and no association was found."*

Bei schwieriger Faktenlage kommt `confidence_note` dazu. Das Feld ist keine
Absicherung, sondern eine inhaltliche Aussage — es sagt dem Leser, wie fest der
Status steht. Vorbild: [`FILE-0004`](../content/reference/files/FILE-0004-jfk-assassination.json),
wo `CONTESTED` ausdrücklich als „Widerspruch im offiziellen Aktenbestand" und
nicht als „Evidenz-Gleichstand" erklärt wird.

---

## 5. GEGENBELEGE SIND PFLICHT, NICHT KÜR

Ein Claim mit Status `debunked` **muss** mindestens einen `undermines`-Beleg
mit Quelle tragen. Das Gate `G-DEBUNK-PROOF` blockiert sonst die Publikation.

Im Trockenlauf hat dieses Gate einen echten Fehler gefunden: In
[`FILE-0003`](../content/reference/files/FILE-0003-moon-landing-hoax.json) war
der Schatten-Claim als widerlegt markiert, hatte aber nur eine Erklärung und
keinen Beleg. Beim Lesen fiel es niemandem auf.

**„Es klingt unplausibel" ist kein Debunk.**

---

## 6. DIE STÄRKSTE VERSION DER GEGENSEITE — UND IHRE GRENZE

Bei Harm-Tier 0 und 1 gilt: Die Argumente der Anhänger werden in ihrer
**besten, nicht in ihrer dümmsten Form** wiedergegeben. Eine Strohmann-Version
zu widerlegen überzeugt niemanden, der die echte Version kennt, und kostet die
Glaubwürdigkeit des ganzen Files.

[`FILE-0007`](../content/reference/files/FILE-0007-majestic-12.json) enthält
deshalb einen eigenen Claim für das beste Argument der Gegenseite — dass die
zwölf genannten Männer real waren und die beschriebenen Positionen innehatten.
Der Claim steht auf `documented`, weil er zutrifft, mit der Anmerkung, dass er
über die Existenz des Komitees nichts aussagt.

**Ab Harm-Tier 2 kehrt sich diese Regel um.** Dort werden Argumente
*beschrieben und eingeordnet*, nicht in ihrer überzeugendsten Form
rekonstruiert. Der Abschnitt heißt `WHY IT SPREAD` und erklärt die
Ausbreitungsmechanik, nicht die Beweisführung. Vergleiche
[`FILE-0009`](../content/reference/files/FILE-0009-vaccines-autism.json):
Der Abschnitt erklärt, warum der zeitliche Zusammenfall von MMR-Impfung und
Autismus-Diagnose eine für Menschen unwiderstehliche Kausalvermutung erzeugt —
und macht damit das Publikum verständlich, statt es lächerlich zu machen.

---

## 7. SCHWÄCHEN DER EIGENEN SEITE NENNEN

Wo die offizielle Erklärung schwach ist, steht das im File.

[`FILE-0005`](../content/reference/files/FILE-0005-roswell.json) nennt zwei
solche Stellen: dass Mogul-Flug 4 im erhaltenen Startprotokoll als abgesagt
geführt wird, und dass die Erklärung der Air Force für die Berichte über
Körper auf Fallschirmtests von 1953–1959 verweist — sechs bis zwölf Jahre nach
den beschriebenen Ereignissen.

Beides wegzulassen wäre bequemer gewesen. Es hätte das File aber angreifbar
gemacht, und zwar zu Recht. **Wer die schwache Stelle selbst nennt, behält die
Deutungshoheit über sie.**

---

## 8. QUIZFRAGEN

- Ausschließlich aus verifizierten Sätzen des Files ableiten
- Jede Frage braucht `source_id` — das Gate erzwingt es
- Falsche Antwortoptionen müssen **plausibel** sein, nicht albern.
  `FBI / CIA / NASA / NSA` ist eine gute Frage. `CIA / Post / Bäckerei / Mond` ist keine.
- Keine Frage, deren richtige Antwort eine unbelegte Behauptung ist
- **`documented_or_debunked` ist das Kernformat.** Es trainiert genau die
  Fähigkeit, um die es der App geht. Mindestens eine Frage je File in diesem Format.

---

## 9. VERKANTUNG

Kanten entstehen **im Cluster**, nicht am Einzelfile. Ein allein geschriebenes
File hat keine Nachbarn — im Trockenlauf sind daran zwei von zehn Files
gescheitert.

Für jede Kante:
- Relationstyp aus der Enum wählen, nicht „irgendwie verwandt"
- `rationale` **und** `rationale_reverse` schreiben. Die Vorwärts-Begründung
  ergibt rückwärts gelesen meistens keinen Sinn, und der Rabbit Hole läuft in
  beide Richtungen.
- **Nach `documented_basis` suchen.** Jedes spekulative File soll, wo möglich,
  eine Kante auf den realen belegten Kern darunter haben. Das ist die Kante,
  die den Rabbit Hole erdet, und der wichtigste Kantentyp des Produkts.

---

## 10. SPRACHE

- Amerikanisches Englisch
- Konjunktiv bei Behauptungen, Indikativ nur bei Belegtem
- Keine vagen Mengenangaben („viele Experten") — Zahlen und Namen
- Über Behauptungen urteilen, nie über Menschen
- Kein Sarkasmus, keine Anführungszeichen der Distanzierung, keine rhetorischen Fragen

---

## 11. CHECKLISTE VOR ABGABE

```
[ ] Quellen zuerst gelesen, dann geschrieben
[ ] Hook enthält eine konkrete belegte Tatsache
[ ] 3-5 Claims, jeder für sich statusfähig
[ ] Der Schlussfolgerungssprung hat einen eigenen Claim
[ ] Jeder Status hat eine Begründung, die "warum" sagt
[ ] Jeder debunked-Claim hat einen undermines-Beleg mit Quelle
[ ] Schwachstellen der offiziellen Erklärung sind genannt
[ ] Jede Quelle hat einen auflösbaren Identifier
[ ] Harm-Tier bestimmt, ab 2 Layout invertiert, WHY IT SPREAD vorhanden
[ ] Kanten mit rationale UND rationale_reverse
[ ] documented_basis gesucht
[ ] Quizfragen mit source_id, mindestens eine documented_or_debunked
[ ] python3 tools/validate.py laeuft ohne BLOCKED fuer dieses File
```

Die letzte Zeile ist die wichtigste: **Das Gate ist der Abgabetermin, nicht
die Meinung der Redaktionsleitung.**
