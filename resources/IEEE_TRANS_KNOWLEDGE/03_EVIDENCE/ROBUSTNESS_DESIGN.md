# Robustness Design

## Evidence basis

Evidence architecture is claim-conditioned. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| robustness | 17/100 | 17.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TCYB | 3/5 | 60.0% |
| TNNLS | 2/5 | 40.0% |
| TII | 2/6 | 33.3% |
| TEVC | 1/3 | 33.3% |
| TSMCS | 1/3 | 33.3% |
| TIM | 1/4 | 25.0% |
| TRO | 2/10 | 20.0% |
| TAC | 1/5 | 20.0% |
| TIV | 1/5 | 20.0% |
| TAES | 1/6 | 16.7% |
| TIE | 1/6 | 16.7% |
| TASE | 1/7 | 14.3% |
| TCST | 0/6 | 0.0% |
| TMECH | 0/6 | 0.0% |
| TVT | 0/6 | 0.0% |
| TITS | 0/5 | 0.0% |
| TAI | 0/4 | 0.0% |
| TCNS | 0/4 | 0.0% |
| TFS | 0/4 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| UAV autonomy paper | 8/35 | 22.9% |
| RL / MARL method paper | 5/35 | 14.3% |
| Navigation / planning paper | 2/14 | 14.3% |
| Autonomous vehicle paper | 2/15 | 13.3% |
| Multi-agent decision paper | 0/1 | 0.0% |

## Actionable use

- Vary the uncertainty named by the claim—noise, disturbance, topology, obstacle density, model error, or adversarial condition.

## Applicability limits

- Do not label ordinary multi-scenario comparison as robustness without a controlled stress dimension.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
