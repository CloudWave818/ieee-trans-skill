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
- For UAV work, does the figure deliberately adapt a relevant preferred-29 construction (palette, grouping, pictograms, connectors, panel relationships), while preserving manuscript-specific objects and evidence?
- For actual RL training, is the learning-process figure considered with explicit budget, reward/evaluation definition, independent seeds and uncertainty, separately from deployment success/safety?
- Does the graph use the actual policy action interface, expose any action conversion, and keep training-only privileged inputs out of deployment?

- Does the corpus prior support only the scope claimed, with exact figure/page/image references for construction claims?
- Are manuscript-derived designs allowed and labeled honestly when no inspected reference matches?
- Does the mechanism view expose a specific changed operation and its observable consequence?
- Do key figures have a layout sketch and an executable trial/time/data collection contract?
- Are specification, rendering, final-width inspection and independent handoff reported separately with actual artifacts?

## Blockers

Mark `BLOCKER` for misleading encoding, wrong or invented data, synthetic physical evidence presented as real, missing central evidence, irreproducible comparison conditions, or a visual contradicting the text.

## Output

Return `KEEP`, `REVISE`, `MERGE`, `DELETE`, or `ADD`, plus the evidence role, exact subtype, rendering route, and executable repair. For whole-paper work, also return a pass/fail decision for `PAPER_FIGURE_DESCRIPTION.md`.
