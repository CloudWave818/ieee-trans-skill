# 04 Claim–Evidence Design

## Entry

Require known contributions or an existing manuscript whose claims can be extracted.

## Procedure

1. Copy `templates/CLAIM_EVIDENCE_MATRIX.md`.
2. List every major claim and the conditions under which it is asserted.
3. Classify the claim: correctness, mechanism, performance, robustness, generalization, efficiency/runtime, scalability, safety, feasibility, or real-world/deployment.
4. Load applicable General rules, two to four domain profiles, and the locked journal rule.
5. Define the minimum evidence that could falsify or support the claim.
6. Record available evidence separately from planned evidence.
7. Map each claim to experiment, metric, baseline, figure/table, and status.
8. Mark dependencies among claims so a failed upstream mechanism claim cannot leave downstream claims intact.

## Status vocabulary

- `CLOSED`: direct evidence exists and its boundary matches the claim.
- `PARTIAL`: evidence exists but a condition, comparator, or analysis is missing.
- `PLANNED`: an executable evidence plan exists but no result exists.
- `CLAIM_WITHOUT_EVIDENCE`: no adequate evidence or plan.
- `NOT_APPLICABLE`: explicitly justified by paper type and claim scope.

Never relabel `PLANNED` as `CLOSED`. Do not use corpus prevalence as evidence for the new paper.

## Exit

All major claims are `CLOSED`, `PARTIAL`, or `PLANNED` with honest labels. Any `CLAIM_WITHOUT_EVIDENCE` becomes a blocker for result, abstract, conclusion, and submission-readiness prose.
