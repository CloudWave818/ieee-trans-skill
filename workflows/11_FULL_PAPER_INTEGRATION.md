# 11 Full Paper Integration and Revision

## Entry

Use for `FULL_DRAFT`, `REVISION`, Mode D, or Mode J. Preserve the existing manuscript until diagnosis justifies a change.

## Manuscript diagnosis

Audit scientific logic, contribution alignment, claim evidence, section balance, experiment sufficiency, figure/table logic, result interpretation, journal fit, AI-writing patterns, terminology, clarity, and reviewer comments.

Classify every recommended action:

- `KEEP` — correct and aligned;
- `REVISE` — local wording or evidence-boundary change;
- `RESTRUCTURE` — move or rebuild argument units;
- `DELETE` — redundant, unsupported, or distracting;
- `ADD` — a scientifically necessary missing unit supported by available evidence or explicitly planned work.

## Integration procedure

1. Reconstruct the paper-level Problem→Gap→Challenge→Mechanism→Claim→Evidence chain from the draft.
2. Compare it with contribution and claim matrices; log contradictions.
3. Build or update `templates/TERMINOLOGY_LEDGER.md` from all observed terms before making local wording edits.
4. Resolve same-concept/multiple-name and same-name/multiple-concept conflicts. Choose one canonical name from meaning, field convention, and author intent—not from occurrence count alone.
5. Create a global rename plan and apply it across title, abstract, contributions, headings, prose, notation, equations, algorithms, figures, tables, captions, legends, experiments, conclusion, and supplementary material.
6. Reconcile assumptions, datasets, baseline names, metrics, and numerical values across sections.
7. Remove unjustified one-off terminology and acronyms; distinguish related concepts whose differences matter scientifically.
8. Reconcile every in-text figure/table callout with its evidence role and canonical terminology.
9. Apply the locked journal profile without changing scientific content to chase style.
10. Route only affected sections through `09_SECTION_WRITING.md`.
11. For revision, map every reviewer request to manuscript evidence and a response action; do not promise unperformed work as completed.

## Exit

Produce a prioritized change map, a completed Terminology Ledger, and an integrated draft whose claims, evidence, figures/tables, notation, and terminology agree. Run `audits/TERMINOLOGY_CLARITY_AUDIT.md`, then Final Audit.
