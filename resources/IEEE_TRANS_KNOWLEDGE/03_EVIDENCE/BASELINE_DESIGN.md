# Baseline Design

## Evidence basis

Evidence architecture is claim-conditioned. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Quantitative anatomy

| Measure | Distribution |
|---|---|
| baseline lower bound | median 1.0; IQR 1.0-2.0; observed range 0.0-8.0 (n=100) |

## Actionable use

- Include classical and recent strong comparators when relevant and keep data, tuning, and evaluation budgets comparable.
- Explain why each baseline represents a method family or claim boundary.

## Applicability limits

- The stored baseline number is only a lower bound from comparison-context detection.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
