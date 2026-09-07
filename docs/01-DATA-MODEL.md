# CONSPIRACY FILES — DATENMODELL

**Zweck:** Verbindliche Spezifikation der Content- und User-Datenstruktur.
**Datenbank:** PostgreSQL 15+ (mit `pgvector`, `pg_trgm`)
**Status:** Entwurf zur Abnahme — Änderungen nach Beginn der Content-Produktion sind teuer.

---

## 1. LEITENTSCHEIDUNGEN

| # | Entscheidung | Konsequenz |
|---|---|---|
| 1 | **`claim` ist eine eigene Tabelle** mit eigenem Evidence Status | Ein File kann belegte *und* widerlegte Teile haben. Der File-Status ist nur der Rollup des `is_core`-Claims. |
| 2 | **`entity` ist normalisiert** (Person, Org, Ort, Event, Projekt) | "CIA" ist eine Zeile. Ermöglicht Entity-Suche, Entity-Seiten und Graph-Kanten über gemeinsame Akteure. |
| 3 | **`file_link` trägt Typ + Begründung + Gewicht** | Rabbit Hole ist kuratiert, nicht zufällig. Die Kante erklärt sich dem Nutzer selbst. |
| 4 | **`source` braucht einen auflösbaren Identifier** | Strukturelle Absicherung gegen erfundene Quellen. Publish-Gate erzwingt es. |
| 5 | **Alles Redaktionelle ist versioniert** (`file_revision`) | Nachvollziehbarkeit, Rollback, Audit — bei einem Evidenz-Produkt nicht optional. |

---

## 2. ÜBERBLICK — ENTITY RELATIONSHIP

```
                    ┌──────────────┐
                    │   category   │
                    └──────┬───────┘
                           │ n:m
                    ┌──────▼───────┐        ┌────────────┐
        n:m ────────┤     file     ├────────┤    tag     │
     ┌──────────────┤  (die Akte)  │  n:m   └────────────┘
     │              └──┬────────┬──┘
     │                 │ 1:n    │ 1:n
┌────▼─────┐    ┌──────▼─────┐  │      ┌──────────────────┐
│  entity  │    │   claim    │  └─────►│   file_link      │
│ person   │    │            │         │  typisierte      │
│ org      │    │ evidence_  │         │  Kante file↔file │
│ place    │    │ status     │         └──────────────────┘
│ event    │    └──────┬─────┘
│ project  │           │ 1:n
└────┬─────┘    ┌──────▼──────────┐
     │          │  evidence_item  │
     │ n:m      │  stance:        │
     │          │  supports /     │
     │          │  undermines /   │
     │          │  context        │
     │          └──────┬──────────┘
     │                 │ n:1
     │          ┌──────▼──────┐
     └─────────►│   source    │
                └─────────────┘

     ┌──────────────┐      ┌───────────────┐
     │ quiz_question├─────►│  file / claim │
     └──────────────┘      └───────────────┘

USER-SEITE
     app_user ──┬── user_file_state   (seen / read / bookmarked)
                ├── user_prediction   (Calibration)
                ├── user_quiz_answer
                ├── rabbit_run ── rabbit_run_step
                ├── user_achievement
                └── user_streak
```

---

## 3. CONTENT-SCHEMA (DDL-Entwurf)

### 3.1 Enums

