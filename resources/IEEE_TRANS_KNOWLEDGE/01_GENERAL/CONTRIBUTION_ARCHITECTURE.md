# Contribution Architecture

## Evidence basis

Contribution counts are estimated only from reliably delimited Introduction blocks. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Quantitative anatomy

| Measure | Distribution |
|---|---|
| contribution count | median 3.0; IQR 3.0-3.0; observed range 1.0-8.0 (n=33) |
| major claim taxonomy count | median 3.0; IQR 2.0-4.25; observed range 0.0-9.0 (n=100) |

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| contribution block count available | 33/100 | 33.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TAI | 3/4 | 75.0% |
| TIE | 4/6 | 66.7% |
| TCNS | 2/4 | 50.0% |
| TIM | 2/4 | 50.0% |
| TASE | 3/7 | 42.9% |
| TIV | 2/5 | 40.0% |
| TNNLS | 2/5 | 40.0% |
| TAES | 2/6 | 33.3% |
| TCST | 2/6 | 33.3% |
| TII | 2/6 | 33.3% |
| TVT | 2/6 | 33.3% |
| TRO | 3/10 | 30.0% |
| TAC | 1/5 | 20.0% |
| TCYB | 1/5 | 20.0% |
| TITS | 1/5 | 20.0% |
| TMECH | 1/6 | 16.7% |
| TFS | 0/4 | 0.0% |
| TEVC | 0/3 | 0.0% |
| TSMCS | 0/3 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| Multi-agent decision paper | 1/1 | 100.0% |
| UAV autonomy paper | 14/35 | 40.0% |
| Navigation / planning paper | 5/14 | 35.7% |
| Autonomous vehicle paper | 4/15 | 26.7% |
| RL / MARL method paper | 9/35 | 25.7% |

## Actionable use

- Write contributions as specific, verifiable advances: mechanism/formulation/system/theory plus the evidence that can test them.
- Align each contribution with a method subsection and an evidence item.
- Treat routine implementation and 'extensive experiments' as support, not standalone novelty.

## Applicability limits

- UNKNOWN contribution counts are excluded from denominators.
- The taxonomy does not judge novelty; it checks specificity and testability.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
