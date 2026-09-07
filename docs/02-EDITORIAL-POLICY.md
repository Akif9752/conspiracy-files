# CONSPIRACY FILES — REDAKTIONSORDNUNG

**Verbindlich für alle Inhalte.** Diese Ordnung geht im Konfliktfall jeder
Design-, Wachstums- oder Umsatzüberlegung vor.

---

## 1. DIE DREI EBENEN

Jede Akte trennt konsequent:

| Ebene | Frage | UI-Abschnitt | Typografie |
|---|---|---|---|
| **1. WAS BEHAUPTET WIRD** | Was sagen Anhänger? | `THE CLAIM` | Serif — fremde Stimme |
| **2. WAS BELEGT IST** | Was lässt sich überprüfen? | `THE EVIDENCE` | Sans + Quellenangabe |
| **3. WAS NICHT BELEGT ODER WIDERLEGT IST** | Was hält der Prüfung nicht stand? | `COUNTERPOINTS` / `ASSESSMENT` | Sans + Quellenangabe |

**Regel:** Ebene 1 erscheint nie ohne sichtbaren Evidence Status **im selben
Viewport**. Nicht darunter, nicht nach dem Scrollen — im selben Bild.

Der einzige zulässige Aufschub ist der **Believe It or Not**-Moment, bei dem der
Nutzer bewusst und freiwillig zuerst schätzt. Dort wird der Status unmittelbar
nach der Abgabe eingeblendet, ohne Umweg, ohne Paywall, ohne Werbung.

---

## 2. EVIDENCE STATUS — DEFINITIONEN

Fünf Status. Vergeben wird immer **pro Claim**, nie pro Thema.

### 🟢 DOCUMENTED
Die Behauptung wird durch Primärquellen, freigegebene Akten, amtliche
Untersuchungsberichte, Gerichtsentscheidungen oder begutachtete Forschung
belegt. Fachlicher Konsens oder unstrittige Dokumentenlage.
> *MKULTRA: Die CIA führte 1953–1973 Experimente mit LSD an teils nichtsahnenden Personen durch — belegt durch Church-Committee-Berichte und freigegebene Akten.*

### 🔵 PARTLY DOCUMENTED
Belegte Kernelemente, unbelegte Erweiterung. **Der häufigste ehrliche Status.**
Die Begründung muss explizit sagen, *welcher Teil* belegt ist und welcher nicht.
> *Operation Northwoods: Der Plan existierte und ist freigegeben. Dass er ausgeführt wurde, ist unbelegt — er wurde von Kennedy abgelehnt.*

### 🟠 CONTESTED
Fachlich ernsthaft umstritten, mit belastbaren Argumenten auf mehreren Seiten,
ohne Konsens. **Kein Feigenblatt für "wir wissen es nicht":** Wenn eine Seite
klar überwiegt, ist es nicht `contested`, sondern `partly_documented` oder `debunked`.
Reserviert für echte offene Fragen.

### 🟡 UNVERIFIED
Nicht ausreichend belegt. Weder tragfähig gestützt noch überzeugend widerlegt.
Zusatzlabel `no evidentiary basis`, wenn keinerlei überprüfbare Grundlage existiert.

### 🔴 DEBUNKED
Die zentrale Behauptung wurde überzeugend widerlegt. **Erfordert zwingend
mindestens einen `undermines`-Beleg mit Quelle.** "Es klingt unplausibel" ist
kein Debunk.

### Verbotene Praktiken

- ❌ Einen Status vergeben, um Ausgewogenheit vorzutäuschen
- ❌ `contested` verwenden, wenn tatsächlich Konsens besteht (*false balance*)
- ❌ `debunked` verwenden ohne belegte Widerlegung
- ❌ Einen Status auf ein ganzes Thema anwenden statt auf eine Behauptung
- ❌ Komplexe Faktenlagen glattbügeln, damit ein Badge passt

Wenn die Faktenlage nicht sauber in einen Status passt, ist das
`confidence_note`-Feld zu nutzen — nicht der Status zu verbiegen.

---

## 3. HARM TIERS

Nicht jede Theorie ist gleich unschädlich. Manche Inhalte richten realen
Schaden an, wenn man sie neutral und überzeugend darstellt. Das Harm Tier
bestimmt, **wie** eine Akte aufgebaut wird.

### Tier 0 — Unbedenklich
Historisch, spekulativ, ohne benannte lebende Betroffene und ohne Anschluss
an Hassnarrative.
*Beispiele: Bermudadreieck, Nazca-Linien, Dyatlov-Pass.*
→ Standardaufbau. Alle Abschnitte, inklusive `THE ARGUMENTS`.

