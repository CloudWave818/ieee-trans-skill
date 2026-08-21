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
| figures/tables | matching files in `04_VISUALS/`, evidence needs, visual-role cards |
| page budget | `01_GENERAL/PAGE_AND_SPACE_BUDGET.md`, paper-type route, journal profile |
| reviewer audit | rule registry, target journal, claim/evidence artifacts, `audits/REVIEWER_AUDIT.md` |

## Memory boundary

Treat user-provided methods, data, figures, experiments, contributions, drafts, and reviewer comments as primary project evidence. Treat the corpus as source evidence, knowledge as generalized guidance, and exemplars as bounded illustrations. Do not write to Corpus, Knowledge, or Exemplars during normal skill use.
