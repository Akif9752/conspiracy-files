# CONSPIRACY FILES — MVP SCOPE & ROADMAP

---

## 1. FEATURE-PRIORISIERUNG

Bewertet nach **User Value**, **Retention**, **Viralität** und **Aufwand**
(jeweils 1–5). *Score = (Value + Retention + Viral) − Aufwand.*

| Feature | Value | Ret. | Viral | Aufw. | Score | Release |
|---|---|---|---|---|---|---|
| **Daily File** (Predict→Reveal→Read→Quiz) | 5 | 5 | 4 | 3 | **11** | V1 |
| **File Detail mit Claim-Breakdown** | 5 | 3 | 3 | 3 | **8** | V1 |
| **Rabbit Hole Runs** | 5 | 5 | 5 | 4 | **11** | V1 |
| **Calibration Score** | 4 | 4 | 5 | 2 | **11** | V1 |
| **Share Cards** | 2 | 2 | 5 | 2 | **7** | V1 |
| Search & Filter | 4 | 3 | 1 | 3 | 5 | V1 |
| Quiz: Documented or Debunked? | 4 | 4 | 4 | 2 | **10** | V1 |
| Quiz: Classic | 3 | 3 | 2 | 1 | 7 | V1 |
| Quiz: Speed | 3 | 3 | 3 | 2 | 7 | V1 |
| Quiz: Rabbit Hole Mode | 4 | 4 | 3 | 3 | 8 | V1 |
| XP / Level / Ränge | 3 | 4 | 2 | 2 | 7 | V1 |
| Streak + Freeze | 2 | 5 | 1 | 1 | 7 | V1 |
| Achievements (40) | 3 | 3 | 2 | 2 | 6 | V1 |
| Collections / Casefiles | 3 | 4 | 2 | 2 | 7 | V1 |
| Connected Files (Nachbarschaft) | 4 | 3 | 2 | 2 | 7 | V1 |
| Premium / Paywall | 1 | 1 | 0 | 3 | −1 | V1 *(Umsatz)* |
| Wöchentliche Ligen | 2 | 5 | 3 | 3 | 7 | V1.5 |
| Freunde per Invite | 2 | 4 | 4 | 3 | 7 | V1.5 |
| Home-Widget | 2 | 4 | 1 | 2 | 5 | V1.5 |
| Trending (echte Daten) | 3 | 2 | 1 | 2 | 4 | V1.5 |
| Entity-Seiten | 4 | 2 | 1 | 3 | 4 | V2 |
| **AI Analyst** | 5 | 3 | 4 | 5 | **7** | V2 |
| Constellation Graph | 3 | 2 | 4 | 5 | 4 | V2 |
| Globales Leaderboard | 1 | 1 | 2 | 2 | 2 | V2 |
| Web-App / SEO | 4 | 2 | 5 | 5 | 6 | V3 |
| Lokalisierung | 3 | 2 | 2 | 5 | 2 | V3 |
| Community-Korrekturen | 2 | 3 | 2 | 5 | 2 | V3 |
| **User-generierte Theorien** | — | — | — | — | **NIE** | ✕ |

### Die vier höchstbewerteten Features tragen das Produkt

Daily File, Rabbit Hole, Calibration und Documented-or-Debunked. Wenn Zeit
knapp wird, wird alles andere gekürzt — nicht diese vier.

---

## 2. CUT-LISTE — was bewusst NICHT in V1 kommt

