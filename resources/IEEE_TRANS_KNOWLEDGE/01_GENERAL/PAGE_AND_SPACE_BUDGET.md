# Page and Space Budget

## Evidence basis

Page allocations are empirical distributions, not quotas. Statistics below use the 100 A-level papers unless a narrower eligible population is stated. Boolean negatives mean *not detected by the conservative extractor*, not confirmed absence.

## Quantitative anatomy

| Measure | Distribution |
|---|---|
| total pages | median 13.5; IQR 11.0-16.0; observed range 8.0-21.0 (n=100) |
| main-text pages | median 12.0; IQR 9.75-14.0; observed range 6.0-21.0 (n=100) |
| Introduction pages | median 1.85; IQR 1.44-2.48; observed range 0.46-20.26 (n=99) |
| Methodology pages | median 3.35; IQR 2.35-5.55; observed range 0.46-9.02 (n=19) |
| Theory pages | median 2.43; IQR 1.95-2.91; observed range 1.95-2.91 (n=2) |
| Experiments pages | median 2.45; IQR 1.67-3.66; observed range 0.61-7.93 (n=56) |
| Conclusion pages | median 2.58; IQR 2.12-3.55; observed range 0.15-6.7 (n=72) |

## Actionable use

- Budget space by claim burden: formulation and proof for theory papers; setup, comparisons, and deployment evidence for system papers.
- Protect enough space for interpretation after tables and figures; do not let a long method crowd out evidence.

## Applicability limits

- Section-length estimates depend on heading extraction and must remain `ESTIMATED`.
- Page budgets vary with journal typesetting and appendices.

## Traceability

Paper-level values are in `../00_META/PAPER_ANATOMY.csv`; rule-to-paper links are in `../00_META/EVIDENCE_REGISTRY.csv`. Do not convert an `ESTIMATED`, `LOWER_BOUND`, or `UNKNOWN` value into an exact claim.
