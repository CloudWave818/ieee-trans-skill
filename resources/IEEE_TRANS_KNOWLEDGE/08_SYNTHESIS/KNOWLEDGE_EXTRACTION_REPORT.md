# Knowledge Extraction Report

Status: `PHASE 2 KNOWLEDGE EXTRACTION COMPLETE / READY FOR HUMAN REVIEW`

## Corpus use

- Analysed papers: 120
- A-level primary evidence: 100
- B-level validation/edge cases: 20
- A denominators are never changed by B papers.

## Output inventory

- Candidate patterns tested: 22
- Formal rules retained: 42
- General rules: 7
- Domain rules: 22
- Journal-specific rules: 13
- Explicit conflict classes: 5
- Exemplar candidates: 30

## Required 20-part phase summary

1. Analysed papers: 120.
2. Evidence roles: 100 A-level papers define denominators; 20 B-level papers validate, challenge, or extend boundaries.
3. Candidate patterns tested: 22.
4. Formal rules retained: 42.
5. General Transactions rules: 7.
6. Domain rules: 22.
7. Journal-specific rules: 13.
8. Explicit conflict classes: 5.
9. Transactions commonality: claim-to-evidence alignment, not one mandatory outline. Overall pages are median 13.5; IQR 11.0-16.0; observed range 8.0-21.0 (n=100); main sections are median 5.0; IQR 3.0-6.0; observed range 1.0-13.0 (n=99).
10. Robotics difference: spatial/system figures, runtime, and physical evidence carry more weight when deployment is claimed.
11. AI/Learning difference: mechanism isolation, robustness/generalization, and transfer boundaries require claim-specific experiments.
12. Control difference: assumptions, stability/convergence, and proof can carry evidence that modular ablation carries in learning papers.
13. UAV/Autonomy difference: planning/control performance must be routed through operating conditions such as disturbance, obstacles, topology, sensing, or onboard limits.
14. Figure pattern: median 10.0; IQR 8.0-15.0; observed range 2.0-35.0 (n=100); the catalog records each caption candidate and preserves unclassified roles for review.
15. Table pattern: median 2.0; IQR 1.0-4.0; observed range 0.0-13.0 (n=100); tables favour exact multi-method/multi-metric comparison, settings, runtime, and compact stress results.
16. Experiment architecture: main comparison establishes headline performance; ablation/proof isolates mechanisms; robustness/generalization/runtime/physical layers test the scope of claims.
17. Results narrative: Observation -> quantitative comparison -> mechanism explanation -> bounded implication; data restatement alone is insufficient.
18. AI-writing antipatterns: generic motivation, empty superiority claims, repeated signposting, module inventories without rationale, table-value restatement, and conclusions detached from evidence.
19. Exemplar candidates selected: 30 (cards intentionally deferred to Phase 3).
20. Human judgment still required: confirm every ESTIMATED/LOWER_BOUND/UNKNOWN field, semantic rhetorical map, caption role, panel/layout decision, and PDF-version pagination before hard editorial use.

## Experiment evidence prevalence in A-level corpus

| Pattern | Evidence | Ratio |
|---|---:|---:|
| simulation | 95/100 | 95.0% |
| physical | 48/100 | 48.0% |
| ablation | 19/100 | 19.0% |
| robustness | 17/100 | 17.0% |
| generalization | 54/100 | 54.0% |
| runtime | 48/100 | 48.0% |

## Human-review queue

- Start with the 30 exemplar candidates and check their Introduction maps, claim-evidence links, Figure/Table catalog rows, and result paragraphs.
- Confirm every `ESTIMATED`, `AUTOMATED_LOWER_BOUND`, and `UNKNOWN` anatomy field before using it as a hard editorial constraint.
- Resolve source-PDF versions whose pagination differs from the final IEEE version.

## Stop condition

Phase 3 exemplar cards and the final `SKILL.md` were not created. The corpus directory was treated as read-only.
