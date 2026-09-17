# Figure/Table Audit

## Checks

- Does every asset answer a scientific question and support a claim?
- Is its evidence role distinct from nearby assets?
- Would deleting it remove information rather than decoration?
- Is a figure used for relationships and a table for exact comparisons/settings appropriately?
- Does the sequence follow the argument and paper type?
- Are axes, units, legends, uncertainty, baselines, and conditions complete and consistent?
- Do captions explain context and encoding without replacing results interpretation?
- Are tables and figures free of duplicated data unless the dual view has a scientific reason?
- Are callouts, numbering, panel labels, and cross-references consistent?
- Do visuals avoid implying unavailable significance, hardware, scenarios, or precision?
- Does every figure have an exact subtype and one declared rendering route?
- Does every `DATA_PLOT` specify source columns, axes, units, groups, aggregation, uncertainty, and transformations?
- Does every `VECTOR_SCHEMATIC` specify nodes, edges, labels, grouping, direction, and layout rather than a vague visual theme?
- Does every `PHOTO_COMPOSITE` use traceable real files and factual annotations rather than generated physical evidence?
- Is `PAPER_FIGURE_DESCRIPTION.md` complete enough for a downstream AI or researcher to execute without guessing scientific content?
- Does each handoff block distinguish visually flexible elements from scientifically exact elements and prohibited inventions?
- Does every existing figure have a justified `KEEP`, `REDESIGN`, `MERGE`, or `DELETE` decision, and every proposed figure a justified `ADD` decision?
- For UAV work, where no more specific user style applies, does the figure deliberately adapt a relevant preferred-29 construction (palette, grouping, pictograms, connectors, panel relationships), while preserving manuscript-specific objects and evidence?
- For actual RL training, is the learning-process figure considered with explicit budget, reward/evaluation definition, independent seeds and uncertainty, separately from deployment success/safety?
- Does the graph use the actual policy action interface, expose any action conversion, and keep training-only privileged inputs out of deployment?

- Does the corpus prior support only the scope claimed, with exact figure/page/image references for construction claims?
- Are manuscript-derived designs allowed and labeled honestly when no inspected reference matches?
- Does the mechanism view expose a specific changed operation and its observable consequence?
- Do key figures have a layout sketch and an executable trial/time/data collection contract?
- Are specification, rendering, final-width inspection and independent handoff reported separately with actual artifacts?

## Framework-specific style audit

For method/network/system architecture only, read `../references/FRAMEWORK_STYLE_PLAYBOOK.md`. Mark this section `NOT_REQUIRED_FOR_LOCAL_TASK` for unrelated figure families.

- Is `PASTEL_LAYERED_FRAMEWORK` applied, or is a current user override / locked existing figure documented?
- Does the brief include `style_id`, source-grounded `FROZEN_STORYBOARD`, `RENDER_LOCK`, borrowed visual grammar, do-not-copy boundary, and final-size design tokens?
- Are pale dashed functional groups, serif stage headings, compact solid-border modules, and fine dark connectors used with readable spacing?
- Do local pictograms explain actual inputs/representations/operations, and is the core changed operation visible instead of hidden in generic boxes?
- Are recurrence, repeated stacks/counts, multi-head branches, gradients, and training/deployment interfaces supported rather than copied from the reference?
- Are group-boundary dashes distinguished from training-only edges, with no privileged-information leakage into deployment?
- Are schematic insets distinguished from measured/quantitative insets, with the latter independently routed to source-grounded `DATA_PLOT`?
- Do final labels/edges match the frozen storyboard, and are editable text/nodes/edges preserved in the actual source rather than a raster inside a vector container?
- Are final-width readability and preview/source agreement checked with actual artifacts? When unrendered, record visual checks as `NOT_EXECUTED`, not passed.

Wrong scientific edges, invented modules/data, or training/deployment leakage are `BLOCKER`. Clear failure to follow the applicable user style, an opaque generic-box mechanism, or final-size unreadability is `MAJOR`. Minor spacing/alignment/color deviations are `MINOR`. A missing rendering artifact is a pending visual check, not evidence of success or a fabricated failure result.

## Blockers

Mark `BLOCKER` for misleading encoding, wrong or invented data, synthetic physical evidence presented as real, missing central evidence, irreproducible comparison conditions, or a visual contradicting the text.

## Output

Return `KEEP`, `REVISE`, `MERGE`, `DELETE`, or `ADD`, plus the evidence role, exact subtype, rendering route, and executable repair. For whole-paper work, also return a pass/fail decision for `PAPER_FIGURE_DESCRIPTION.md`.
