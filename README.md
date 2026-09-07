# CONSPIRACY FILES

> *Enter the rabbit hole.*

Ein evidenzbasiertes, vernetztes Archiv von Verschwörungstheorien — als
Consumer-App gedacht: Wissensdatenbank, Discovery-Erlebnis, Quiz und
Medienkompetenz-Werkzeug in einem.

**Status:** Konzeptphase. Noch kein Anwendungscode — bewusst.
Zuerst steht das Produkt, dann der Build.

---

## Dokumente

| Datei | Inhalt |
|---|---|
| **[docs/00-BLUEPRINT.md](docs/00-BLUEPRINT.md)** | Vollständiges Product Blueprint: Positionierung, USP, Zielgruppe, User Journey, Core Loop, IA, Quiz, Rabbit Hole, Gamification, Branding, UI/UX, Monetarisierung, MVP, Roadmap, technische Architektur, Content-, Growth-Strategie, Risiken |
| **[docs/01-DATA-MODEL.md](docs/01-DATA-MODEL.md)** | Entitäten, Beziehungen, Postgres-DDL, Score-Berechnung, Pfadabfragen, Publish-Gates |
| **[docs/02-EDITORIAL-POLICY.md](docs/02-EDITORIAL-POLICY.md)** | Evidenzsystem, Harm-Tiers, Quellenregeln, KI-Einsatzgrenzen, Sprachregeln |
| **[docs/03-MVP-SCOPE.md](docs/03-MVP-SCOPE.md)** | Feature-Priorisierung, Cut-Liste, Launch-Checkliste, Roadmap, Metriken, offene Entscheidungen |
| **[docs/04-WRITING-STANDARD.md](docs/04-WRITING-STANDARD.md)** | Schreibstandard für Autor:innen: Arbeitsreihenfolge, Claim-Zerlegung, Hooks, Verkantung, Abgabe-Checkliste |
| **[docs/05-DRY-RUN.md](docs/05-DRY-RUN.md)** | Trockenlauf der 10 Referenz-Files gegen Schema und Rabbit-Hole-Logik: sieben Befunde, vier mit Änderungsfolge |

## Referenz-Content

| Pfad | Inhalt |
|---|---|
| [`content/reference/files/`](content/reference/files/) | 10 vollständige Referenz-Files — alle 5 Evidence-Status, alle 4 Harm-Tiers |
| [`content/reference/sources.json`](content/reference/sources.json) | 33 normalisierte Quellen mit auflösbaren Identifiern |
| [`content/reference/links.json`](content/reference/links.json) | 8 typisierte Kanten inkl. Richtungssemantik |
| [`tools/validate.py`](tools/validate.py) | Prüft Publish-Gates und simuliert die Rabbit-Hole-Pfadlogik — `python3 tools/validate.py` |

---

## Die fünf zentralen Empfehlungen

1. **Ein tägliches Ritual statt vier.** `THE DAILY FILE` bündelt Theory of the Day,
   Believe It or Not, Quiz und Streak in eine 3-Minuten-Sequenz.
2. **Calibration Score statt XP als Leitmetrik.** Misst Können statt Zeit,
   ist teilbar, und macht die App messbar zu einem Medienkompetenz-Werkzeug.
3. **Evidence Status pro Behauptung, nicht pro Thema.** Strukturell im
   Datenmodell erzwungen.
4. **Kein Graph im MVP.** Nachbarschaftsansicht + Breadcrumb liefern 90 % des
   Gefühls für 10 % des Aufwands.
5. **Harm-Tier-System.** Nicht jede Theorie darf gleich dargestellt werden —
   das ist gleichzeitig Ethik, Recht und App-Store-Freigabe.

---

## Der Core Loop

```
DISCOVER → PREDICT → READ FILE → CONNECT → RABBIT HOLE
    ↑                                            ↓
LEVEL UP ← XP ← QUIZ ← CALIBRATION ← DEEPER FILE
```

---

## Nächste Schritte

1. ~~Editorial Policy abnehmen~~ → Entwurf steht, Abnahme offen
2. ~~Datenmodell abnehmen~~ → Entwurf steht, im Trockenlauf korrigiert, Abnahme offen
3. ~~10 Referenz-Files schreiben~~ → ✅ 10 Files, 30 Claims, 28 Quizfragen, 33 Quellen
4. ~~Rabbit-Hole-Algorithmus testen~~ → ✅ getestet, zwei Regelfehler gefunden und behoben
5. **Cluster-Plan schreiben** — die ersten 12 Cluster à 8–15 Files definieren den Launch-Content
6. Referenz-Files auf volle Produktionstiefe bringen (8 Quellen, 5 Fragen, 5 Kanten je Tier A)
7. CMS + Review-Queue bauen
8. Design-System + 3 Kern-Screens als Prototyp
9. Content-Produktion hochfahren, App-Entwicklung parallel starten
