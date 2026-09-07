# CONSPIRACY FILES — PRODUCT BLUEPRINT

> **CONSPIRACY FILES**
> *Enter the rabbit hole.*

**Dokument-Status:** v1.0 — Konzeptphase, noch kein Code
**Autor:** Produktkonzeption
**Zweck:** Vollständiges Product Blueprint als Grundlage für MVP-Bau

---

## 0. LESEHINWEIS — WAS ICH ANDERS EMPFEHLE

Ich übernehme die Idee nicht blind. Fünf Punkte weiche ich substanziell ab.
Sie stehen bewusst am Anfang, weil sie das gesamte Produktdesign verändern:

| # | Deine Idee | Meine Empfehlung | Warum |
|---|---|---|---|
| 1 | 4 parallele Daily-Mechaniken (Theory of the Day, Quiz of the Day, Believe It or Not, Streak) | **Ein einziges tägliches Ritual: THE DAILY FILE** (Predict → Reveal → Quiz), eine Streak, eine Notification, eine Share Card | Vier halbe Daily-Features zersplittern die Gewohnheit. Ein gebündeltes tägliches Format ist das Wordle-Prinzip und der stärkste Retention-Hebel, den dieses Produkt hat. |
| 2 | XP als zentrale Nutzer-Metrik | **CALIBRATION SCORE als Leitmetrik**, XP nur als Fortschrittswährung | XP misst Zeit. Calibration misst Können ("Wie gut erkennst du, was belegt ist?"). Das ist teilbar, neuartig, PR-fähig — und macht die App messbar zu einem Medienkompetenz-Tool statt zu einer Verschwörungs-Sammlung. Das ist gleichzeitig deine App-Store- und Presse-Versicherung. |
| 3 | Ein Evidence Status pro Theorie | **Evidence Status pro CLAIM**, plus ein Rollup auf Datei-Ebene, explizit beschriftet als "Status der Kernbehauptung" | Der größte inhaltliche Fehler, den diese App machen kann: ein Badge auf ein Thema stempeln, das belegte *und* falsche Teile enthält. JFK ist genau so ein Fall. Pro-Claim-Status ist die einzige ehrliche Lösung und setzt deine Redaktionsregel (§8) strukturell durch. |
| 4 | Graph-Visualisierung des Netzwerks im MVP | **Nachbarschafts-Ansicht (max. 8 Knoten) + Breadcrumb im MVP.** Vollständiger Graph ("Constellation") erst in V2 | Ein force-directed Graph mit 1.000+ Knoten ist auf dem Handy ein Demo, kein Feature. Unlesbar, teuer, kein Nutzwert. Die lokale Nachbarschaft liefert 90 % des Gefühls für 10 % des Aufwands. |
| 5 | Random Theory als prominenter Hero-Button | **Random wird zum Startpunkt-Generator für Rabbit Holes**, nicht zum eigenständigen Hero | Random allein ist ein Spielautomat ohne Gedächtnis: hohe Klickrate, null Retention. Als "Wirf mich irgendwo in den Graph und lass mich tauchen" wird derselbe Button zum stärksten Discovery-Einstieg. |

Dazu ein **kritisches Risiko, das ganz oben stehen muss** und in deinem Prompt fehlt:
Diese App kann an der App-Store-Freigabe scheitern, rechtlich angreifbar werden und
von genau der falschen Zielgruppe adoptiert werden. Das ist kein Detail, das ist eine
Design-Vorgabe. Siehe **§20 Risiken** und die **Harm-Tier-Systematik** in
[`02-EDITORIAL-POLICY.md`](02-EDITORIAL-POLICY.md).

---

## 1. FINALE POSITIONIERUNG

**Name:** CONSPIRACY FILES (bestätigt)
**Tagline (in-app):** ENTER THE RABBIT HOLE.
**Tagline (Store / Presse):** *The evidence-based archive of everything people believe.*

### Warum CONSPIRACY FILES und nicht RABBIT HOLE

- **ASO:** "conspiracy" ist der Suchbegriff, den Menschen tatsächlich eintippen. "Rabbit hole" nicht.
- **Marken-Freiraum:** "Rabbit Hole" ist als Marke stark überbelegt (Podcasts, Serien, Apps, Spiele). "Conspiracy Files" ist ebenfalls generisch, aber im App-Kontext freier und mit dem Zusatz eindeutiger.
- **Semantik:** "Files" trägt die zentrale Metapher, "Rabbit Hole" trägt die zentrale Handlung. Die Kombination ist stärker als jede Hälfte.

**Store-Titel:** `Conspiracy Files: Rabbit Hole`
**Store-Subtitle:** `Investigate. Verify. Go deeper.`

### Positionierungssatz

> Conspiracy Files ist das erste Archiv, das Verschwörungstheorien nicht als Liste,
> sondern als **verbundenes Netzwerk** katalogisiert — und jede einzelne Behauptung
> darin sichtbar an ihrer **Beweislage** misst.

### Was es ausdrücklich *nicht* ist

- Keine Plattform, die Theorien verbreitet oder bestätigt
- Kein Debunking-Portal, das sich über Gläubige lustig macht
- Keine Wikipedia-Kopie im dunklen Theme
- Kein Nachrichten- oder Community-Produkt (jedenfalls nicht in V1)

### Der Ton (das schwierigste Element)

**Neugierig, präzise, respektvoll, nie überheblich.**
Die App sagt nie "das ist Blödsinn". Sie sagt: *Das wird behauptet. Das ist belegt.
Das ist nicht belegt. Das wurde widerlegt — und so.*
Wer sich verspottet fühlt, schließt die App. Wer sich ernst genommen fühlt, liest weiter.
Das ist keine Höflichkeit, das ist Retention.

---

## 2. USP

Drei Bausteine, von denen **keiner allein verteidigungsfähig** ist — die Kombination ist es:

1. **Das Netzwerk.** Theorien sind über *typisierte* Kanten verbunden (`SPAWNED`, `SHARES_ACTOR`, `ESCALATES`, `DOCUMENTED_BASIS` …). Kein Wettbewerber hat das. Wikipedia hat Links, aber keine Semantik, keine Tiefensteuerung, kein Erlebnis.
2. **Die Evidenz-Schicht.** Jede Behauptung trägt einen sichtbaren, begründeten Status mit Quellen. Das macht aus Content eine Bewertung — und aus einer Datenbank ein Werkzeug.
3. **Der Rabbit Hole als Spielmechanik.** Ein geführter, aber selbstgesteuerter Abstieg mit steigender Obskurität, persönlicher Bestleistung und teilbarem Pfad.

### Die eine Zeile, die die App verkauft

> **"Ich wusste nicht, dass es diese Theorie gibt — und ich wusste nicht, dass dieser Teil davon wahr ist."**

Der zweite Halbsatz ist der eigentliche USP. Die Überraschung, dass ein Teil
belegt ist (MKULTRA, COINTELPRO, Operation Northwoods, Tuskegee), ist emotional
stärker als jede erfundene Theorie — und sie ist gratis, weil sie historisch ist.

---

## 3. ZIELGRUPPE

### Primär — "The Curious Skeptic" (60 % des Zielmarkts)

18–34, überdurchschnittlich gebildet, konsumiert True Crime, Dokus, Lex-Fridman-/
Podcast-Kultur, Reddit (r/UnresolvedMysteries, r/AskHistorians). **Glaubt die
Theorien nicht**, findet sie faszinierend. Will Wissen, das man auf einer Party
erzählen kann. Sucht das Gefühl von Tiefe, nicht von Bestätigung.
→ *Das ist der Kunde. Für den wird gebaut.*

### Sekundär — "The Trivia Competitor" (25 %)

Quiz-App-Nutzer (QuizUp-Erbe, Duolingo-Streak-Mentalität). Kommt wegen Gamification,
bleibt wegen Content. Treiber für Leaderboards, Streaks, Share Cards.

### Tertiär — "The Media Literacy Audience" (15 %)

Lehrkräfte, Journalismus-/Politikstudierende, Eltern. Kleine Gruppe, aber
überproportional wichtig für **Presse, Feature-Placements und institutionelle
Glaubwürdigkeit**. Die Calibration-Mechanik ist für sie gebaut.

### Ausdrücklich NICHT die Zielgruppe

Menschen, die Bestätigung für Überzeugungen suchen. Die App wird sie enttäuschen —
und das ist beabsichtigt. Ein Produkt, das diese Gruppe zufriedenstellen will,
ist nicht publizierbar. Diese Entscheidung muss bewusst und früh getroffen werden,
weil sie Content, Tonalität und Marketing bestimmt.

