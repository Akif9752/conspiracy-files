# TROCKENLAUF — 10 REFERENZ-FILES GEGEN SCHEMA UND ALGORITHMUS

**Datum:** Konzeptphase, vor Produktionsbeginn
**Fixture:** 10 Files, 30 Claims, 28 Quizfragen, 33 Quellen, 8 typisierte Kanten
**Werkzeug:** [`tools/validate.py`](../tools/validate.py) — reproduzierbar mit `python3 tools/validate.py`

Zweck des Laufs: Schema und Rabbit-Hole-Logik gegen echte Inhalte prüfen,
**bevor** 1.000 Einträge nach einer möglicherweise falschen Spezifikation
geschrieben werden. Der Lauf hat sieben Befunde ergeben, davon vier, die
Änderungen an Blueprint oder Datenmodell erzwingen.

---

## ABDECKUNG DES FIXTURES

| Kern-Status | Files |
|---|---|
| DOCUMENTED | #0001 MKULTRA, #0005 Roswell, #0006 Project Mogul |
| PARTLY DOCUMENTED | #0002 Operation Northwoods |
| CONTESTED | #0004 The Kennedy Assassination |
| UNVERIFIED | #0008 Project Blue Beam *(no evidentiary basis)* |
| DEBUNKED | #0003 Moon Landing Hoax, #0007 Majestic 12, #0009 Vaccines and Autism, #0010 Pizzagate |

| Harm Tier | Files |
|---|---|
| 0 | #0005, #0006, #0007 |
| 1 | #0001, #0002, #0003, #0004, #0008 |
| 2 | #0009 Vaccines and Autism *(inverted layout, no THE ARGUMENTS)* |
| 3 | #0010 Pizzagate *(THE PATTERN + THE REAL COST, publish blocked)* |

Alle fünf Evidence-Status und alle vier Harm-Tiers sind belegt. Das war das
Ziel des Sets.

---

## BEFUND F-1 — Das Gate hat zwei echte Fehler in meinem eigenen Text gefunden

Zwei Defekte, die beim Lesen nicht aufgefallen wären:

| Gate | Fund | Behoben |
|---|---|---|
| `G-DEBUNK-PROOF` | #0003, Claim 4 („Schatten laufen nicht parallel") war als `debunked` markiert, hatte aber **nur eine Begründung und keinen Gegenbeleg**. Genau der Fehlertyp, den §2 der Redaktionsordnung verbietet: „Es klingt unplausibel" ist kein Debunk. | ✅ zwei `undermines`-Belege ergänzt |
| `G-HARM-2-LAYOUT` | #0010 Pizzagate fehlte der Pflichtabschnitt `WHY IT SPREAD`. Tier 3 erbt alle Tier-2-Regeln — beim Schreiben übersehen, weil `THE PATTERN` und `THE REAL COST` das Gefühl von Vollständigkeit erzeugen. | ✅ Abschnitt ergänzt |

**Wert des Befunds:** Die Gates sind kein Formalismus. Bei einem Fixture von
10 Dateien, die mit maximaler Sorgfalt geschrieben wurden, haben sie zwei
inhaltliche Verstöße gefunden. Bei 1.000 Dateien von vier Autor:innen ist
das der Unterschied zwischen einem Evidenz-Produkt und einer Content-Farm.

---

## BEFUND F-2 — Files entstehen in Clustern, nicht einzeln ⚠️ ÄNDERT DIE CONTENT-STRATEGIE

Der Graph zerfällt in **drei Komponenten**:

```
Komponente 1:  #0001 #0002 #0003 #0004 #0005 #0006 #0007 #0008   (8 Files)
Komponente 2:  #0009 Vaccines and Autism                          (isoliert)
Komponente 3:  #0010 Pizzagate                                    (isoliert)
```

#0009 und #0010 haben **null Kanten** — nicht aus Nachlässigkeit, sondern
weil ihre echten Nachbarn im Set fehlen. Vaccines gehört in ein Cluster mit
Pharma-, Fluoridierungs- und HIV-Leugnungs-Files. Pizzagate gehört zwingend
neben Satanic Panic, Blood Libel und QAnon — und **darf ohne diese Nachbarn
gar nicht publiziert werden**, weil ein Tier-3-Inhalt ohne seinen historischen
Kontext dem Leser die Behauptung ohne das Muster präsentiert, das sie lesbar macht.