```sql
CREATE TYPE evidence_status AS ENUM (
  'documented',          -- 🟢 belegt
  'partly_documented',   -- 🔵 teilweise belegt
  'contested',           -- 🟠 fachlich umstritten
  'unverified',          -- 🟡 nicht belegt
  'debunked'             -- 🔴 widerlegt
);

CREATE TYPE content_tier AS ENUM ('a_full', 'b_file', 'c_index');

CREATE TYPE editorial_state AS ENUM (
  'draft', 'in_review', 'fact_check', 'legal_review', 'published', 'retired'
);

CREATE TYPE entity_kind AS ENUM (
  'person', 'organization', 'place', 'event', 'project', 'publication'
);

CREATE TYPE link_relation AS ENUM (
  'spawned',           -- A brachte B hervor
  'precursor_of',      -- A ging B voraus
  'shares_actor',      -- gemeinsame Person/Organisation
  'shares_event',      -- gemeinsames Ereignis
  'escalates',         -- radikalere Version derselben Behauptung
  'contradicts',       -- schließen sich gegenseitig aus
  'rebutted_by',       -- verweist auf die Widerlegung
  'documented_basis'   -- der reale, belegte Kern darunter  ← wichtigster Typ
);

CREATE TYPE evidence_stance AS ENUM ('supports', 'undermines', 'context');

CREATE TYPE source_kind AS ENUM (
  'primary_document',      -- Originaldokument
  'declassified_record',   -- freigegebene Regierungsakte
  'court_record',          -- Gerichtsakte / Urteil
  'official_inquiry',      -- Untersuchungsbericht (Warren, Church, Rogers …)
  'peer_reviewed',         -- begutachtete Fachpublikation
  'investigative_journalism',
  'book_nonfiction',
  'reference_work',        -- Enzyklopädie, Fachlexikon
  'contemporary_press',    -- zeitgenössische Berichterstattung
  'primary_claimant'       -- Quelle DER Theorie selbst (z. B. Originalvideo)
);
```

`primary_claimant` ist wichtig: Man muss belegen können, *wer die Behauptung
wann aufgestellt hat*, ohne diese Quelle als Beleg für ihren Inhalt zu werten.
Die UI kennzeichnet sie als `SOURCE OF THE CLAIM`, nicht als Evidenz.

### 3.2 `file` — die Akte

```sql
CREATE TABLE file (
  id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_number         integer UNIQUE NOT NULL,      -- FILE #00421, stabil, nie wiederverwendet
  slug                text UNIQUE NOT NULL,
  title               text NOT NULL,
  subtitle            text,

  tier                content_tier NOT NULL,
  editorial_state     editorial_state NOT NULL DEFAULT 'draft',

  -- Narrative Abschnitte (Tier C füllt nur summary + origin_note)
  summary             text NOT NULL,               -- der Hook: 1–2 Sätze, belegt & konkret
  origin_note         text,                        -- wann/wo/in welchem Kontext entstanden
  story               text,                        -- Entwicklung der Theorie
  assessment          text,                        -- redaktionelle Gesamteinschätzung
  current_status_note text,                        -- wie wird sie heute eingeordnet

  -- Verortung
  origin_year         integer,
  period_start        integer,
  period_end          integer,
  region_code         text,                        -- ISO 3166-1 alpha-2 oder 'GLOBAL'

  -- Scores
  obscurity_score     smallint CHECK (obscurity_score BETWEEN 1 AND 10),
  obscurity_raw       numeric(5,4),
  popularity_score    numeric(6,3) DEFAULT 0,      -- intern, nicht in der UI als Skala

  -- Sicherheit / Redaktion
  harm_tier           smallint NOT NULL DEFAULT 0 CHECK (harm_tier BETWEEN 0 AND 3),
  harm_note           text,
  requires_legal_ok   boolean NOT NULL DEFAULT false,

  -- Betrieb
  content_version     integer NOT NULL DEFAULT 1,
  published_at        timestamptz,
  last_reviewed_at    timestamptz,
  next_review_due     date,
  created_at          timestamptz NOT NULL DEFAULT now(),
  updated_at          timestamptz NOT NULL DEFAULT now(),

  search_vector       tsvector,
  embedding           vector(1536)                 -- pgvector: nur für Redaktionsvorschläge
);

CREATE INDEX file_search_idx      ON file USING gin(search_vector);
CREATE INDEX file_obscurity_idx   ON file (obscurity_score) WHERE editorial_state = 'published';
CREATE INDEX file_published_idx   ON file (published_at DESC) WHERE editorial_state = 'published';
CREATE INDEX file_embedding_idx   ON file USING hnsw (embedding vector_cosine_ops);
```

**Kein `evidence_status` auf `file`.** Der angezeigte Status ist immer der des
`is_core`-Claims — abgefragt über einen View:

```sql
CREATE VIEW file_public AS
SELECT f.*, c.evidence_status AS core_status, c.statement AS core_claim
FROM file f
LEFT JOIN claim c ON c.file_id = f.id AND c.is_core = true
WHERE f.editorial_state = 'published';
```

Damit ist es **strukturell unmöglich**, ein Thema pauschal zu labeln, ohne zu
sagen, *welche Behauptung* gemeint ist.

### 3.3 `claim` — die einzelne Behauptung

```sql
CREATE TABLE claim (
  id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_id          uuid NOT NULL REFERENCES file(id) ON DELETE CASCADE,
  ordinal          smallint NOT NULL,
  is_core          boolean NOT NULL DEFAULT false,

  statement        text NOT NULL,            -- wörtlich, was behauptet wird
  claimed_by       text,                     -- wer stellt sie auf
  first_claimed_at date,

  evidence_status  evidence_status NOT NULL,
  status_rationale text NOT NULL,            -- PFLICHT: warum dieser Status
  no_evidentiary_basis boolean DEFAULT false,-- Zusatzlabel bei 'unverified'
  confidence_note  text,                     -- wenn die Faktenlage komplex ist

  created_at       timestamptz NOT NULL DEFAULT now(),
  updated_at       timestamptz NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX claim_one_core_per_file
  ON claim (file_id) WHERE is_core = true;
```

Der partielle Unique-Index erzwingt: **genau ein Kern-Claim pro File.**

### 3.4 `evidence_item` — Beleg an einem Claim

```sql
CREATE TABLE evidence_item (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  claim_id    uuid NOT NULL REFERENCES claim(id) ON DELETE CASCADE,
  source_id   uuid NOT NULL REFERENCES source(id),
  stance      evidence_stance NOT NULL,
  ordinal     smallint NOT NULL,
  statement   text NOT NULL,          -- was dieser Beleg konkret zeigt
  locator     text,                   -- Seite, Absatz, Timecode, Aktenzeichen
  created_at  timestamptz NOT NULL DEFAULT now()
);
```

`stance` erzeugt die UI-Abschnitte automatisch:
`supports` → **THE EVIDENCE** · `undermines` → **COUNTERPOINTS** · `context` → **CONTEXT**.
Keine getrennten Freitextfelder, keine Inkonsistenz zwischen Text und Quellen.

### 3.5 `source`

```sql
CREATE TABLE source (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  kind          source_kind NOT NULL,
  title         text NOT NULL,
  author        text,
  publisher     text,
  published_on  date,

  -- MINDESTENS EINER MUSS GESETZT SEIN (Publish-Gate)
  url           text,
  doi           text,
  isbn          text,
  archive_ref   text,          -- z. B. "NARA RG 263, Box 12"

  reliability_tier smallint CHECK (reliability_tier BETWEEN 1 AND 3),
  access_note   text,          -- Paywall, nur Archiv vor Ort, etc.
  retrieved_at  date,
  created_at    timestamptz NOT NULL DEFAULT now(),

  CONSTRAINT source_needs_identifier CHECK (
    url IS NOT NULL OR doi IS NOT NULL OR isbn IS NOT NULL OR archive_ref IS NOT NULL
  )
);
```