### Tier 1 — Erhöhte Sorgfalt
Politisch aufgeladen, aber ohne direkte Schädigungswirkung.
*Beispiele: Mondlandung, Area 51, Bilderberg.*
→ Standardaufbau. `ASSESSMENT` ist Pflichtfeld, nicht optional.

### Tier 2 — Umgekehrter Aufbau
Gesundheitsfehlinformation, Krisen-/Katastrophenleugnung, Inhalte mit
belegter realer Schadenswirkung.
*Beispiele: Impfstoff-Autismus, AIDS-Leugnung, Chemtrails, 5G-Gesundheitsclaims.*

**Aufbau wird invertiert:**
```
1. CONTEXT & CONSEQUENCES   ← was diese Behauptung real angerichtet hat
2. THE CLAIM (zusammengefasst, NICHT ausgebaut)
3. THE EVIDENCE
4. WHY IT SPREAD            ← ersetzt "THE ARGUMENTS"
5. ASSESSMENT
```
→ **Kein `THE ARGUMENTS`-Abschnitt.** Die Argumente der Anhänger werden
*beschrieben und eingeordnet*, nicht in ihrer überzeugendsten Form nachgebaut.
Der Unterschied zwischen Erklären und Weiterverbreiten liegt genau hier.
→ Zwei-Augen-Freigabe zwingend.

### Tier 3 — Höchste Restriktion
Hassnarrative und Inhalte gegen benannte lebende Personen.
*Beispiele: antisemitische Tropen (Protokolle der Weisen von Zion,
Rothschild-Narrative, "Great Replacement"), Pizzagate, Sandy-Hook-"Crisis Actors".*

**Zusätzlich zu allen Tier-2-Regeln:**
- Die Akte behandelt die Theorie **als Phänomen und als Schadensfall**, nicht als offene Frage
- Verpflichtender Abschnitt `THE PATTERN` — welches ältere Hassnarrativ hier neu verpackt wird. Antisemitische Verschwörungserzählungen sind Neuauflagen mittelalterlicher Blutlegenden; das gehört in die Akte.
- **Lebende Privatpersonen ausschließlich als `target_of_claim`.** Niemals als mutmaßliche Täter. Technisch im Datenmodell erzwungen.
- Verpflichtender Abschnitt `THE REAL COST` — dokumentierte Folgen (Belästigung, Gewalt, Gerichtsurteile)
- **Rechtsprüfung vor Publish**
- Nicht als `daily_file` zulässig
- Nicht als Rabbit-Hole-Endknoten zulässig — der Pfad endet nie auf einem Tier-3-Inhalt
- **Keine Share Card.** Diese Akten sind nicht teilbar.

### Was gar nicht ins Archiv kommt

- Anleitungen zu Schädigung jeglicher Art
- Aktive Aufforderungen gegen Personen oder Gruppen
- Theorien über nicht-öffentliche Privatpersonen ohne öffentliches Interesse
- Laufende, nicht abgeschlossene Ermittlungen gegen benannte Personen
- Neue, ungeprüfte Behauptungen ohne dokumentierte Verbreitung — das Archiv ist kein Erstverbreiter. **Ein Eintrag entsteht, weil eine Behauptung nachweislich kursiert, nie weil sie interessant klingt.**

---

## 4. QUELLENREGELN

### Mindestanforderungen

| Tier | Quellen | davon `reliability_tier` 1 |
|---|---|---|
| A — Full File | ≥ 8 | ≥ 3 |
| B — File | ≥ 3 | ≥ 1 |
| C — Index Entry | ≥ 1 | ≥ 1 |

### Harte Regeln

1. **Jede Quelle braucht einen auflösbaren Identifier** (URL, DOI, ISBN, Archiv-Signatur). Technisch per `CHECK`-Constraint erzwungen.
2. **Jeder Faktensatz wird gegen die Quellenzeile geprüft** — von einer zweiten Person, nicht der Autorin.
3. **Keine Quelle aus dem Modellgedächtnis.** KI darf ein *bereitgestelltes* Quellenset zusammenfassen. Sie darf niemals Quellen vorschlagen, die nicht vorher von einem Menschen geöffnet und geprüft wurden. Halluzinierte Zitate sind der häufigste und tödlichste Fehlermodus für ein Evidenz-Produkt.
4. **`primary_claimant`-Quellen belegen nur die Existenz der Behauptung**, nie ihren Inhalt. UI-Label: `SOURCE OF THE CLAIM`.
5. **Tote Links** werden quartalsweise geprüft und auf Archivkopien umgestellt.