### Markt-Größenordnung (grobe Einordnung)

- "Conspiracy" / "unexplained" / "mystery" Apps: kleiner, schlecht bedienter Longtail, meist Ad-Ware mit 2–3★
- Vergleichbare Nische mit funktionierendem Abo: True-Crime-Apps, Astro-/Mystery-Apps, Wissens-Apps (Blinkist-Klasse)
- Realistische Erwartung Jahr 1: 100k–500k Downloads bei guter organischer Distribution, 2–4 % Abo-Konversion

---

## 4. APP-STRUKTUR

### Bottom Navigation — 5 Tabs

```
   HOME        ARCHIVE      ◉ RABBIT HOLE      QUIZ       PROFILE
```

- **HOME** — Daily File, Einstiegspunkte, kuratierte Regale
- **ARCHIVE** — Suche, Filter, Kategorien, Collections (die "Datenbank")
- **RABBIT HOLE** — zentral, visuell hervorgehoben (Rabbit-Mark statt Icon-Standard), startet/setzt einen Run fort
- **QUIZ** — alle Modi, Trainingsbereich
- **PROFILE** — Level, Calibration, Case Log, Achievements, Settings

Begründung gegen "EXPLORE": **ARCHIVE** ist das Markenwort aus deiner eigenen
Markenarchitektur (§27) und beschreibt präziser, was der Tab tut.
"Files" wäre die Alternative, aber "Archive" umfasst auch Collections und Suche.

### Screen-Inventar (MVP)

```
HOME
├── Daily File (Predict → Reveal → Quiz)
├── Continue Rabbit Hole (nur wenn Run offen)
├── Shelf: EDITOR'S PICKS
├── Shelf: DOCUMENTED — "This actually happened"
├── Shelf: DEEP CUTS (Obscurity 7+)
└── Shelf: NEW IN THE ARCHIVE

ARCHIVE
├── Search (Entity-aware)
├── Filter Sheet (Category, Evidence, Obscurity, Era, Region)
├── Category Grid
├── Collections / Casefiles
└── File List

FILE DETAIL
├── Header: FILE #, Titel, Status-Chip, Obscurity
├── THE CLAIM
├── ORIGIN
├── THE STORY
├── KEY FIGURES  (verlinkte Entities)
├── CLAIM BREAKDOWN  ← Kernstück: Claims mit je eigenem Status
├── EVIDENCE  /  COUNTERPOINTS
├── ASSESSMENT
├── SOURCES
├── CONNECTED FILES (typisierte Nachbarschaft, max. 8)
└── [ ENTER RABBIT HOLE FROM HERE ]

RABBIT HOLE
├── Entry (aus File / Random / Category)
├── Node Card (Hook + 2–3 typisierte Wege)
├── Breadcrumb Trail
├── Depth Meter
└── Run Summary  → Share Card

QUIZ
├── Classic (10 Fragen)
├── Speed
├── Documented or Debunked?  (Binär-Sortierer)
├── Rabbit Hole Quiz (Tiefenmodus)
└── Result → Share Card

PROFILE
├── Rank / Level / XP
├── CALIBRATION SCORE  ← Leitmetrik
├── Stats (Files, Deepest Run, Streak, Accuracy)
├── Case Log (gespeicherte Runs)
├── Achievements
└── Settings
```

---

## 5. KOMPLETTE USER JOURNEY

### 5.1 First Session — Ziel: Time-to-Wow < 30 Sekunden

**Kein Signup-Wall.** Account erst, wenn es etwas zu verlieren gibt.

```
[0s]   Cold Open — schwarzer Screen, Wortmarke, ein Satz:
       "Some of it is true. That's the problem."
       [ BEGIN ]

[5s]   3 Interessen wählen (aus 12 Kacheln)
       → nur zur Erstpersonalisierung, überspringbar

[12s]  SOFORT ein 3-Schritt-Mini-Rabbit-Hole.
       Schritt 1 ist IMMER eine historisch belegte Verschwörung
       (MKULTRA, COINTELPRO, Operation Northwoods, Tuskegee).
       → "Das ist echt?" ist der stärkste erste Eindruck, den die App hat.

[45s]  Believe It or Not? — erste Einschätzung abgeben
       → Reveal → erster Calibration-Datenpunkt → "+150 XP"

[70s]  "SAVE YOUR PROGRESS?" — Soft-Prompt für Account
       (Apple / Google / E-Mail; Skip erlaubt, lokaler Fortschritt bleibt)

[90s]  Home Screen, Streak Day 1 aktiv, Notification-Prompt
       (erst NACH dem ersten Erfolgserlebnis, nie davor)
```

Die Entscheidung, mit einer **belegten** Verschwörung zu starten, ist die
wichtigste einzelne Onboarding-Entscheidung des Produkts. Sie entwaffnet sofort
den Vorwurf "die App erklärt eh alles für Blödsinn" und etabliert die Glaubwürdigkeit,
die nötig ist, um später überzeugend zu widerlegen.

### 5.2 Returning Session — Ziel: < 4 Minuten, vollständig befriedigend

```
Push (variabel, 1×/Tag, nutzerdefinierte Uhrzeit):
"FILE #0412 is open. Do you believe it?"
   ↓
DAILY FILE
   ├─ 1. PREDICT   "How likely is this claim substantially true?"  [Slider 0–100]
   ├─ 2. REVEAL    Status + Begründung + Calibration-Delta
   ├─ 3. READ      Die Akte (oder "Read later")
   └─ 4. QUIZ      3 Fragen, ausschließlich aus dieser Akte beantwortbar
   ↓
Streak +1 · XP · Share Card angeboten
   ↓
"CONTINUE THE THREAD?"  → Rabbit Hole aus dieser Akte
```

### 5.3 Deep Session — der eigentliche Suchtpfad

```
Rabbit Hole Run
 → 6–25 Knoten
 → Obskurität steigt monoton
 → jeder Knoten: Hook + Wahl zwischen 2–3 typisierten Wegen
 → Ende: BOTTOM REACHED → Pfad-Zusammenfassung → Case Log → Share
Dauer: 8–30 Minuten. Das ist die Session, für die Leute die App behalten.
```

---

## 6. CORE LOOP

```
        ┌──────────────────────────────────────────────┐
        │                                              │
        ▼                                              │
   DISCOVER  ──►  PREDICT  ──►  READ FILE  ──►  CONNECT
   (Daily/Random)  (Belief)     (Evidence)      (typed link)
                      │                             │
                      ▼                             ▼
              CALIBRATION ◄────── QUIZ ◄──── RABBIT HOLE
                 SCORE             XP          (deeper)
                      │             │              │
                      └─────────────┴──────────────┘
                                    ▼
                          LEVEL UP · STREAK · SHARE
                                    │
                                    └──► zurück zu DISCOVER
```

**Drei ineinandergreifende Schleifen — bewusst unterschiedlich getaktet:**

| Loop | Taktung | Zweck | Kernmechanik |
|---|---|---|---|
| **Micro** | 30 s | Sofortbefriedigung | Predict → Reveal (Überraschung) |
| **Daily** | 3–5 min | Gewohnheit | Daily File + Streak |
| **Deep** | 10–30 min | Bindung & Identität | Rabbit Hole Run + persönlicher Rekord |

Die meisten Wissens-Apps haben nur den Daily Loop. Der **Deep Loop** ist hier
das Differenzierungsmerkmal — und der Grund, warum Nutzer die App nicht
nach zwei Wochen löschen.

---

## 7. INFORMATIONSARCHITEKTUR

### Drei Zugriffsachsen auf denselben Content

1. **Taxonomisch** — Kategorien, Subkategorien, Tags, Ära, Region *(Archive)*
2. **Relational** — typisierte Kanten zwischen Files und Entities *(Rabbit Hole)*
3. **Editorial** — Collections, Casefiles, Regale, Daily File *(Home)*

Ein Content-Objekt, drei Wege. Das ist die IA-Grundentscheidung: **nichts wird dupliziert.**

### Kategorien — konsolidiert

Deine Liste hat 25 Kategorien. Das ist für eine Filter-UI auf dem Handy zu viel
und die Trennschärfe leidet (Government/Politics/Military/Intelligence überlappen fast vollständig).

**Empfehlung: 10 Top-Level-Kategorien, alles andere als Tag.**

