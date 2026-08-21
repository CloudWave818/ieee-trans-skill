# Ablation Design

## Evidence basis

Evidence architecture is claim-conditioned. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| ablation | 19/100 | 19.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TEVC | 2/3 | 66.7% |
| TASE | 3/7 | 42.9% |
| TRO | 4/10 | 40.0% |
| TAES | 2/6 | 33.3% |
| TSMCS | 1/3 | 33.3% |
| TFS | 1/4 | 25.0% |
| TIM | 1/4 | 25.0% |
| TITS | 1/5 | 20.0% |
| TIV | 1/5 | 20.0% |
| TNNLS | 1/5 | 20.0% |
| TII | 1/6 | 16.7% |
| TVT | 1/6 | 16.7% |
| TCST | 0/6 | 0.0% |
| TIE | 0/6 | 0.0% |
| TMECH | 0/6 | 0.0% |
| TAC | 0/5 | 0.0% |
| TCYB | 0/5 | 0.0% |
| TAI | 0/4 | 0.0% |
| TCNS | 0/4 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| RL / MARL method paper | 9/35 | 25.7% |
| UAV autonomy paper | 6/35 | 17.1% |
| Navigation / planning paper | 2/14 | 14.3% |
| Autonomous vehicle paper | 2/15 | 13.3% |
| Multi-agent decision paper | 0/1 | 0.0% |

## Actionable use

- Ablate only claimed mechanisms; removal, replacement, or controlled parameter variation should match the claimed effect.

## Applicability limits

- Do not demand ablation from monolithic proof contributions when a theorem or controlled comparison is the direct test.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
