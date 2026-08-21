# Runtime And Complexity

## Evidence basis

Evidence architecture is claim-conditioned. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| runtime | 48/100 | 48.0% |
| complexity | 20/100 | 20.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TEVC | 3/3 | 100.0% |
| TSMCS | 3/3 | 100.0% |
| TRO | 8/10 | 80.0% |
| TIV | 4/5 | 80.0% |
| TASE | 5/7 | 71.4% |
| TCST | 4/6 | 66.7% |
| TIE | 4/6 | 66.7% |
| TAES | 3/6 | 50.0% |
| TMECH | 3/6 | 50.0% |
| TFS | 2/4 | 50.0% |
| TIM | 2/4 | 50.0% |
| TII | 2/6 | 33.3% |
| TAC | 1/5 | 20.0% |
| TCYB | 1/5 | 20.0% |
| TITS | 1/5 | 20.0% |
| TNNLS | 1/5 | 20.0% |
| TVT | 1/6 | 16.7% |
| TAI | 0/4 | 0.0% |
| TCNS | 0/4 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| Autonomous vehicle paper | 9/15 | 60.0% |
| Navigation / planning paper | 7/14 | 50.0% |
| RL / MARL method paper | 16/35 | 45.7% |
| UAV autonomy paper | 16/35 | 45.7% |
| Multi-agent decision paper | 0/1 | 0.0% |

## Actionable use

- Report hardware/software, batch size or agent count, latency/frequency, and complexity measure that match deployment claims.

## Applicability limits

- Asymptotic complexity alone is insufficient for a real-time claim.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