| Kategorie | Deckt ab |
|---|---|
| **POWER** | Government, Politics, Deep State, New World Order |
| **SECRET SOCIETIES** | Illuminati, Freemasons, Bilderberg, Bohemian Grove |
| **INTELLIGENCE** | CIA/KGB/MI6, Secret Projects, Assassinations, Psy-Ops |
| **THE SKY** | UFOs, Aliens, Space, Moon, Satellites |
| **BODY & MIND** | Medicine, Health, Mind Control, Psychology |
| **MONEY** | Finance, Banking, Corporations, Crypto |
| **THE PAST** | Ancient Civilizations, Lost History, Archaeology |
| **THE UNEXPLAINED** | Paranormal, Cryptids, Disappearances, Deaths |
| **THE NETWORK** | Internet, Tech, Surveillance, AI, Media |
| **BELIEF** | Religion, Cults, Prophecy, Apocalypse |

Tags bleiben frei und beliebig viele (`cold-war`, `1960s`, `declassified`,
`cia`, `assassination`, `antisemitic-trope`, `health-misinfo` …). Tags tragen
die Feingranularität, Kategorien tragen die Navigation. Ein File hat 1–3
Kategorien und 5–15 Tags.

### Suche

Suche muss **entity-aware** sein, nicht nur Volltext:

```
"CIA"      → Entity-Karte "Central Intelligence Agency"
             + 84 verbundene Files, gruppiert nach Rolle
"JFK"      → Entity + Event + 23 Files
"1947"     → Zeitachse: Roswell, National Security Act, CIA-Gründung …
"shadows"  → Volltext in Claims/Evidence
```

Das erfordert eine **normalisierte Entity-Tabelle** (Personen, Organisationen,
Orte, Events, Projekte) statt Freitext-Feldern auf dem File. Siehe
[`01-DATA-MODEL.md`](01-DATA-MODEL.md).

---

## 8. DATENBANKSTRUKTUR

Vollständige Spezifikation inkl. DDL: **[`01-DATA-MODEL.md`](01-DATA-MODEL.md)**

Die vier Entscheidungen, die alles bestimmen:

1. **`claim` ist eine eigene Tabelle.** Ein File hat n Claims, jeder Claim hat
   einen eigenen Evidence Status. Der File-Status ist nur der Rollup des als
   `is_core` markierten Claims. → setzt §8 strukturell durch.
2. **`entity` ist normalisiert.** "CIA" ist eine Zeile, keine 84 Strings.
   → ermöglicht Suche, Graph-Kanten über gemeinsame Akteure, Entity-Seiten.
3. **`file_link` trägt einen Relationstyp und eine Begründung.**
   → macht den Rabbit Hole *kuratiert* statt zufällig.
4. **`source` ist normalisiert und braucht einen auflösbaren Identifier**
   (URL, DOI, ISBN, Archiv-Signatur). Ohne Identifier kein Publish.
   → strukturelle Absicherung gegen erfundene Quellen (§35).

### Relationstypen (Kantentypen)

| Typ | Bedeutung | Beispiel |
|---|---|---|
| `SPAWNED` | A brachte B hervor | Pizzagate → QAnon |
| `PRECURSOR_OF` | A ging B historisch voraus | Protocols → moderne NWO-Narrative |
| `SHARES_ACTOR` | Gemeinsame Person/Organisation | MKULTRA ↔ Operation Midnight Climax |
| `SHARES_EVENT` | Gemeinsames Ereignis | Roswell ↔ Project Mogul |
| `ESCALATES` | Radikalere Version derselben Behauptung | Chemtrails → Geoengineering-Weltkontrolle |
| `CONTRADICTS` | Die beiden Theorien schließen sich aus | zwei konkurrierende JFK-Täterthesen |
| `REBUTTED_BY` | Verweist auf die Widerlegung | Moon Hoax → Lunar Reconnaissance Orbiter Imagery |
| **`DOCUMENTED_BASIS`** | **Der reale, belegte Kern darunter** | **Majestic 12 → Project Blue Book** |

`DOCUMENTED_BASIS` ist der wichtigste Kantentyp des Produkts. **Regel: Jedes
spekulative File soll, wo möglich, mindestens eine solche Kante haben.** Damit
erzwingt die Graph-Struktur selbst die redaktionelle Mission — der Rabbit Hole
führt nicht nur tiefer ins Unbelegte, sondern immer wieder zurück auf Boden.

### Scores

**Obscurity Score (1–10)** — berechnet, nicht geraten:

```
obscurity_raw =
    0.30 × (1 − norm(wikipedia_pageview_band))
  + 0.30 × (1 − norm(search_volume_band))
  + 0.20 × (1 − norm(media_mention_band))
  + 0.20 × (1 − norm(in_app_open_rate))      // erst ab 1.000 Opens gewichtet

obscurity_score = dezil_bucket(obscurity_raw, über gesamtes Korpus)  → 1..10
```

Dezil-Bucketing über das Gesamtkorpus garantiert, dass immer die volle Skala
1–10 belegt ist, egal wie sich das Korpus verändert. Externe Signale werden zum
Redaktionszeitpunkt eingefroren und quartalsweise neu erhoben.
**Der Score ist eine Heuristik für Bekanntheit — nicht für Wahrheit.**
Das muss in der UI stehen.

**Popularity Score** — intern gepflegt (Opens, Completion, Shares), aber
**nicht als zweite Sterne-Leiste in der UI ausspielen**. Obscurity und Popularity
sind nahezu invers; beides zu zeigen ist redundanter UI-Lärm. Nach außen:
Obscurity-Skala + ggf. ein `TRENDING`-Badge. Popularity bleibt Ranking-Signal.

---

## 9. QUIZ-SYSTEM

### Grundregel (nicht verhandelbar)

**Jede Frage muss ausschließlich aus der verknüpften Akte und deren Quellen
beantwortbar sein.** Keine Frage über eine unbelegte Behauptung, die eine
unbelegte Behauptung als richtige Antwort hat. Sonst bringt die App Falsches bei.
Technisch: `quiz_question.file_id` + `quiz_question.claim_id` sind Pflichtfelder,
`source_ref` ebenfalls.

### Modi

| Modus | Format | XP | Zweck |
|---|---|---|---|
| **CLASSIC** | 10 Fragen, 4 Optionen | 100/Frage | Basis, ohne Zeitdruck |
| **SPEED** | 10 Fragen, 15 s, Zeitbonus | 100 + max. 50 | Kompetitiv |
| **DOCUMENTED OR DEBUNKED?** | Binär-Sortierer, 20 Karten, 60 s | 60/Karte, Combo-Bonus | **Der markenprägende Modus** |
| **RABBIT HOLE QUIZ** | Endlos, Obskurität steigt, 3 Leben | 100 → 1000 skalierend | "How deep can you go?" |
| *DAILY (in Home)* | 3 Fragen zur Tagesakte | 100/Frage | Habit |

**DOCUMENTED OR DEBUNKED?** ist der beste Quiz-Modus für dieses Produkt und sollte
der Hero sein, nicht Classic. Er ist schneller, thematisch eigenständiger, besser
teilbar — und er trainiert exakt die Fähigkeit, um die es der App geht. Klassische
MC-Trivia gibt es überall; dieser Modus gibt es nur hier.

### Schwierigkeit — automatisch aus Content-Metadaten

`question.difficulty = f(file.obscurity_score, claim.evidence_status_ambiguity)`

Damit macht der Obscurity Score doppelte Arbeit: Er steuert Discovery **und**
die Quiz-Progression. Keine separate manuelle Schwierigkeitspflege nötig.

### Anti-Cheese

- Fragenpools pro File (mind. 5 Fragen je Tier-A-File), Rotation, kein Repeat bis Pool erschöpft
- Antwortoptionen serverseitig geshuffelt, korrekte Antwort nie im Client-Payload vor Abgabe
- Zeitbonus gedeckelt (max. 33 % der Frage-XP), sonst misst das Leaderboard Reflexe statt Wissen
- Serverseitige XP-Vergabe, Client-Werte nie vertrauen

### Bedarf

- MVP: **≥ 600 Fragen** (150 Tier-A-Files × ~4)
- Nachschub: ~100 Fragen/Monat, um Speed-/Daily-Nutzer nicht zu erschöpfen

---

## 10. RABBIT-HOLE-SYSTEM

Das Herzstück. Naiv umgesetzt ("folge Links bis Sackgasse") produziert es
Zyklen, Sackgassen und Qualitätsverfall. Deshalb als **kuratierter Pfad-Generator**:

### Regeln eines Runs

