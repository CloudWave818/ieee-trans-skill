# Generalization Design

## Evidence basis

Evidence architecture is claim-conditioned. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| generalization | 54/100 | 54.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TEVC | 3/3 | 100.0% |
| TASE | 6/7 | 85.7% |
| TFS | 3/4 | 75.0% |
| TRO | 7/10 | 70.0% |
| TAES | 4/6 | 66.7% |
| TMECH | 4/6 | 66.7% |
| TSMCS | 2/3 | 66.7% |
| TAC | 3/5 | 60.0% |
| TCYB | 3/5 | 60.0% |
| TITS | 3/5 | 60.0% |
| TIV | 3/5 | 60.0% |
| TCST | 3/6 | 50.0% |
| TIM | 2/4 | 50.0% |
| TIE | 2/6 | 33.3% |
| TII | 2/6 | 33.3% |
| TVT | 2/6 | 33.3% |
| TAI | 1/4 | 25.0% |
| TNNLS | 1/5 | 20.0% |
| TCNS | 0/4 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| Autonomous vehicle paper | 10/15 | 66.7% |
| RL / MARL method paper | 20/35 | 57.1% |
| Navigation / planning paper | 8/14 | 57.1% |
| UAV autonomy paper | 16/35 | 45.7% |
| Multi-agent decision paper | 0/1 | 0.0% |

## Actionable use

- Use unseen maps/tasks, cross-scenario or cross-domain tests, or changed agent counts when these represent the claimed transfer boundary.

## Applicability limits

- Do not infer generalization from higher in-distribution accuracy.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
