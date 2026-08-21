# Methodology

## Evidence basis

Focused analysis for methodology. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Quantitative anatomy

| Measure | Distribution |
|---|---|
| method pages | median 3.35; IQR 2.35-5.55; observed range 0.46-9.02 (n=19) |
| equation lower bound | median 25.5; IQR 13.0-36.25; observed range 2.0-70.0 (n=100) |

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| algorithm block | 67/100 | 67.0% |
| problem formulation | 29/100 | 29.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TVT | 6/6 | 100.0% |
| TITS | 5/5 | 100.0% |
| TAI | 4/4 | 100.0% |
| TEVC | 3/3 | 100.0% |
| TRO | 8/10 | 80.0% |
| TCYB | 4/5 | 80.0% |
| TASE | 5/7 | 71.4% |
| TAES | 4/6 | 66.7% |
| TCST | 4/6 | 66.7% |
| TII | 4/6 | 66.7% |
| TMECH | 4/6 | 66.7% |
| TSMCS | 2/3 | 66.7% |
| TAC | 3/5 | 60.0% |
| TIV | 3/5 | 60.0% |
| TCNS | 2/4 | 50.0% |
| TIM | 2/4 | 50.0% |
| TNNLS | 2/5 | 40.0% |
| TFS | 1/4 | 25.0% |
| TIE | 1/6 | 16.7% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| Multi-agent decision paper | 1/1 | 100.0% |
| UAV autonomy paper | 29/35 | 82.9% |
| RL / MARL method paper | 22/35 | 62.9% |
| Navigation / planning paper | 8/14 | 57.1% |
| Autonomous vehicle paper | 7/15 | 46.7% |

## Actionable use

- For each component write Challenge -> design principle -> mathematical mechanism -> expected effect -> evidence target.
- Use framework figures for relationships and prose/equations for causal reasoning.
- Include an algorithm box only when execution order or branching adds information.

## Applicability limits

- Avoid Module A + B + C narration without a reason for each connection.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
