# 04 Claim–Evidence Design

## Entry

Require known contributions or an existing manuscript whose claims can be extracted.

## Procedure

1. Copy `templates/CLAIM_EVIDENCE_MATRIX.md`, or embed the relevant rows in a tightly scoped requested artifact.
2. List every major claim and the conditions under which it is asserted.
3. Classify the claim: correctness, mechanism, performance, robustness, generalization, efficiency/runtime, scalability, safety, feasibility, or real-world/deployment.
4. Load applicable General rules, two to four domain profiles, and the locked journal rule for full-project work. For a one-figure task, use only scopes that change the decision; a journal may remain UNDECIDED.
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

That exit condition governs evidence completion. A local provisional plan may be returned with `CLAIM_WITHOUT_EVIDENCE` and explicit missing definitions/materials; it does not close the gate. Do not call a plan `PLANNED` merely because it lists an experiment if the metric, intervention or source requirements remain too ambiguous to execute. Continue the unaffected planning work and retain the blocker on the unsupported result claim.
