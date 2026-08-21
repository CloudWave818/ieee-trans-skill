# Equation Narrative

## Evidence basis

Writing patterns are paraphrased from corpus-level evidence; no source sentence is a template. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Quantitative anatomy

| Measure | Distribution |
|---|---|
| equation lower bound | median 25.5; IQR 13.0-36.25; observed range 2.0-70.0 (n=100) |

## Observed patterns

| Pattern | Evidence | Ratio |
|---|---:|---:|
| problem formulation | 29/100 | 29.0% |
| ablation | 19/100 | 19.0% |
| robustness | 17/100 | 17.0% |
| generalization | 54/100 | 54.0% |

## Journal-conditioned view

| Journal | Evidence | Ratio |
|---|---:|---:|
| TVT | 4/6 | 66.7% |
| TITS | 3/5 | 60.0% |
| TAES | 3/6 | 50.0% |
| TAC | 2/5 | 40.0% |
| TIV | 2/5 | 40.0% |
| TNNLS | 2/5 | 40.0% |
| TRO | 3/10 | 30.0% |
| TASE | 2/7 | 28.6% |
| TAI | 1/4 | 25.0% |
| TCNS | 1/4 | 25.0% |
| TFS | 1/4 | 25.0% |
| TIM | 1/4 | 25.0% |
| TCYB | 1/5 | 20.0% |
| TCST | 1/6 | 16.7% |
| TII | 1/6 | 16.7% |
| TMECH | 1/6 | 16.7% |
| TIE | 0/6 | 0.0% |
| TEVC | 0/3 | 0.0% |
| TSMCS | 0/3 | 0.0% |

## Paper-type-conditioned view

| Primary type | Evidence | Ratio |
|---|---:|---:|
| UAV autonomy paper | 16/35 | 45.7% |
| Navigation / planning paper | 4/14 | 28.6% |
| RL / MARL method paper | 7/35 | 20.0% |
| Autonomous vehicle paper | 2/15 | 13.3% |
| Multi-agent decision paper | 0/1 | 0.0% |

## Actionable use

- Before an equation, state why it is needed and what relationship is being formalized.
- After it, define the consequence, link to the next equation/algorithm, and state the claim served.

## Applicability limits

- Functional analysis does not license copying wording from any paper.
- Human review is required for paragraph-level quality judgments.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
