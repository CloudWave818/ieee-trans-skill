# Section Architecture

## Evidence basis

Section presence is conditioned by paper type, domain, and journal. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Quantitative anatomy

| Measure | Distribution |
|---|---|
| main sections | median 5.0; IQR 3.0-6.0; observed range 1.0-13.0 (n=99) |
| subsections | median 12.0; IQR 8.75-15.0; observed range 0.0-35.0 (n=100) |

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| Related Work independent | 24/100 | 24.0% |
| Preliminaries independent | 17/100 | 17.0% |
| Problem Formulation independent | 29/100 | 29.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TASE | 5/7 | 71.4% |
| TRO | 6/10 | 60.0% |
| TITS | 3/5 | 60.0% |
| TFS | 2/4 | 50.0% |
| TVT | 2/6 | 33.3% |
| TSMCS | 1/3 | 33.3% |
| TAC | 1/5 | 20.0% |
| TIV | 1/5 | 20.0% |
| TAES | 1/6 | 16.7% |
| TCST | 1/6 | 16.7% |
| TIE | 1/6 | 16.7% |
| TII | 0/6 | 0.0% |
| TMECH | 0/6 | 0.0% |
| TCYB | 0/5 | 0.0% |
| TNNLS | 0/5 | 0.0% |
| TAI | 0/4 | 0.0% |
| TCNS | 0/4 | 0.0% |
| TIM | 0/4 | 0.0% |
| TEVC | 0/3 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| UAV autonomy paper | 10/35 | 28.6% |
| RL / MARL method paper | 9/35 | 25.7% |
| Autonomous vehicle paper | 3/15 | 20.0% |
| Navigation / planning paper | 2/14 | 14.3% |
| Multi-agent decision paper | 0/1 | 0.0% |

## Actionable use

- Split a section when it creates a reusable contract for later reasoning: notation, assumptions, system model, or evaluation protocol.
- Merge short background material when separation would interrupt the problem-to-mechanism chain.

## Applicability limits

- A low prevalence signals an alternative pattern, not a prohibition.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