1. **Monotone Tiefe:** `obscurity(n+1) ≥ obscurity(n) − 1`, im Mittel steigend.
2. **Keine Wiederholung** innerhalb eines Runs.
3. **Wahl statt Autoplay:** Jeder Knoten bietet **2–3 Wege**, jeweils beschriftet
   mit dem *Relationstyp*, nicht nur dem Titel:
   ```
   →  SHARES AN ACTOR      Operation Midnight Climax
   →  THIS GREW OUT OF IT  Project ARTICHOKE
   →  THE DOCUMENTED CORE  Church Committee Hearings
   ```
   Agency ist der Unterschied zwischen "ich scrolle" und "ich erkunde".
   Und sie erzeugt einen **persönlichen Pfad** — die eigentliche teilbare Einheit.
4. **Mindestens ein `DOCUMENTED_BASIS`-Weg alle 4 Knoten**, wo verfügbar.
   Verhindert, dass ein Run monoton immer weiter ins Unbelegte kippt.
5. **Ende:** Kein gültiger nächster Knoten → `BOTTOM REACHED`.

### Node Card (das UI-Atom des Runs)

```
LEVEL 07                                    OBSCURITY 6/10
────────────────────────────────────────────────────────
FILE #1183
PROJECT SUNSHINE
🟢 DOCUMENTED

Zwischen 1953 und 1957 sammelte die US-Atomenergiekommission
weltweit Leichenteile — meist von Säuglingen — um Strontium-90
aus Atomtests zu messen. Meist ohne Zustimmung der Familien.

[ OPEN FULL FILE ]        [ CONTINUE ▸ ]
```

Ein Hook pro Knoten: **eine belegte, konkrete, überraschende Tatsache.** Nicht
die Zusammenfassung der Theorie — der Haken.

### Tiefe & Rekord

- `depth` = Anzahl Knoten in einem Run
- "Deepest Rabbit Hole: Level 87" ist ein **Lebenszeit-Rekord**, kein Single-Session-Wert.
  Ein Run ist als **Thread** speicher- und fortsetzbar (Case Log), Tiefe akkumuliert im Thread.
- **Ehrliche Erwartung:** Mit ~1.000 Einträgen bei Launch sind Threads realistisch
  20–30 Knoten tief, nicht 87. Level 87 ist ein Ziel für V2+ bei 5.000+ Einträgen.
  Lieber ein echter Rekord von 24 als ein aufgeblasener von 87.

### Run Summary — die virale Einheit

```
YOU WENT 14 LEVELS DEEP

MOON LANDING HOAX  →  Project Blue Book  →  Majestic 12
 →  Roswell  →  Project Mogul  →  Operation Paperclip
 →  … →  PROJECT SUNSHINE

4 DEBUNKED · 6 DOCUMENTED · 4 UNVERIFIED
DEEPEST OBSCURITY: 8/10

[ SHARE PATH ]   [ SAVE TO CASE LOG ]
```

Der **Pfad selbst** ist das teilbare Artefakt — nicht die Punktzahl. Zwei Leute
mit demselben Startpunkt landen woanders. Das ist inhärent gesprächsfähig.

---

## 11. GAMIFICATION

### 11.1 CALIBRATION SCORE — die Leitmetrik

Kern der Empfehlung Nr. 2. Der Nutzer schätzt vor dem Reveal, wie wahrscheinlich
eine Kernbehauptung substanziell zutrifft (0–100 %). Bewertet wird mit dem
**Brier Score**:

```
brier = (p_user − p_target)²          // 0 = perfekt, 1 = maximal daneben
calibration = round((1 − mean(brier_letzte_50)) × 100)
```

`p_target` ist ein **redaktionell gesetztes Band** pro Evidence Status:

| Status | p_target | angezeigtes Band |
|---|---|---|
| 🟢 DOCUMENTED | 0.95 | 90–100 % |
| 🔵 PARTLY DOCUMENTED | 0.65 | 50–80 % |
| 🟠 CONTESTED | 0.50 | 35–65 % |
| 🟡 UNVERIFIED | 0.25 | 10–40 % |
| 🔴 DEBUNKED | 0.03 | 0–10 % |

**Transparenzpflicht in der UI:** Das ist eine redaktionelle Einschätzung der
Beweislage, keine gemessene Wahrheitswahrscheinlichkeit. Angezeigt wird das
**Band**, nie ein Punktwert mit Scheingenauigkeit. Nutzer innerhalb des Bands
gelten als "kalibriert".

Warum das so wertvoll ist:
- Es misst **Können statt Zeit** → echtes Fortschrittsgefühl, das XP nie liefert
- Es ist **teilbar und herausfordernd** ("Ich bin bei 81. Wie kalibriert bist du?")
- Es macht die App **messbar zu einem Medienkompetenz-Werkzeug** → Presse, Feature-Chancen, Store-Review-Argument
- Es ist **nicht kopierbar ohne die Evidenz-Schicht** → Wettbewerbsschutz

### 11.2 XP & Level

XP bleibt als Fortschrittswährung, aber nachrangig.

| Aktion | XP |
|---|---|
| Prediction abgegeben | 50 |
| Prediction im Band | +100 |
| File gelesen (>60 % scroll, >30 s) | 100 |
| Quiz-Frage richtig | 100 |
| Zeitbonus (Speed) | max. +50 |
| Combo (3/5/10 in Folge) | +100 / +250 / +600 |
| Obskures File entdeckt (Obs. 7–8) | +250 |
| Sehr obskures File (Obs. 9–10) | +500 |
| Rabbit-Hole-Knoten | 75 |
| Run abgeschlossen (BOTTOM) | +500 |
| Daily File komplett | +200 |
| Streak-Multiplikator | ×1.0 → ×1.5 (Tag 30) |

**Kurve:** `xp_to_next(n) = round(100 + 55 × (n−1)^1.35)`

| Level | Kumulativ | Realistisch erreicht nach |
|---|---|---|
| 10 | ~5.100 | ~1 Woche |
| 25 | ~26.000 | ~6 Wochen |
| 50 | ~97.000 | ~5 Monate |
| 100 | ~410.000 | ~18 Monate |

Bei ~600–900 XP pro engagiertem Tag. Level 100 muss erreichbar, aber ein
echtes Statement sein.

### 11.3 Ränge

100 einzelne Level-Namen sind Pflegeaufwand ohne Nutzen. **10 Ränge über 100 Level:**

| Rang | ab Level |
|---|---|
| CURIOUS | 1 |
| OBSERVER | 5 |
| RESEARCHER | 10 |
| INVESTIGATOR | 18 |
| ANALYST | 28 |
| ARCHIVIST | 40 |
| CASE OFFICER | 55 |
| DEEP DIVER | 70 |
| CONSPIRACY SCHOLAR | 85 |
| KEEPER OF THE ARCHIVE | 100 |

Angezeigt wird `ANALYST · LEVEL 32`. Der Rang trägt Identität, das Level trägt Fortschritt.

### 11.4 Achievements — 40 bei Launch

Verteilung: 12 leicht (Woche 1), 16 mittel (Monat 1–2), 8 schwer (Monat 3+),
**4 geheim** (als `CLASSIFIED ████████` mit Redaction-Bar dargestellt — thematisch perfekt).

Beispiele über deine Liste hinaus:
- **CALIBRATED** — 20 Predictions in Folge im Band
- **DEVIL'S ADVOCATE** — 10 Files gelesen, deren Status du falsch eingeschätzt hattest
- **PAPER TRAIL** — 50 Quellen geöffnet
- **THE REAL ONES** — alle Files mit Status DOCUMENTED in einer Kategorie
- **CROSS-REFERENCE** — zwei Runs, die sich an einem Knoten kreuzen
- **NO SLEEP TONIGHT** *(geheim)* — 25 Files zwischen 02:00 und 05:00
- **DEAD END** *(geheim)* — den Boden eines Rabbit Hole 3× erreicht

### 11.5 Streaks

Ein Streak-Zähler, eine Bedingung: **Daily File abgeschlossen.**
Nicht drei konkurrierende Streaks. Ein **Streak Freeze** pro Monat gratis
(zwei für Premium) — Duolingo hat empirisch bewiesen, dass das Churn nach
Streak-Verlust massiv senkt.

### 11.6 Was ich NICHT empfehle

- **Globales Leaderboard im MVP.** Für 99 % der Nutzer unerreichbar und
  damit demotivierend. Stattdessen ab V1.5: **wöchentliche Ligen** mit
  Kohorten von ~30 Spielern (Duolingo-Modell) + Freundesliste. Bounded
  competition schlägt globale Ranglisten in jedem gemessenen Fall.
