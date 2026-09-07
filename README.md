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

1. Editorial Policy abnehmen
2. Datenmodell abnehmen
3. CMS + Review-Queue bauen
4. 10 Referenz-Files in voller Tiefe schreiben
5. Design-System + 3 Kern-Screens als Prototyp
6. Rabbit-Hole-Algorithmus gegen die Referenz-Files testen
7. Content-Produktion hochfahren, App-Entwicklung parallel starten