| Gestrichen | Begründung |
|---|---|
| Vollständige Graph-Visualisierung | Auf 390 px Breite unlesbar. Kostet Wochen, liefert einen Screenshot. Die Nachbarschaftsansicht (max. 8 Knoten) liefert 90 % des Nutzens. |
| Globales Leaderboard | Für 99 % der Nutzer unerreichbar → demotivierend. Braucht außerdem Nutzerbasis, die bei Launch nicht existiert. Ligen in V1.5 sind die bessere Lösung. |
| AI Analyst | Ohne dichtes Korpus halluziniert das Feature genau das, was die App verhindern soll. Erst ab ~2.500 Files sinnvoll. |
| Freunde / Social Graph | Erfordert Accounts, Privacy-Arbeit, Missbrauchsschutz. Nicht die erste Retention-Baustelle. |
| Kommentare / Foren | App-Store-Regel 1.2 (UGC-Moderation). Auf diesem Themengebiet ein Moderations-Albtraum. |
| User-generierte Theorien | Dauerhaft ausgeschlossen. Das Produktversprechen ist redaktionelle Prüfung — UGC zerstört es. |
| Werbung | Erst nach nachgewiesener Retention. Vorher kostet sie mehr Vertrauen als sie einbringt. |
| Lokalisierung | Content-Kosten × Sprachen. Erst EN validieren. |
| Popularity-Sterne in der UI | Redundant zu Obscurity (nahezu invers). Nur Obscurity zeigen + `TRENDING`-Badge. |
| 25 Kategorien | Auf 10 konsolidiert; Feingranularität über Tags. |
| Separates "Random Theory" als Hero | Wird zum Startpunkt-Generator des Rabbit Hole. |
| 6. Evidence Status (`SPECULATIVE`) | In `UNVERIFIED` integriert als Zusatzlabel `no evidentiary basis`. 5 Chips passen in eine Filterzeile, 6 nicht. |
| 100 einzelne Level-Namen | 10 Ränge über 100 Level. Gleiche Identitätswirkung, kein Pflegeaufwand. |

---

## 3. LAUNCH-CHECKLISTE

### Content
- [ ] 150 Tier-A-Files publiziert (alle 5 Evidence Status vertreten)
- [ ] 150 Tier-B-Files publiziert
- [ ] 700 Tier-C-Index-Entries publiziert
- [ ] ≥ 600 Quizfragen aktiv, alle mit `source_id`
- [ ] ≥ 2.000 typisierte Kanten; jedes File mit ≥ 2 Kanten
- [ ] Jedes File mit `harm_tier ≥ 2` zweitfreigegeben
- [ ] Jedes File mit `harm_tier = 3` rechtsgeprüft
- [ ] 60 Tage `daily_file` im Voraus kuratiert
- [ ] 12 Collections
- [ ] Kein Startknoten mit `max_depth < 6`

### Produkt
- [ ] Onboarding < 90 s bis Home
- [ ] Erster Rabbit-Hole-Knoten ist immer `DOCUMENTED`
- [ ] Evidence Status auf jedem Claim im selben Viewport
- [ ] Alle Share Cards tragen den Status
- [ ] Tier-3-Inhalte: keine Share Card, kein Daily File, kein Run-Endknoten
- [ ] Paywall zeigt nie Evidence/Counterpoints/Assessment hinter Schloss
- [ ] Status = Farbe **+** Form **+** Label (Barrierefreiheit)
- [ ] Dynamic Type / Schriftskalierung bis 200 %
- [ ] VoiceOver / TalkBack für File Detail und Quiz

### Technik
- [ ] Tier-A-Snapshot in der App gebündelt (< 5 MB)
- [ ] XP / Streak / Calibration serverautoritativ
- [ ] Rabbit-Hole-Reachability nächtlich vorberechnet
- [ ] Alle Publish-Gates als DB-Constraints aktiv
- [ ] Analytics: Core-Loop-Funnel vollständig instrumentiert
- [ ] Crash-free Sessions > 99,5 %
- [ ] Cold Start < 1,5 s bis erster Inhalt

### Store
- [ ] Altersfreigabe 17+ / Mature bewusst gesetzt
- [ ] Screenshot 1 zeigt die Evidence-Schicht, nicht das Mysterium
- [ ] Store-Beschreibung stellt Evidenz-Methodik voran
- [ ] Reviewer Notes mit redaktionischer Methodik beigelegt
- [ ] Datenschutzerklärung, Nutzungsbedingungen, Notice-and-Takedown-Verfahren live
- [ ] Kontaktweg für Korrekturmeldungen sichtbar in der App

---

## 4. ROADMAP