- **Energie-/Leben-Systeme mit Timer.** Passen nicht zum Explorations-Versprechen.
- **Lootboxen, Gacha, kosmetische Käufe.** Markenschaden.

---

## 12. BRANDING

### Markenarchitektur

```
CONSPIRACY FILES          Dachmarke
└── ENTER THE RABBIT HOLE. Claim
    ├── FILES      Wissensdatenbank
    ├── RABBIT HOLE Discovery-Erlebnis  (Rabbit-Mark)
    ├── QUIZ       Gamification
    ├── ARCHIVE    Sammlung / Navigation
    └── PROFILE    Fortschritt
```

### Logo

**Primär:** Wortmarke `CONSPIRACY FILES`, Grotesk, Versalien, enges Tracking,
zweizeilig gesetzt, `CONSPIRACY` in Regular / `FILES` in Medium.

**Sekundärmarke (App-Icon & Rabbit-Hole-Feature):** Der Rabbit.

Konzept: **geometrische Hasensilhouette, bei der der Negativraum zwischen den
Ohren ein Schlüsselloch bildet.** Konstruiert aus Kreisen und geraden Kanten,
keine Kurvenzeichnung, kein Fell, keine Augen. Strichstärke gleichmäßig.
Auf 24 px noch erkennbar.

Variante für Redaction-Motiv: Die Ohren als zwei schwarze Balken über einer
Grundform — liest sich gleichzeitig als Hase und als geschwärztes Dokument.

**Verboten:** Cartoon-Kaninchen, Alice-in-Wonderland-Zitate, Dreiecke,
Augen-in-Pyramide, Aluhüte, Matrix-Grün, UFO-Silhouetten, Lens Flares, CRT-Scanlines.

### App-Icon

Schwarz. Der Rabbit-Mark in Off-White, zentriert, mit einem einzigen Akzent-Punkt
in Signalrot. Nichts sonst. Im dunklen App-Grid soll das Icon durch Zurückhaltung
auffallen, nicht durch Lautstärke.

---

## 13. UI / UX

### 13.1 Farbwelt

| Token | Hex | Verwendung |
|---|---|---|
| `bg/base` | `#0A0A0B` | App-Hintergrund |
| `bg/surface` | `#121214` | Karten |
| `bg/raised` | `#1A1A1D` | Sheets, Overlays |
| `border/hairline` | `#232327` | 1 px Trennlinien |
| `text/primary` | `#F2F2F0` | Headlines, Fließtext |
| `text/secondary` | `#9A9AA0` | Metadaten |
| `text/tertiary` | `#5C5C63` | Labels, Disabled |
| `accent/signal` | `#C8102E` | **sparsam**: File-Nummer, aktiver Tab, CTA-Kante |

**Akzent-Budget: max. 5 % der sichtbaren Fläche pro Screen.** Rot ist ein Signal,
kein Dekor. Wenn zwei rote Elemente gleichzeitig sichtbar sind, ist eines zu viel.

### 13.2 Evidence-Status-Palette

Muss **getrennt** vom Marken-Akzent stehen, sonst kollidiert Rot als
"Marke" mit Rot als "widerlegt".

| Status | Farbe | Icon | Label |
|---|---|---|---|
| DOCUMENTED | `#2E9E5B` | ● gefüllt | DOCUMENTED |
| PARTLY DOCUMENTED | `#3B82C4` | ◐ halb | PARTLY DOCUMENTED |
| CONTESTED | `#D08432` | ◑ geteilt | CONTESTED |
| UNVERIFIED | `#C9A227` | ○ offen | UNVERIFIED |
| DEBUNKED | `#B33A3A` | ✕ | DEBUNKED |

**Barrierefreiheit-Pflicht: Status = Farbe + Form + Textlabel, immer alle drei.**
Ca. 8 % der männlichen Nutzer unterscheiden Rot/Grün nicht zuverlässig. Ein
farbcodierter Wahrheitsstatus, den ein Teil der Nutzer nicht lesen kann, ist
ein inhaltlicher Fehler, kein Design-Detail.

**Reduktion von 6 auf 5 Status:** `SPECULATIVE` und `UNVERIFIED` überlappen für
Nutzer zu stark. Die Unterscheidung bleibt als Zusatzlabel erhalten
(`UNVERIFIED · no evidentiary basis`), aber nicht als eigene Farbkategorie.
Fünf Chips passen in eine Filterzeile auf dem Handy, sechs nicht.

### 13.3 Typografie

| Rolle | Empfehlung (frei verfügbar) | Verwendung |
|---|---|---|
| Display | **Inter Tight** ExtraBold, Tracking −3 % | File-Titel, Screen-Headlines |
| Body | **Inter** Regular 16/26 | Fließtext |
| Mono | **IBM Plex Mono** | `FILE #00421`, Daten, Metadaten, Timestamps |
| Editorial *(optional)* | **Instrument Serif** | ausschließlich der `THE CLAIM`-Block |

```
FILE #00421                          OBSCURITY 2/10
─────────────────────────────────────────────────────
THE
MOON LANDING
HOAX
🔴 DEBUNKED — core claim
```

Der Serif ausschließlich für das wörtliche Zitat der Behauptung setzt sie
typografisch als *fremde Stimme* ab — die Behauptung spricht, die App nicht.
Ein subtiles, aber wirksames redaktionelles Signal.

### 13.4 Motion

Zurückhaltend. **Eine** Signature-Transition: **Redaction Reveal** — schwarze
Balken gleiten seitlich weg und geben Text frei. Einsatz: Status-Reveal im
Daily File, Achievement-Unlock. Maximal einmal pro Screen. Alles andere:
120–200 ms Standard-Easing.

Rabbit-Hole-Tiefe bekommt eine **kontinuierliche Umgebungsveränderung**: mit
jedem Level wird der Hintergrund minimal dunkler und die Vignette minimal
stärker. Über 20 Level kaum bewusst wahrnehmbar, im Rückblick aber deutlich —
körperliches Gefühl von Tiefe ohne Effekthascherei.

### 13.5 Anti-Patterns

Kein Grunge, keine Papierfetzen, keine roten Fäden mit Pinnadeln, keine
Schreibmaschinen-Font, kein "TOP SECRET"-Stempel auf jedem Screen. Wenn
Textur, dann **eine**: Papierkorn bei 3 % Deckkraft auf `bg/base`. Mehr nicht.

Die Referenz ist nicht "Verschwörungs-Website", sondern:
Netflix-Doku-Titelsequenz × Financial-Times-Layout × Archive-Interface.

---

## 14. MONETARISIERUNG

### Modell: Freemium mit Abo

| | FREE | PREMIUM |
|---|---|---|
| Tier-A- & Tier-B-Files | ✅ vollständig | ✅ |
| **Evidence, Counterpoints, Assessment** | **✅ immer** | ✅ |
| Deep Index (Tier C, obskure Einträge) | 10/Monat | ✅ unbegrenzt |
| Rabbit Hole Runs | 2/Tag | unbegrenzt |
| Daily File + Quiz | ✅ | ✅ |
| Erweiterte Filter (Obscurity, Era, Region) | – | ✅ |
| AI Analyst *(V2)* | – | ✅ |
| Offline / Download | – | ✅ |
| Erweiterte Statistiken & Calibration-Historie | Basis | ✅ |
| Exklusive Quiz-Modi | – | ✅ |
| Werbung | ja (dezent) | keine |

### Absolute Paywall-Regel

> **Evidenz, Gegenargumente und Assessment sind NIEMALS kostenpflichtig.**

Wenn eine Behauptung gratis sichtbar ist, muss ihre Einordnung gratis sichtbar
sein. Alles andere wäre inhaltlich schädlich (die App würde für Geld Falsches
stehen lassen) und ein reales Ablehnungsrisiko im App Review.
Premium verkauft **Breite, Tiefe, Werkzeuge und Komfort** — nie die Korrektur.

### Preise

| Produkt | Preis | Zweck |
|---|---|---|
| Monat | 4,99 € | Einstieg |
| **Jahr** | **29,99 €** (= 2,50 €/Mt.) | **Anker, Hauptprodukt, −50 %** |
| Lifetime | 79,99 € | Superfans, Cashflow früh |

Kein Wochen-Abo — hohe Churn, schlechte Store-Reputation, ruiniert LTV-Wahrnehmung.
7 Tage Trial auf dem Jahresabo. Hard Paywall **nie vor Session 3**.

### Werbung — realistische Erwartung