Eine erfundene Kante hätte beide Files formal publizierbar gemacht. Genau das
ist der Fehler, den das Gate verhindern soll.

> **Konsequenz für die Produktionsplanung:**
> Der Redaktionsplan darf **nicht** nach Bekanntheit sortiert abgearbeitet werden
> („die 150 populärsten Theorien"). Er muss **clusterweise** geplant werden:
> 8–15 zusammenhängende Files pro Cluster, gemeinsam recherchiert, gemeinsam
> verkantet, gemeinsam freigegeben. Ein Cluster ist die Produktionseinheit,
> nicht das File.

Das verändert Redaktionsplan, Autorenzuschnitt und Freigabe-Workflow.

---

## BEFUND F-3 — Die Obskuritätsregel blockierte den wichtigsten Kantentyp ⚠️ BLUEPRINT KORRIGIERT

Die ursprüngliche Regel im Blueprint lautete:

```
obscurity(next) >= obscurity(prev) − 1
```

`documented_basis`-Kanten zeigen naturgemäß auf **gut belegte und damit meist
bekanntere** Files. Sie wurden von der eigenen Regel systematisch blockiert —
also genau der Kantentyp, den der Blueprint als „wichtigsten Kantentyp des
Produkts" bezeichnet und alle vier Knoten einstreuen wollte. Die Regel und
die Absicht widersprachen sich.

**Korrigierte Regel (jetzt in Blueprint §10 und Datenmodell §5):**

```
obscurity(next) >= high_water_mark − 1          // HWM statt Vorgängerknoten
Ausnahme: documented_basis-Kanten sind von der Regel befreit
```

Gemessener Effekt über alle 10 Startknoten:

| Startknoten | Tiefe mit Ausnahme | ohne Ausnahme |
|---|---|---|
| #0004 Kennedy | **5** | 4 |
| #0002 Northwoods | **4** | 3 |
| #0003 Moon Landing | **4** | 3 |
| #0005 Roswell | **4** | 3 |
| #0006 Project Mogul | **4** | 2 |
| #0008 Blue Beam | **3** | 2 |
| #0007 Majestic 12 | **2** | 1 |

Die Ausnahme bringt konsistent +1 bis +2 Ebenen — bei einem Graphen dieser
Größe zwischen 25 % und 100 % mehr Tiefe.

---

## BEFUND F-4 — Kanten müssen in beide Richtungen begehbar sein ⚠️ SCHEMA ERWEITERT

Der Beispielpfad läuft über zwei Kanten **rückwärts**:

```
L0  #0004 THE KENNEDY ASSASSINATION      obs 1   hwm 1
L1  #0002 OPERATION NORTHWOODS           obs 5   hwm 5   SHARES AN EVENT
L2  #0008 PROJECT BLUE BEAM              obs 7   hwm 7   WHAT WAS BUILT ON IT   ← rückwärts
L3  #0007 MAJESTIC 12                    obs 6   hwm 7   THESE CANNOT BOTH BE TRUE
L4  #0006 PROJECT MOGUL                  obs 7   hwm 7   THESE CANNOT BOTH BE TRUE
L5  #0005 ROSWELL                        obs 2   hwm 7   WHAT WAS BUILT ON IT   ← rückwärts
    BOTTOM REACHED
```

Ohne Rückwärtstraversierung wäre der Graph fast unbegehbar. Das erfordert
zwei Schema-Ergänzungen:

1. **`file_link.rationale_reverse`** — die Wegbeschriftung aus der Gegenrichtung.
   Die Vorwärts-Begründung ergibt rückwärts gelesen oft keinen Sinn.
2. **Richtungssemantik je Relationstyp** — welches Label in welcher Laufrichtung
   erscheint. Vollständig spezifiziert in
   [`content/reference/links.json`](../content/reference/links.json) unter
   `direction_semantics`:

| Relation | vorwärts | rückwärts |
|---|---|---|
| `spawned` | WHAT IT BECAME | WHERE IT CAME FROM |
| `precursor_of` | WHAT CAME AFTER | WHAT CAME BEFORE |
| `escalates` | IT GOES FURTHER | THE MILDER VERSION |
| `rebutted_by` | THE REBUTTAL | WHAT IT REBUTS |
| `documented_basis` | THE DOCUMENTED CORE | WHAT WAS BUILT ON IT |
| `shares_actor` / `shares_event` / `contradicts` | *symmetrisch* | *symmetrisch* |

---

## BEFUND F-5 — Ein Run kann auf einem sehr bekannten File enden ⚠️ UX-KORREKTUR

Der Pfad oben endet auf **#0005 Roswell mit Obskurität 2/10** — über eine
`documented_basis`-Rückwärtskante. Nach fünf Ebenen Abstieg landet der Nutzer
auf einem der bekanntesten Files des Archivs. Der Bildschirm sagt
`YOU REACHED THE BOTTOM`, und der Nutzer sieht Roswell.

Das ist die logische Folge der Ausnahme aus F-3 und inhaltlich sogar richtig —
der Pfad endet auf dem dokumentierten Boden. Als Belohnung funktioniert es nicht.

**Korrekturen (jetzt in Blueprint §10):**

1. Die Run Summary meldet die **erreichte Höchstobskurität (High-Water Mark)**,
   nicht die des letzten Knotens. Im Beispiel: `DEEPEST OBSCURITY 7/10`, nicht 2.
2. `documented_basis`-Schritte werden in der Pfaddarstellung visuell als
   **ANCHOR** markiert — „hier bist du kurz aufgetaucht" — statt als normaler
   Abstiegsschritt. Sie zählen zur Tiefe, aber nicht zum Obskuritätsverlauf.
3. Der Pfadgenerator bevorzugt bei gleichwertigen Kandidaten einen
   **Nicht-Anchor-Knoten als Endknoten**.

---

## BEFUND F-6 — Bei 10 Files gibt es null qualifizierte Einstiegspunkte

Der Blueprint fordert für Rabbit-Hole-Einstiegspunkte `max_depth ≥ 6`.
Erreicht wird maximal **5** (ab #0004 Kennedy).

```
qualifizierte Einstiegspunkte: 0 / 10
```

Zusätzlich: **#0001 MKULTRA hat Tiefe 0.** Das File wirkt zentral, hat aber nur
eine Kante — zu #0004 Kennedy (Obskurität 1). Unter der Monotonieregel ist
dieser Weg von MKULTRA aus gesperrt. Ein prominentes File wird so zum
Endknoten, nie zum Einstieg.

**Das ist kein Fehler, sondern die Messung.** Einstiegspunkt-Tauglichkeit
hängt an der **Kantendichte**, nicht an der Zahl der Files. Aus dem Fixture
hochgerechnet:

| | Fixture | Launch-Ziel |
|---|---|---|
| Files | 10 | 1.000 |
| Kanten | 8 | **≥ 2.000** |
| Kanten pro File | 0,8 | **≥ 4** (Tier A: ≥ 5) |
| Einstiegspunkte | 0 | ~150 |

Die Blueprint-Zahl „≥ 2.000 typisierte Kanten" ist damit nicht mehr geschätzt,
sondern aus einer Messung abgeleitet. Ein File ohne mindestens vier Kanten ist
für den Rabbit Hole faktisch unsichtbar — es kann geöffnet, aber nicht
durchquert werden.

---

## BEFUND F-7 — Das Quellen-Gate war für Behauptungen ohne Evidenzgrundlage unerfüllbar ⚠️ GATE KORRIGIERT

`G-SRC-MIN` verlangte für Tier A acht zitierte Quellen. Für **#0008 Project
Blue Beam** ist das strukturell unmöglich: Die Behauptung hat keine
Evidenzgrundlage, also gibt es keine Evidenzliteratur zu zitieren. Ein Gate,
das ausgerechnet den am schwächsten belegten Behauptungen die meisten Belege
abverlangt, ist falsch herum gedacht.

**Korrigierte Regel:**

```
Tier A, Kern-Claim mit no_evidentiary_basis = true:
    ≥ 5 Quellen  UND  ≥ 2 Quellen vom Typ primary_claimant
```

Statt Evidenzquellen werden **Herkunftsquellen** verlangt: Wer hat die
Behauptung wann in welcher Form aufgestellt. Bei einer Behauptung ohne
Evidenzgrundlage ist die Provenienz die eigentliche Rechercheleistung.

---

## STAND DER GATES NACH DEN KORREKTUREN

```
publizierbar:   1 / 10        blockiert:  9 / 10
```

Verbleibende Blockaden sind **keine Defekte**, sondern die gemessene Lücke
zwischen Fixture-Tiefe und Produktionstiefe:

| Gate | betroffen | Bedeutung |
|---|---|---|
| `G-SRC-MIN` | 7 Files | Fixture zitiert 3–5 Quellen, Tier A verlangt 8. **Die Sourcing-Arbeit ist rund doppelt so groß wie die Schreibintuition** — der wichtigste Kalkulationsbefund für das Content-Budget. |
| `G-LINK-MIN` | 9 Files | Direkte Folge von F-2 und F-6: Kanten entstehen erst im Cluster. |
| `G-QUIZ-MIN` | 8 Files | 3 statt 5 Fragen je Tier-A-File geschrieben. |
| `G-HARM-3` | #0010 | Rechtsprüfung nicht dokumentiert — korrekt blockiert, siehe F-2. |
| `G-PROVENANCE` | #0008 | Neues Gate aus F-7. |

**#0006 Project Mogul** ist als einziges File publizierbar — ein Tier-B-File
mit niedrigeren Schwellen. Auch das ist eine brauchbare Beobachtung: Tier B
und C sind nicht nur billiger, sie sind auch schneller freigabefähig. Für die
Launch-Mischung spricht das dafür, Cluster mit **einem Tier-A-Anker und
mehreren Tier-B-Satelliten** zu bauen, statt gleichrangige Tier-A-Files zu
häufen.

---

## AUFWANDSKALIBRIERUNG

Aus dem Fixture abgeleitet, für die Budgetplanung:

| Kennzahl | Fixture-Messung | Konsequenz |
|---|---|---|
| Claims je Tier-A-File | 3,4 | Blueprint-Annahme bestätigt |
| Zitierte Quellen je Tier-A-File | 3,9 (nötig: 8) | **Quellenarbeit ≈ 2× unterschätzt** |
| Quizfragen je File | 2,8 (nötig: 5) | Fragenproduktion als eigener Arbeitsschritt einplanen, nicht als Nebenprodukt |
| Kanten je File | 0,8 (nötig: ≥ 4) | Verkantung ist Cluster-Arbeit, kein File-Anhängsel |

Die 4–6 Stunden je Tier-A-File aus dem Blueprint gelten für Recherche und Text.
**Quellen-Zweitprüfung, Verkantung und Quizproduktion kommen obendrauf.**
Realistischer Gesamtansatz: **6–9 Stunden je Tier-A-File**, davon ein Drittel
außerhalb des eigentlichen Schreibens.

---

## GEÄNDERTE DOKUMENTE

| Befund | Änderung |
|---|---|
| F-3 | `00-BLUEPRINT.md` §10, `01-DATA-MODEL.md` §5 — High-Water-Mark-Regel + `documented_basis`-Ausnahme |
| F-4 | `01-DATA-MODEL.md` §3.7 — `rationale_reverse`, bidirektionale Traversierung, Richtungssemantik |
| F-5 | `00-BLUEPRINT.md` §10 — Run Summary meldet HWM; Anchor-Markierung |
| F-7 | `01-DATA-MODEL.md` §7 — `G-SRC-MIN`-Ausnahme + neues Gate `G-PROVENANCE` |
| F-2, F-6 | `00-BLUEPRINT.md` §18, `03-MVP-SCOPE.md` — Cluster-Produktion, Kantendichte-Ziel |

---

## OFFEN

1. **Cluster-Plan schreiben.** Die ersten 12 Cluster à 8–15 Files definieren
   den gesamten Launch-Content. Das ist der nächste Redaktionsschritt.
2. **#0010 Pizzagate freigeben oder zurückstellen** — braucht Satanic Panic,
   Blood Libel und QAnon im selben Cluster plus Rechtsprüfung.
3. **Fixture auf volle Produktionstiefe bringen** (8 Quellen, 5 Fragen, 5 Kanten
   je Tier-A-File), damit es als Qualitätsmaßstab für Autor:innen taugt.
   Aktuell ist es ein Schema-Testfall, noch kein Musterexemplar.
4. **`p_target`-Bänder gegen das Fixture prüfen** — Calibration-Mechanik ist
   in diesem Lauf nicht getestet worden.