Der `CHECK`-Constraint ist die **technische Umsetzung von §35 ("keine erfundenen
Quellen")**. Eine Quelle ohne auflösbaren Identifier kann nicht gespeichert werden.

`reliability_tier`: 1 = Primärdokument / begutachtet / amtlicher Untersuchungsbericht,
2 = etablierter investigativer Journalismus / Fachbuch, 3 = zeitgenössische Presse /
Sekundärdarstellung / Quelle der Behauptung selbst.

### 3.6 `entity` und Verknüpfung

```sql
CREATE TABLE entity (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  kind          entity_kind NOT NULL,
  name          text NOT NULL,
  slug          text UNIQUE NOT NULL,
  aka           text[],                    -- Aliase für die Suche
  description   text,
  birth_year    integer,
  death_year    integer,
  is_living_private_person boolean NOT NULL DEFAULT false,  -- ← Rechts-Flag
  wikidata_id   text,
  created_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE file_entity (
  file_id   uuid NOT NULL REFERENCES file(id) ON DELETE CASCADE,
  entity_id uuid NOT NULL REFERENCES entity(id) ON DELETE CASCADE,
  role      text NOT NULL,        -- 'alleged_actor' | 'documented_actor' |
                                  -- 'target_of_claim' | 'investigator' | 'source_of_claim'
  PRIMARY KEY (file_id, entity_id)
);
```

`role` ist entscheidend für Recht und Redaktion: Der Unterschied zwischen
*"X hat laut Theorie Y getan"* (`alleged_actor`) und *"X wurde durch eine widerlegte
Theorie beschuldigt"* (`target_of_claim`) ist der Unterschied zwischen
Berichterstattung und Verleumdung. `is_living_private_person = true` in Kombination
mit `alleged_actor` löst automatisch `harm_tier = 3` und Rechtsprüfung aus.

### 3.7 `file_link` — die Kante

```sql
CREATE TABLE file_link (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  from_file_id  uuid NOT NULL REFERENCES file(id) ON DELETE CASCADE,
  to_file_id    uuid NOT NULL REFERENCES file(id) ON DELETE CASCADE,
  relation      link_relation NOT NULL,
  rationale     text NOT NULL,        -- eine Zeile, wird dem Nutzer angezeigt
  strength      smallint NOT NULL DEFAULT 5 CHECK (strength BETWEEN 1 AND 10),
  approved_by   uuid REFERENCES editor(id),   -- keine Auto-Publikation
  created_at    timestamptz NOT NULL DEFAULT now(),

  CHECK (from_file_id <> to_file_id),
  UNIQUE (from_file_id, to_file_id, relation)
);

CREATE INDEX file_link_traverse_idx ON file_link (from_file_id, relation, strength DESC);
```

`rationale` wird im Rabbit Hole wörtlich als Wegbeschriftung genutzt:
> `→ THE DOCUMENTED CORE — Project Blue Book war die reale Untersuchung, auf die sich Majestic 12 beruft.`

### 3.8 Quiz

```sql
CREATE TABLE quiz_question (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_id       uuid NOT NULL REFERENCES file(id) ON DELETE CASCADE,
  claim_id      uuid REFERENCES claim(id) ON DELETE SET NULL,
  format        text NOT NULL,          -- 'single_choice' | 'documented_or_debunked'
  prompt        text NOT NULL,
  explanation   text NOT NULL,          -- wird nach der Antwort gezeigt
  source_id     uuid NOT NULL REFERENCES source(id),   -- PFLICHT: Beleg der Antwort
  difficulty    smallint NOT NULL CHECK (difficulty BETWEEN 1 AND 10),
  active        boolean NOT NULL DEFAULT true,
  created_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE quiz_option (
  id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  question_id  uuid NOT NULL REFERENCES quiz_question(id) ON DELETE CASCADE,
  label        text NOT NULL,
  is_correct   boolean NOT NULL DEFAULT false
);
```

`source_id NOT NULL` ist die technische Garantie, dass die App nichts Unbelegtes
als "richtig" lehrt.

### 3.9 Kuratierung

```sql
CREATE TABLE collection (            -- "Casefiles" in der UI
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  slug        text UNIQUE NOT NULL,
  title       text NOT NULL,
  blurb       text,
  cover_ref   text,
  is_premium  boolean NOT NULL DEFAULT false,
  sort_order  integer NOT NULL DEFAULT 0
);

CREATE TABLE collection_file (
  collection_id uuid REFERENCES collection(id) ON DELETE CASCADE,
  file_id       uuid REFERENCES file(id) ON DELETE CASCADE,
  ordinal       smallint NOT NULL,
  PRIMARY KEY (collection_id, file_id)
);

CREATE TABLE daily_file (
  on_date   date PRIMARY KEY,
  file_id   uuid NOT NULL REFERENCES file(id),
  claim_id  uuid NOT NULL REFERENCES claim(id),   -- welche Behauptung wird geschätzt
  blurb     text
);
```

`daily_file` wird **mindestens 60 Tage im Voraus redaktionell befüllt** — kein
Algorithmus. Das Tagesfile ist das Schaufenster; es wird kuratiert.

---

## 4. USER-SCHEMA

```sql
CREATE TABLE app_user (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  handle          text UNIQUE,
  auth_provider   text,
  country_code    text,
  xp_total        bigint NOT NULL DEFAULT 0,
  level           smallint NOT NULL DEFAULT 1,
  deepest_run     smallint NOT NULL DEFAULT 0,
  calibration     smallint,               -- 0..100, aus letzten 50 Predictions
  is_premium      boolean NOT NULL DEFAULT false,
  created_at      timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE user_file_state (
  user_id     uuid REFERENCES app_user(id) ON DELETE CASCADE,
  file_id     uuid REFERENCES file(id) ON DELETE CASCADE,
  first_seen  timestamptz NOT NULL DEFAULT now(),
  read_at     timestamptz,               -- gesetzt bei >60 % Scroll & >30 s
  bookmarked  boolean NOT NULL DEFAULT false,
  PRIMARY KEY (user_id, file_id)
);

CREATE TABLE user_prediction (          -- Believe It or Not / Calibration
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       uuid NOT NULL REFERENCES app_user(id) ON DELETE CASCADE,
  claim_id      uuid NOT NULL REFERENCES claim(id),
  p_user        numeric(4,3) NOT NULL CHECK (p_user BETWEEN 0 AND 1),
  p_target      numeric(4,3) NOT NULL,   -- Snapshot: Status kann sich später ändern
  brier         numeric(5,4) GENERATED ALWAYS AS (power(p_user - p_target, 2)) STORED,
  in_band       boolean NOT NULL,
  created_at    timestamptz NOT NULL DEFAULT now(),
  UNIQUE (user_id, claim_id)
);

CREATE TABLE rabbit_run (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       uuid NOT NULL REFERENCES app_user(id) ON DELETE CASCADE,
  start_file_id uuid NOT NULL REFERENCES file(id),
  depth         smallint NOT NULL DEFAULT 0,
  max_obscurity smallint,
  completed     boolean NOT NULL DEFAULT false,   -- BOTTOM REACHED
  started_at    timestamptz NOT NULL DEFAULT now(),
  ended_at      timestamptz
);

CREATE TABLE rabbit_run_step (
  run_id     uuid REFERENCES rabbit_run(id) ON DELETE CASCADE,
  step_no    smallint NOT NULL,
  file_id    uuid NOT NULL REFERENCES file(id),
  via        link_relation,          -- über welche Kante kam der Nutzer hierher
  PRIMARY KEY (run_id, step_no)
);
```

`p_target` wird als **Snapshot** gespeichert. Wenn ein Claim später neu bewertet
wird, bleibt die historische Calibration fair — der Nutzer wird nicht rückwirkend
für eine damals korrekte Einschätzung bestraft.

---

## 5. RABBIT-HOLE-PFADABFRAGE

Kandidaten für den nächsten Knoten — eine Query, kein Graph-Framework:

```sql
-- $1 aktueller Knoten, $2 dessen Obscurity, $3 bereits besuchte File-IDs
SELECT f.id, f.file_number, f.title, f.obscurity_score,
       l.relation, l.rationale
FROM file_link l
JOIN file_public f ON f.id = l.to_file_id
WHERE l.from_file_id = $1
  AND f.obscurity_score >= $2 - 1
  AND NOT (f.id = ANY($3))
ORDER BY
  -- documented_basis regelmäßig einstreuen, damit der Run geerdet bleibt
  (l.relation = 'documented_basis') DESC,
  l.strength DESC,
  f.obscurity_score DESC
LIMIT 3;
```

Reachability-Vorberechnung (nächtlicher Job) verhindert Sackgassen:

```sql
CREATE MATERIALIZED VIEW file_reach_depth AS
WITH RECURSIVE walk(root_id, file_id, depth, visited) AS (
  SELECT f.id, f.id, 0, ARRAY[f.id]
  FROM file f WHERE f.editorial_state = 'published'
  UNION ALL
  SELECT w.root_id, l.to_file_id, w.depth + 1, w.visited || l.to_file_id
  FROM walk w
  JOIN file_link l ON l.from_file_id = w.file_id
  WHERE w.depth < 40 AND NOT (l.to_file_id = ANY(w.visited))
)
SELECT root_id, max(depth) AS max_depth, count(DISTINCT file_id) AS reachable
FROM walk GROUP BY root_id;
```

`max_depth` je Startknoten steuert, welche Files als Rabbit-Hole-Einstieg
angeboten werden (nur solche mit `max_depth >= 6`) — und liefert der Redaktion
die Liste unterversorgter Bereiche des Graphen.

**Bei 50.000 Knoten bleibt das Postgres-Territorium.** Keine Graphdatenbank nötig.

---

## 6. SCORE-BERECHNUNG

```sql
-- Nächtlich; externe Signale quartalsweise neu erhoben
UPDATE file f SET
  obscurity_raw =
      0.30 * (1 - s.wiki_band)
    + 0.30 * (1 - s.search_band)
    + 0.20 * (1 - s.media_band)
    + 0.20 * (1 - COALESCE(s.in_app_open_rate, s.search_band))  -- Fallback vor 1000 Opens
FROM file_signal s WHERE s.file_id = f.id;

-- Dezil-Bucketing über das Gesamtkorpus → garantiert volle Skala 1..10
WITH ranked AS (
  SELECT id, ntile(10) OVER (ORDER BY obscurity_raw) AS bucket
  FROM file WHERE editorial_state = 'published'
)
UPDATE file f SET obscurity_score = r.bucket FROM ranked r WHERE r.id = f.id;
```

Dezil-Bucketing statt absoluter Schwellen bedeutet: Der Score ist immer relativ
zum aktuellen Archiv. Wächst das Korpus in die Tiefe, verschieben sich die Grenzen
mit — Level 10 bleibt "das Obskurste, was wir haben", statt zu inflationieren.

---

## 7. PUBLISH-GATES (technisch erzwungen)

Als Constraint-Trigger auf `file.editorial_state = 'published'`:

```
✓ tier = 'a_full'  → ≥ 8 Quellen, ≥ 5 Kanten, ≥ 5 Quizfragen, alle Abschnitte gefüllt
✓ tier = 'b_file'  → ≥ 3 Quellen, ≥ 3 Kanten, ≥ 2 Quizfragen
✓ tier = 'c_index' → ≥ 1 Quelle,  ≥ 1 Kante
✓ genau ein claim.is_core = true
✓ jeder claim hat evidence_status UND status_rationale (nicht leer)
✓ jeder claim mit status='debunked' hat ≥ 1 evidence_item mit stance='undermines'
✓ jede source hat url ODER doi ODER isbn ODER archive_ref
✓ harm_tier ≥ 2 → zweite Freigabe (approved_by ≠ author_id)
✓ harm_tier = 3 → requires_legal_ok = true UND legal_ok_at IS NOT NULL
✓ jede entity mit is_living_private_person=true hat role ≠ 'alleged_actor'
```

Die letzte Regel ist die wichtigste Rechtsschranke: **Eine lebende Privatperson
kann in diesem Datenmodell nicht als mutmaßlicher Täter einer unbelegten
Behauptung gespeichert werden.** Nur als `target_of_claim` — also als jemand,
der von einer Behauptung betroffen ist.

---

## 8. MIGRATIONS-DISZIPLIN

- Jede Schemaänderung als nummerierte, vorwärtsgerichtete Migration
- `file_number` wird **nie** wiederverwendet, auch nach Löschung nicht — die Aktennummer ist eine öffentliche Referenz
- `file_revision` speichert jede publizierte Fassung als JSONB-Snapshot
- Statusänderungen an publizierten Claims erzeugen einen Eintrag in `status_change_log` mit Begründung und werden in der UI als *"Assessment updated · [Datum]"* sichtbar gemacht

Der letzte Punkt ist ein Vertrauens-Feature: Ein Evidenz-Produkt, das seine
eigenen Korrekturen sichtbar macht, ist glaubwürdiger als eines, das
stillschweigend umschreibt.
