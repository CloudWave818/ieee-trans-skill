# Knowledge Paths and Loading Contract

## Portable roots

The router resolves data in this order:

1. Embedded resources distributed with the skill:
   - `../resources/IEEE_TRANS_KNOWLEDGE`
   - `../resources/IEEE_TRANS_EXEMPLARS`
2. Legacy sibling folders next to the skill:
   - `../IEEE_TRANS_KNOWLEDGE`
   - `../IEEE_TRANS_EXEMPLARS`

The source corpus is optional during normal use and is intentionally excluded from the GitHub package because the original PDFs may be copyright protected. Keep any local corpus separately as `../IEEE_TRANS_CORPUS` when source-level adjudication is required.

Fail with `MISSING_INPUT` when neither the portable nor legacy Knowledge/Exemplars pair is present. Never silently substitute a similarly named folder.

## Always inspect first

For a one-figure Mode F request, apply the SKILL.md local exception: inspect the visual-case index and only the rule/profile entries that can change that figure. Do not load all five registry/control documents below merely to satisfy a full-project default.

1. `IEEE_TRANS_KNOWLEDGE/00_META/RULE_REGISTRY.csv` - active 42-rule registry.
2. `IEEE_TRANS_KNOWLEDGE/08_SYNTHESIS/GENERAL_VS_DOMAIN_VS_JOURNAL.md` - load order and authority.
3. `IEEE_TRANS_KNOWLEDGE/08_SYNTHESIS/CONFLICT_RESOLUTION.md` - scope conflicts.
4. `IEEE_TRANS_EXEMPLARS/00_META/EXEMPLAR_REGISTRY.csv` - card metadata.
5. `IEEE_TRANS_EXEMPLARS/00_META/EXEMPLAR_ROUTING.csv` - scoring inputs.

Inspect registries first; do not open every knowledge document or card.

## Task-directed loading

| Task | Additional sources |
|---|---|
| project architecture | `01_GENERAL/`, routed domains, routed journal |
| section writing | matching file in `02_SECTIONS/`, one writing file in `05_WRITING/`, section-routed cards |
| claim/evidence or experiments | `03_EVIDENCE/CLAIM_EVIDENCE_SYSTEM.md`, requested evidence file, routed rules/cards |
| figures/tables | matching files in `04_VISUALS/`, evidence needs, visual-role cards; `references/VISUAL_DESIGN_EVIDENCE.md`; UAV style first from `references/preferred_29/STYLE_PLAYBOOK.md` and selected preferred cards; old `references/visual_cases/` supplements |
| page budget | `01_GENERAL/PAGE_AND_SPACE_BUDGET.md`, paper-type route, journal profile |
| reviewer audit | rule registry, target journal, claim/evidence artifacts, `audits/REVIEWER_AUDIT.md` |

## Memory boundary

Treat user-provided methods, data, figures, experiments, contributions, drafts, and reviewer comments as primary project evidence. Treat the corpus as source evidence, knowledge as generalized guidance, and exemplars as bounded illustrations. Do not write to Corpus, Knowledge, or Exemplars during normal skill use.

## Inspected visual-case layer

`references/preferred_29/` is the user's primary UAV visual-style library: 29 supplied papers, 281 figure-level AI reading records and 12 detailed key designs with layout SVGs. `papers.json` records PDF versions/hashes, story, learning type and coverage. `cases.json` records figure/page, construction, context and transfer limits; selected cards add exact interfaces, collection needs and sketches. Page-level reading does not certify every tiny label or statistical definition. Original PDFs/pages/text remain locally in the sibling `USER_PREFERRED_VISUAL_LIBRARY`, outside the portable package. `scripts/build_preferred_library.py` publishes manually written TSV/JSON notes and never infers review from rendering. `scripts/query_visual_cases.py` prefers this collection by default, falling back to the legacy collection only when no preferred figure matches. Source papers of any venue are eligible as visual references.

`references/visual_cases/cases.json` and its cards are a separate, maintained visual-case layer. They do not overwrite the automated caption catalog or upgrade uninspected figures. Use `python scripts/query_visual_cases.py "disturbance control"` to retrieve by scientific relationship (English tags or Chinese text). A lexical match is not proof of applicability; read the card boundary. Local original page images and context live outside the portable skill. If those files are absent, the recorded AI review remains historical evidence; do not claim a fresh visual inspection. Recreate pages from the identified local PDFs using `scripts/prepare_visual_review.py` when needed.