**Warnung, die eingeplant werden muss:** Programmatic-Advertising auf
Conspiracy-Content unterliegt **Brand-Safety-Blocklists**. "conspiracy",
"QAnon", "vaccine" u. ä. stehen auf Keyword-Sperrlisten praktisch aller
großen Werbetreibenden. Erwartbarer eCPM: deutlich unter Kategoriedurchschnitt.

**Konsequenz: Das Abo muss dieses Produkt tragen. Werbung ist Beiwerk.**
Empfehlung: nur **Rewarded Video** (freiwillig: +1 Rabbit-Hole-Run, +3 Deep-Index-Öffnungen)
und maximal ein Interstitial nach jeder zweiten Quiz-Session. Keine Banner —
sie zerstören die Ästhetik, die das Preispremium rechtfertigt.

### Zielwerte Jahr 1

- Abo-Konversion: 2–4 % der MAU
- Trial→Paid: 35–45 %
- ARPU (gemischt): 0,45–0,90 € / MAU / Monat
- **Break-even braucht ~50k MAU** bei kleinem Team — das ist die Zahl, an der der Businessplan hängt

---

## 15. MVP

### Scope — was V1 enthält

1. Onboarding (3 Interessen, Mini-Rabbit-Hole, Soft-Signup)
2. Home mit **Daily File** (Predict → Reveal → Read → 3 Quiz)
3. Archive: Suche, 10 Kategorien, 5 Filter, Collections
4. File Detail inkl. **Claim Breakdown mit Per-Claim-Status**
5. Connected Files (Nachbarschaft, max. 8, typisiert)
6. Rabbit Hole Runs mit Auswahl-Mechanik, Breadcrumb, Run Summary, Case Log
7. Quiz: Classic, Speed, **Documented or Debunked?**
8. XP, 10 Ränge, Level 1–50 balanciert
9. **Calibration Score**
10. Streak + Streak Freeze
11. 40 Achievements
12. Profil & Statistiken
13. Share Cards (Run Path, Calibration, Quiz Result)
14. Premium-Paywall & Abos
15. **Content: 150 Tier A + 150 Tier B + 700 Index Entries ≈ 1.000 Einträge, 600+ Quizfragen**

### Explizit NICHT im MVP

| Feature | Warum später |
|---|---|
| Vollständige Graph-Visualisierung | Auf dem Handy unlesbar; hoher Aufwand, geringer Nutzwert |
| AI Analyst | Braucht ein reifes Korpus als RAG-Grundlage, sonst halluziniert es genau das, was die App verhindern soll |
| Globale Leaderboards | Cold-Start ohne Nutzer sinnlos; demotivierend |
| Freunde / Social Graph | Erfordert Accounts, Moderation, Privacy-Arbeit |
| User-generierte Theorien | App-Store-Regel 1.2 verlangt Moderation. Eine Conspiracy-App mit UGC ist ein Moderations-Albtraum und ein Ablehnungsrisiko. **Nicht in V1. Nicht in V2.** |
| Werbung | Erst wenn Retention steht; vorher schadet sie mehr, als sie einbringt |
| Kommentare / Foren | Siehe UGC |
| Lokalisierung | Content-Kosten × Sprachen; erst wenn EN validiert ist |

### Cold-Start-Problem — ehrlich lösen

"TRENDING" und "MOST POPULAR" brauchen Nutzer, die es noch nicht gibt.
**Keine erfundenen Zahlen** — Nutzer merken das und es beschädigt die
Glaubwürdigkeitsmarke, auf der das ganze Produkt steht. Stattdessen bei Launch
vier **redaktionell kuratierte** Regale:

```
EDITOR'S PICKS
DOCUMENTED — "This actually happened"
DEEP CUTS  (Obscurity 7+)
NEW IN THE ARCHIVE
```

Algorithmische Regale (Trending, Most Read) werden freigeschaltet, sobald
≥ 5.000 DAU echte Signale liefern.

### Zeit- & Ressourcenschätzung

| Rolle | Aufwand bis Launch |
|---|---|
| Product / Design | 1 Person, 4 Monate |
| Mobile Dev (RN) | 2 Personen, 5 Monate |
| Backend / Data | 1 Person, 4 Monate |
| **Content Lead + 3 Autoren** | **6 Monate — der eigentliche kritische Pfad** |
| Fact-Checker (Teilzeit) | 4 Monate |

**Realistisch: 6–7 Monate bis Store-Launch.** Der Engpass ist der Content,
nicht die App. Wer das umdreht, baut eine schöne, leere App.

---

## 16. SPÄTERE VERSIONEN

### V1.5 — "The League" (Monat 3–5 nach Launch)
- Wöchentliche Ligen (Kohorten ~30) statt globalem Leaderboard
- Freundesliste per Invite-Code
- Collections erweitert, Content auf ~2.500 Einträge
- Trending-Regale live (echte Daten)
- Widget: Daily File auf dem Homescreen

### V2 — "The Constellation" (Monat 6–10)
- **Constellation View:** navigierbarer Graph, aber als *geführte Karte* —
  Cluster-Ebene → Regions-Ebene → Knoten-Ebene, nie 1.000 Knoten gleichzeitig
- **AI ANALYST** (Premium): strikt RAG-gegroundet auf das eigene Korpus.
  Analysiert eine vom Nutzer eingegebene Behauptung Argument für Argument,
  zitiert ausschließlich Files und Quellen aus der Datenbank, sagt bei
  fehlender Abdeckung explizit *"das deckt das Archiv nicht ab"* statt zu improvisieren
- Entity-Seiten (Personen, Organisationen, Orte) als eigene Zielseiten
- Content ~6.000 Einträge

### V3 — "The Network" (Jahr 2)
- Kuratierte Community: Nutzer schlagen *Quellen und Korrekturen* vor,
  nicht ganze Theorien. Redaktionelle Freigabe zwingend.
- Web-App (großer ASO-/SEO-Hebel: File-Seiten sind exzellenter SEO-Content)
- Lokalisierung DE, ES, PT-BR, FR
- Bildungslizenz (Schulen/Unis) — eigenes B2B-Segment für die Calibration-Mechanik

---

## 17. TECHNISCHE ARCHITEKTUR

### Stack-Empfehlung

| Schicht | Wahl | Begründung |
|---|---|---|
| Client | **React Native + Expo**, TypeScript | Ein Codebase iOS/Android; content-lastige App mit moderatem Animationsbedarf; Reanimated + Skia reichen. Flutter wäre gleichwertig — RN gewinnt bei Hiring und Web-Wiederverwendung in V3. |
| State | TanStack Query + Zustand | Server-State und UI-State sauber getrennt |
| Backend | **Supabase (Postgres + Auth + Storage + Edge Functions)** für V1 | Schnellster Weg für ein kleines Team. Es *ist* Postgres — kein Lock-in auf das Datenmodell. Bei Skalierung: eigener Fastify-Service davor, DB bleibt. |
| Datenbank | **PostgreSQL** | siehe unten |
| Suche | Postgres FTS (`tsvector` + `pg_trgm`) → **Typesense** ab ~5k Files | FTS trägt V1 problemlos. Facettensuche macht Typesense besser als Elasticsearch bei einem Zehntel Betriebsaufwand. |
| Semantik / "Related" | **pgvector** | Vorschläge für Kanten im Redaktionstool; nicht als Nutzer-Feature |
| Abos | **RevenueCat** | Store-Abos selbst zu bauen ist verschwendete Zeit |
| Analytics | PostHog (oder Amplitude) | Funnels, Kohorten, Feature Flags |
| Crash / Perf | Sentry | |
| CMS | **Payload** oder **Directus** über dem eigenen Postgres-Schema | Kein generisches Headless-CMS: das Schema (Claims, Evidence, typisierte Kanten, Review-Workflow) ist zu speziell. Aber Admin-UI auch nicht from scratch bauen. |

### Warum Postgres und ausdrücklich **kein** Neo4j

Der reflexhafte Gedanke bei "Netzwerk" ist eine Graphdatenbank. Falsch hier:

- 50.000 Knoten und ~300.000 Kanten sind für Postgres **klein**
- Pfadsuche für Rabbit-Hole-Runs = rekursive CTE (`WITH RECURSIVE`), mit Index auf `(from_file_id, relation_type)` im niedrigen Millisekundenbereich
- Der Content ist zu 95 % relational (Files, Claims, Sources, Quiz) — nur die Kanten sind graphartig
- Zwei Datenbanken zu betreiben und synchron zu halten kostet mehr, als der Graph-Query je einspart

**Regel: Eine Datenbank, bis sie beweisbar nicht mehr reicht.**

