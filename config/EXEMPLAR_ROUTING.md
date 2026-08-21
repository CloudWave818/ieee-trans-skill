# Exemplar Routing

Use `IEEE_TRANS_EXEMPLARS/00_META/EXEMPLAR_ROUTING.csv`, then open only the selected cards.

## Input

Normalize target journal, two to four domains, paper type, method type, current task, current section, evidence needs, and optional rule IDs.

## Hard gates

1. Exclude a card whose `Do Not Generalize` boundary conflicts with the project.
2. Require at least one role/current-section or evidence-need match.
3. Reject scores below 35 unless fewer than three cards pass; label fallback cards.
4. Return three cards by default; allow four or five only for a cross-domain or multi-section task; never exceed five.

## Transparent score

| Feature | Points |
|---|---:|
| all requested domains / one requested domain / adjacent domain | 30 / 20 / 10 |
| exact primary role / compatible role | 25 / 15 |
| exact paper type / compatible hybrid | 15 / 8 |
| exact target journal | 15 |
| all / partial evidence needs | 10 / 5 |
| requested rule linked | 5 |

Break ties by role match, domain match, then teaching value. Citation count is not a routing feature.

## Re-route by task

Map experiment design to `EXPERIMENT_ARCHITECTURE`, results to `RESULT_NARRATIVE`, introduction to `INTRODUCTION`, figures to `FIGURE_ARCHITECTURE` or `FIGURE`, tables to `TABLE_ARCHITECTURE` or `TABLE`, formulation/theory to their exact roles, and real-world claims to `REAL_WORLD_VALIDATION` plus `REAL_WORLD` evidence.

Do not fix one exemplar set for the entire manuscript. Record card IDs, scores, matched dimensions, exclusions, and boundaries in each Section Brief.