```
M0 ─────── M2 ─────── M4 ─────── M6 ─────── M9 ─────── M12 ────── M18
│          │          │          │          │          │          │
│ FUNDAMENT│ PRODUKTION│  BETA   │  LAUNCH  │   V1.5   │    V2    │  V3
│          │          │          │          │          │          │
├ Policy   ├ Content  ├ 600 Ein- ├ 1.000    ├ Ligen    ├ AI       ├ Web
├ Schema   │  ×3 Auto-│  träge   │  Einträge├ Freunde  │  Analyst ├ SEO
├ CMS      │  ren     ├ Beta 500 ├ Store-   ├ Widget   ├ Constel- ├ i18n
├ 10 Ref-  ├ App-Dev  │  Tester  │  Launch  ├ 2.500    │  lation  ├ Community
│  Files   ├ Design-  ├ Balancing├ PR / TikTok  Einträge├ Entity-  ├ EDU-B2B
├ Prototyp │  System  │          │          │          │  Seiten  │
```

### Gates zwischen den Phasen

| Gate | Bedingung zum Weitergehen |
|---|---|
| Fundament → Produktion | 10 Referenz-Files abgenommen; Rabbit-Hole-Logik funktioniert auf kleinem Graph; CMS produktiv |
| Produktion → Beta | 600 Einträge; Core Loop vollständig spielbar |
| Beta → Launch | D7-Retention ≥ 18 % in der Beta; Crash-free ≥ 99,5 %; Content-Checkliste erfüllt |
| Launch → V1.5 | D30 ≥ 10 %; Abo-Konversion ≥ 2 % |
| V1.5 → V2 | 2.500 Einträge (RAG-Grundlage tragfähig); MAU ≥ 50k |

---

## 5. METRIKEN

**North Star:** WAU, die ≥ 3 Daily Files pro Woche abschließen.

| Metrik | Beta | Launch +3M | Launch +12M |
|---|---|---|---|
| D1 Retention | 35 % | 40 % | 45 % |
| D7 Retention | 18 % | 20 % | 25 % |
| D30 Retention | 8 % | 10 % | 14 % |
| Daily-File-Completion | 50 % | 60 % | 65 % |
| Ø Rabbit-Hole-Tiefe | 5 | 7 | 9 |
| Run-Completion | 35 % | 45 % | 50 % |
| Share-Rate / Run | 4 % | 8 % | 10 % |
| Abo-Konversion | — | 2 % | 4 % |
| **Calibration Δ über 30 Tage** | +5 | +8 | +10 |

Die letzte Zeile ist die wichtigste. Wenn sie hält, ist Conspiracy Files
nachweislich ein Medienkompetenz-Produkt mit Unterhaltungsmechanik — und das
verändert Presse, Preissetzung, Store-Positionierung und B2B-Potenzial.

---

## 6. OFFENE ENTSCHEIDUNGEN

Punkte, die vor Produktionsbeginn entschieden werden müssen:

| # | Frage | Empfehlung | Muss entschieden werden bis |
|---|---|---|---|
| 1 | Wird die Calibration-Mechanik als Leitmetrik übernommen? | **Ja** — sie ist der USP und die Store-Versicherung | vor Design-System |
| 2 | Vier Daily-Mechaniken zu einer bündeln? | **Ja** — Daily File | vor Home-Screen-Design |
| 3 | Content-Sprache bei Launch | **Nur Englisch** — größter Markt, halbe Content-Kosten | vor Content-Produktion |
| 4 | Werden Tier-3-Themen überhaupt aufgenommen? | **Ja, aber nach Tier-3-Regeln** — sie auszulassen wäre eine inhaltliche Lücke; sie unbehandelt zu lassen überlässt das Feld anderen | vor Redaktionsplan |
| 5 | Eigenes Backend oder Supabase | **Supabase für V1** — es *ist* Postgres, kein Lock-in | vor Backend-Start |
| 6 | Team-Größe Content | **Mind. 1 Lead + 3 Autor:innen + 1 Fact-Checker** — sonst rutscht der Launch | sofort |
| 7 | Ads in V1? | **Nein** — Brand-Safety-eCPM zu niedrig, Vertrauensschaden zu hoch | vor Monetarisierungs-Build |