### Performance-Entscheidungen

1. **Tier-A-Files werden mit der App gebündelt** (JSON-Snapshot, ~3–5 MB).
   Cold Start zeigt sofort Inhalt, funktioniert offline, spart Requests.
   Delta-Sync beim Start.
2. **Content ist read-heavy und ändert sich selten** → aggressives CDN-Caching,
   `ETag` + `stale-while-revalidate`, Cache-Invalidierung nur beim Publish.
3. **Rabbit-Hole-Pfade werden serverseitig gerechnet**, aber die nächsten
   2 Knoten werden vorgeladen → gefühlt keine Ladezeit beim Abstieg.
4. **XP, Streaks, Calibration ausschließlich serverautoritativ.**
   Client-Werte sind ein Vorschlag, nie die Wahrheit.

### Technische Hauptherausforderungen

| Herausforderung | Lösung |
|---|---|
| Pfadgenerierung ohne Sackgassen/Zyklen | Vorberechnete Reachability pro Startknoten, nächtlicher Job; Fallback-Kante `SHARES_ACTOR` als Notausgang |
| Graph-Qualität skaliert nicht mit Handarbeit | pgvector schlägt Kanten vor, Redaktion bestätigt und typisiert. Nie automatisch publizieren. |
| Obscurity-Score-Drift bei wachsendem Korpus | Dezil-Bucketing statt absoluter Schwellen; quartalsweise Neuberechnung |
| Quiz-Fragen erschöpfen sich | Pool-Rotation + Pflicht: 5 Fragen je Tier-A-File beim Publish |
| Content-Freshness vs. Cache | `content_version` global; Client vergleicht beim Start, lädt Delta |
| Redaktions-Workflow ist das Nadelöhr | CMS mit Review-Queue **vor** dem ersten App-Screen bauen. Das Content-Tooling *ist* die Infrastruktur. |

---

## 18. CONTENT-STRATEGIE

### Die unbequeme Rechnung

Ein sauber recherchiertes, mehrfach belegtes File kostet eine kompetente
Autorin **2–6 Stunden**. 10.000 Files = **über 30.000 Arbeitsstunden**.
Bei 50.000 Files das Fünffache. Dein §34 (50.000 Einträge) und dein §35
(keine KI-Slop, keine erfundenen Quellen) stehen in direktem Widerspruch —
es sei denn, man staffelt die Tiefe.

### Lösung: drei Content-Tiers

| Tier | Umfang | Aufwand/Stück | Launch | Jahr 1 |
|---|---|---|---|---|
| **A — FULL FILE** | Alle Abschnitte, Claim-Breakdown, 8–15 Quellen, 5+ Kanten, 5 Quizfragen | 4–6 h | 150 | 600 |
| **B — FILE** | Claim, Origin, Story kurz, Status, 3–5 Quellen, 3 Kanten | 1,5–2 h | 150 | 900 |
| **C — INDEX ENTRY** | 1 Absatz, Status, 1–3 Quellen, 1–2 Kanten | 20–30 min | 700 | 4.000 |

**Tier C wird in der UI klar als `INDEX ENTRY` gekennzeichnet.** Es wird nicht
so getan, als sei es eine volle Akte. Genau diese Einträge liefern das
"Ich wusste nicht, dass es das gibt"-Gefühl und die Rabbit-Hole-Tiefe —
ehrlich und bezahlbar.

**Launch-Ziel: ~1.000 Einträge.** Das reicht für 20–30 Level tiefe Runs,
600+ Quizfragen und ein Archiv, das sich groß anfühlt. 10.000 leere Einträge
fühlen sich kleiner an als 1.000 gute.

### Produktionspipeline

```
1. SCOPE       Redaktion wählt Thema, prüft Duplikat
2. SOURCE      Quellen ZUERST sammeln (Primärdokumente, Archive, Fachliteratur,
               Untersuchungsberichte, Gerichtsakten, Peer-Review)
3. DRAFT       KI-Unterstützung erlaubt — aber ausschließlich als Zusammenfassung
               DES BEREITGESTELLTEN QUELLENSETS. Niemals aus dem Modellgedächtnis.
4. CLAIM SPLIT Behauptungen in einzelne, prüfbare Claims zerlegen
5. STATUS      Jeder Claim bekommt Status + schriftliche Begründung
6. VERIFY      Zweite Person prüft JEDEN Faktensatz gegen die Quellenzeile
7. HARM REVIEW Harm-Tier bestimmen; ab Tier 2 Vier-Augen-Prinzip, ab Tier 3 Rechtsprüfung
8. LINK        Kanten setzen und typisieren; DOCUMENTED_BASIS suchen
9. QUIZ        Fragen erzeugen — nur aus verifizierten Sätzen
10. PUBLISH    Publish-Gate blockiert bei fehlendem Quell-Identifier
11. REVIEW     Jährliche Wiedervorlage; sofort bei neuer Faktenlage
```

### Harte Publish-Gates (technisch erzwungen)

- ❌ Kein Publish ohne mindestens 3 Quellen mit auflösbarem Identifier
- ❌ Kein Publish ohne genau einen `is_core`-Claim mit Status **und** Begründung
- ❌ Kein Publish ohne mindestens 2 typisierte Kanten
- ❌ Kein Publish mit Status `DEBUNKED` ohne mindestens eine Quelle, die die Widerlegung trägt
- ❌ Kein Publish von Harm-Tier ≥ 2 ohne zweite Freigabe

Details und die vollständige Redaktionsordnung: **[`02-EDITORIAL-POLICY.md`](02-EDITORIAL-POLICY.md)**

---

## 19. GROWTH-STRATEGIE

### 19.1 Die virale Einheit ist NICHT die Punktzahl

Niemanden interessiert dein XP-Stand. Drei Share-Formate, nach erwarteter
Wirkung sortiert:

**1. THE PATH** *(stärkstes Format)*
```
I went 14 levels deep.
MOON LANDING HOAX → … → PROJECT SUNSHINE
Where does yours end?
```
Inhärent gesprächsfähig: zwei Menschen mit demselben Start landen woanders.
Fordert zur Nachahmung auf und trägt echten Content nach außen.

**2. THE CALIBRATION CHALLENGE**
```
"The CIA tested LSD on unwitting Americans for 20 years."
I said 30 %. The evidence says: DOCUMENTED.
My calibration: 81. What's yours?
```
Eine Behauptung, ein Fehlurteil, eine Herausforderung. Funktioniert als
Standbild, als TikTok-Hook, als X-Post.

**3. THE FILE CARD** — eine Akte als Share Card mit Status-Badge

**Pflichtregel für ALLE Share Cards: Der Evidence Status steht immer drauf.**
Nie eine Behauptung ohne ihre Einordnung nach außen geben. Sonst wird die App
zum Zitat-Steinbruch für genau die Verbreitung, die sie einordnen will. Das
ist gleichzeitig Markenschutz und Verantwortung.

### 19.2 Kanäle

| Kanal | Ansatz | Priorität |
|---|---|---|
| **TikTok / Reels / Shorts** | Eigener Kanal, 3–5×/Woche, Format "One documented conspiracy in 40 seconds". Der belegte Content ist das virale Material, nicht der widerlegte. | ★★★★★ |
| **Reddit** | r/UnresolvedMysteries, r/todayilearned, r/declassified. **Wert liefern, nicht spammen** — Files als Quelle teilen, nicht als Werbung. | ★★★★ |
| **ASO** | "conspiracy", "mystery", "unexplained", "quiz", "declassified". Screenshots müssen die Evidence-Chips zeigen — das ist das Differenzierungsmerkmal im Store-Regal. | ★★★★ |
| **SEO (ab V3 Web)** | File-Seiten sind hervorragender Longtail-SEO-Content. "was ist Project Blue Beam" hat konstantes Suchvolumen. Langfristig größter Kanal. | ★★★★ |
| **Presse / Feature** | Der Calibration-Angle ist die Story: *"Die App, die dir zeigt, wie gut du Fakten von Fiktion trennst."* Das öffnet Tech-Presse und Apple-Feature-Türen — die reine Conspiracy-Story nicht. | ★★★ |
| **Podcasts** | Sponsoring in True-Crime-/History-Podcasts, sehr passende Zielgruppe | ★★★ |
| **Paid** | Erst nach nachgewiesener D30-Retention > 15 %. Vorher verbrennt es Geld. | ★ |

### 19.3 North Star Metric

> **WAU, die ≥ 3 Daily Files pro Woche abschließen**