### KI-Einsatz — erlaubt und verboten

| ✅ Erlaubt | ❌ Verboten |
|---|---|
| Bereitgestellte Quellen zusammenfassen | Fakten aus dem Modellgedächtnis erzeugen |
| Kanten zwischen Files vorschlagen (Redaktion bestätigt) | Kanten automatisch publizieren |
| Quizfragen aus verifiziertem Text ableiten | Quizfragen aus unverifiziertem Text erzeugen |
| Sprachliche Überarbeitung, Kürzung | Quellenangaben erzeugen oder vervollständigen |
| Duplikate im Korpus finden | Evidence Status vergeben |
| Lücken im Graphen identifizieren | Ohne menschliche Freigabe publizieren |

**Der Evidence Status wird immer von einem Menschen vergeben und schriftlich
begründet.** Das ist die redaktionelle Kernleistung des Produkts und wird
nicht delegiert.

---

## 5. SPRACHREGELN

### Ton

| Statt | Besser |
|---|---|
| "Verschwörungstheoretiker glauben absurderweise …" | "Anhänger der Theorie führen an, dass …" |
| "Das ist offensichtlich falsch." | "Die Fotos zeigen [X]; das widerspricht der Behauptung, weil [Y]." |
| "Natürlich stimmt das nicht." | "Dafür gibt es keine belegten Hinweise." |
| "Verrückte behaupten …" | "Die Behauptung tauchte erstmals [wann/wo] auf." |

**Nie über Menschen urteilen. Immer über Behauptungen.**
Das ist nicht nur ethisch richtig, es ist wirkungsvoller: Wer sich verspottet
fühlt, hört auf zu lesen — und genau dann hat die App ihren Zweck verfehlt.

### Präzision

- Keine vagen Mengenangaben ("viele Experten") — konkrete Zahlen und Namen
- Passiv vermeiden, wo es Verantwortung verschleiert
- Datumsangaben immer vollständig
- Konjunktiv konsequent bei Behauptungen, Indikativ nur bei Belegtem
- Amerikanisches Englisch als Basissprache

### Der Hook (`file.summary`)

1–2 Sätze. Muss **eine konkrete, belegte, überraschende Tatsache** enthalten —
nicht eine Zusammenfassung der Theorie. Der Hook trägt die Node Card im
Rabbit Hole und entscheidet über Weiterlesen oder Abbruch.

> ❌ *"Manche glauben, die Regierung habe Gedankenkontrolle erforscht."*
> ✅ *"Zwischen 1953 und 1973 gab die CIA über 80 Institutionen Geld für Experimente mit LSD an teils nichtsahnenden Bürgern. Der Direktor ließ 1973 fast alle Akten vernichten."*

---

## 6. REVIEW-ZYKLUS

| Auslöser | Frist |
|---|---|
| Neue Primärquelle / Freigabe von Akten | sofort |
| Gerichtsentscheidung mit Bezug | sofort |
| Nutzer-Korrekturmeldung | 14 Tage |
| Turnusmäßige Prüfung Tier A | jährlich |
| Turnusmäßige Prüfung Tier B/C | alle 2 Jahre |
| Link-Rot-Prüfung | quartalsweise |

Jede Statusänderung an einer publizierten Akte:
- erzeugt Eintrag in `status_change_log` **mit Begründung**
- wird in der UI sichtbar gemacht: `ASSESSMENT UPDATED · 12 MAR 2027`
- alte Fassung bleibt in `file_revision` einsehbar

**Sichtbare Korrekturen sind ein Feature, kein Eingeständnis.** Ein Archiv,
das seine eigenen Änderungen offenlegt, ist glaubwürdiger als eines, das
stillschweigend umschreibt. Das ist ein echtes Differenzierungsmerkmal
gegenüber jeder Content-Farm.

---

## 7. DIE ZEHN GEBOTE (Kurzfassung für Autor:innen)

1. Trenne immer, **was behauptet wird**, von **dem, was belegt ist**.
2. Jeder Status braucht eine schriftliche Begründung.
3. Keine Quelle ohne auflösbaren Identifier.
4. Kein Faktensatz ohne Zweitprüfung.
5. Erfinde nichts — keine Theorie, keine Quelle, kein Ereignis, kein Zitat.
6. Verspotte keine Menschen. Prüfe Behauptungen.
7. Bei Tier 2/3: erklären, nicht nachbauen.
8. Bei Unsicherheit: die Unsicherheit **benennen**, nicht auflösen.
9. Der Hook ist eine belegte Tatsache, kein Teaser.
10. Im Zweifel: nicht publizieren.
