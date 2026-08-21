# Sensitivity Design

## Evidence basis

Evidence architecture is claim-conditioned. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| sensitivity | 16/100 | 16.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TRO | 4/10 | 40.0% |
| TAC | 2/5 | 40.0% |
| TEVC | 1/3 | 33.3% |
| TSMCS | 1/3 | 33.3% |
| TASE | 2/7 | 28.6% |
| TFS | 1/4 | 25.0% |
| TCYB | 1/5 | 20.0% |
| TIV | 1/5 | 20.0% |
| TCST | 1/6 | 16.7% |
| TMECH | 1/6 | 16.7% |
| TVT | 1/6 | 16.7% |
| TAES | 0/6 | 0.0% |
| TIE | 0/6 | 0.0% |
| TII | 0/6 | 0.0% |
| TITS | 0/5 | 0.0% |
| TNNLS | 0/5 | 0.0% |
| TAI | 0/4 | 0.0% |
| TCNS | 0/4 | 0.0% |
| TIM | 0/4 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| UAV autonomy paper | 7/35 | 20.0% |
| RL / MARL method paper | 5/35 | 14.3% |
| Navigation / planning paper | 2/14 | 14.3% |
| Autonomous vehicle paper | 2/15 | 13.3% |
| Multi-agent decision paper | 0/1 | 0.0% |

## Actionable use

- Vary parameters that control the proposed mechanism and explain stable versus failure regions.

## Applicability limits

- Routine hyperparameter sweeps do not replace mechanism-focused sensitivity analysis.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