Erfasst Gewohnheit *und* Kernnutzen in einer Zahl. Nicht Downloads
(Vanity), nicht DAU (sagt nichts über Wert), nicht XP (misst nur Zeit).

**Supporting Metrics**

| Metrik | Zielwert V1 |
|---|---|
| D1 Retention | 40 % |
| D7 Retention | 20 % |
| D30 Retention | 10 % |
| Daily-File-Completion (der Aktiven) | 60 % |
| Ø Rabbit-Hole-Tiefe pro Run | 7+ |
| Run-Completion-Rate | 45 % |
| Share-Rate pro abgeschlossenem Run | 8 % |
| Abo-Konversion | 2–4 % |
| **Calibration-Verbesserung über 30 Tage** | **+8 Punkte** ← der Beweis, dass das Produkt wirkt |

Die letzte Metrik ist die wichtigste für die Markenerzählung. Wenn sich die
Kalibrierung nachweislich verbessert, hat man kein Unterhaltungsprodukt mehr,
sondern ein Bildungsprodukt mit Unterhaltungsmechanik. Das verändert Presse,
Preissetzung, Store-Kategorie und B2B-Potenzial.

---

## 20. RISIKEN UND MÖGLICHE PROBLEME

Nach *Schwere × Wahrscheinlichkeit* sortiert.

### 🔴 R1 — App-Store-Ablehnung / Plattform-Policy
**Wahrscheinlichkeit: hoch. Schwere: existenziell.**
Apple (Guidelines 1.1 objectionable content, 1.2 UGC) und Google Play
(Misrepresentation Policy) prüfen Apps, die Fehlinformation *thematisieren*,
streng. Eine App namens "Conspiracy Files" mit dem Claim "Enter the rabbit hole"
kann von einem Reviewer in 30 Sekunden als Verbreitungsplattform gelesen werden.

**Mitigation:**
- Store-Beschreibung, Screenshot 1 und Subtitle stellen die **Evidenz-Schicht** in den Vordergrund, nicht das Mysterium
- Evidence Status ist auf jedem Screenshot sichtbar
- Kein UGC in V1 → Regel 1.2 entfällt vollständig
- Altersfreigabe 17+ / Mature, bewusst gesetzt
- Ein Reviewer-Notes-Dokument beilegen, das die redaktionelle Methodik erklärt
- Interne Beispiel-Files für Review vorbereiten, die die Debunking-Qualität zeigen

### 🔴 R2 — Zielgruppen-Fehlpassung (die zentrale Produktspannung)
**Wahrscheinlichkeit: hoch. Schwere: hoch.**
Wer "conspiracy" sucht, will teils Bestätigung — und wird enttäuscht.
Wer Medienkompetenz will, schreckt vor dem Namen zurück. Die App sitzt
zwischen zwei Stühlen.

**Mitigation:** Der First-Run mit einer **belegten** Verschwörung ist die
zentrale Waffe dagegen. Ebenso der Ton: nie spöttisch. Die Botschaft ist
nicht "ihr seid dumm", sondern *"manches davon ist wirklich passiert — lass
uns herausfinden, welches."* Das ist für beide Gruppen anschlussfähig.

### 🔴 R3 — Rechtliche Haftung (Verleumdung, lebende Personen)
**Wahrscheinlichkeit: mittel. Schwere: hoch.**
Pizzagate benennt einen realen Restaurantbesitzer. Zu Sandy Hook gibt es
rechtskräftige Urteile in dreistelliger Millionenhöhe. Eine Akte, die eine
Beschuldigung gegen eine lebende Person auch nur strukturiert wiedergibt,
ist angreifbar.

**Mitigation:**
- Lebende Privatpersonen erscheinen ausschließlich als **Ziel einer widerlegten Behauptung**, nie als Subjekt einer offenen Anschuldigung
- Harm-Tier 3 → Pflicht-Rechtsprüfung vor Publish
- Kein "THE ARGUMENTS"-Abschnitt bei Tier-3-Inhalten (siehe Editorial Policy)
- Klares Notice-and-Takedown-Verfahren, dokumentiert und schnell

### 🟠 R4 — Content-Geschwindigkeit und -Kosten
**Wahrscheinlichkeit: hoch. Schwere: mittel.**
Der kritische Pfad. Ohne Content ist die App leer, mit schlechtem Content
ist sie wertlos.
**Mitigation:** Drei-Tier-System, CMS zuerst bauen, Content-Team vor Dev-Team
starten, Freelance-Pool aus Geschichts-/Journalismus-Absolventen.

### 🟠 R5 — Retention-Klippe nach der Neuheit
**Wahrscheinlichkeit: mittel-hoch. Schwere: hoch.**
Discovery-Produkte haben starke Woche 1 und schwache Woche 4.
**Mitigation:** Genau dafür existieren Daily File, Streak, Calibration
(langfristige Progression) und Collections (Sammelvervollständigung).
Der Deep Loop ist die eigentliche Retention, nicht die Discovery.

### 🟠 R6 — Werbeerlöse enttäuschen (Brand Safety)
**Wahrscheinlichkeit: hoch. Schwere: mittel.**
Siehe §14. **Mitigation:** Von Anfang an abo-getrieben planen. Ads nie im
Finanzmodell als tragende Säule ansetzen.

### 🟡 R7 — Zitat-Missbrauch / Kontextverlust
Screenshots der Claim-Sektion ohne Status kursieren als "Beleg".
**Mitigation:** Status ist im selben visuellen Block wie der Claim, nie
darunter weggescrollt. Share Cards tragen ihn immer. Kein Screen zeigt
je eine Behauptung ohne Einordnung im selben Viewport.

### 🟡 R8 — Graph-Qualität degradiert mit Korpusgröße
Automatisch gesetzte Kanten erzeugen sinnlose Rabbit Holes.
**Mitigation:** Kanten nur redaktionell bestätigt; pgvector schlägt vor,
Menschen entscheiden. Stichproben-Audit von 20 zufälligen Runs pro Monat.

### 🟡 R9 — Team- und Finanzierungsrealität
Ein Produkt mit 1.000 recherchierten Einträgen ist kein Solo-Projekt.
**Mitigation:** Kleiner, scharfer Launch (1.000 Einträge, EN) statt breitem
Versprechen. Erst Retention beweisen, dann skalieren.

### 🟡 R10 — KI-Analyse halluziniert (ab V2)
Ein KI-Feature, das Fakten erfindet, zerstört exakt die Glaubwürdigkeit,
die das Produkt aufbaut.
**Mitigation:** Strikt RAG-gegroundet auf das eigene, verifizierte Korpus.
Keine Antwort ohne Zitat aus einem publizierten File. Bei fehlender Abdeckung:
explizites *"Das Archiv deckt diese Behauptung nicht ab."* Erst ausliefern,
wenn das Korpus dicht genug ist — lieber V2.5 als ein halluzinierendes V2.

---

## 21. NÄCHSTE SCHRITTE

Reihenfolge nach Abhängigkeit, nicht nach Bequemlichkeit:

1. **Editorial Policy final abnehmen** — [`02-EDITORIAL-POLICY.md`](02-EDITORIAL-POLICY.md). Ohne sie ist jeder Content Nacharbeit.
2. **Datenmodell final abnehmen** — [`01-DATA-MODEL.md`](01-DATA-MODEL.md). Schema-Änderungen nach 300 Files sind teuer.
3. **CMS + Review-Queue bauen** (2–3 Wochen). Vor dem ersten App-Screen.
4. **10 Referenz-Files in voller Tiefe schreiben.** Sie definieren den Qualitätsmaßstab für alle folgenden und decken alle 5 Evidence-Status und alle Harm-Tiers ab.
5. **Design-System + 3 Kern-Screens** (Home / File Detail / Rabbit Hole Node) als klickbarer Prototyp.
6. **Rabbit-Hole-Algorithmus gegen die 10 Referenz-Files testen** — funktioniert die Pfadlogik bei winzigem Graph?
7. **Content-Produktion hochfahren**, parallel App-Entwicklung starten.

Dokumentenübersicht:
- [`01-DATA-MODEL.md`](01-DATA-MODEL.md) — Entitäten, Beziehungen, DDL, Scores
- [`02-EDITORIAL-POLICY.md`](02-EDITORIAL-POLICY.md) — Evidenzsystem, Harm-Tiers, Quellenregeln, Publish-Gates
- [`03-MVP-SCOPE.md`](03-MVP-SCOPE.md) — Feature-Priorisierung, Cut-Liste, Roadmap, Metriken

---

*CONSPIRACY FILES — Enter the rabbit hole.*
