# Figure/Table Audit

## Checks

- For reference-matched tasks, were the main source and actual crop/page opened, and source/new renderings compared for geometry, hierarchy, pictograms, fonts, arrows and density? Similar colors or a completed brief do not pass. Distinguish sketches from originals and record scientifically necessary deviations in STYLE_LOCK.

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
- If a local original was borrowed, was its complete source context inspected and its drawing rebuilt with current scientific objects? A source patch is a reference, not a new-method asset. Input/context pictures inside a computation box do not by themselves explain that computation.
- Do key figures have a layout sketch and an executable trial/time/data collection contract?
- Are specification, rendering, final-width inspection and independent handoff reported separately with actual artifacts?

## Whole-paper rendering check

For a whole-paper deliverable, inspect the actual figure group in manuscript context: overview, necessary mechanism views, experimental setup and available evidence figures. Compare their order, relative space, captions and first text callouts with the selected source. Do not prescribe every figure type or the donor's figure count. Planned data plots are not rendered evidence, and one completed framework does not establish the appearance of the complete paper.

## Publication width and mixed figure group

- Are single-column width, full text width and available height obtained from the actual template, or explicitly provisional?
- Are publication span, physical width × height, canvas shape, panel grid and span rationale recorded separately? Single-column does not mean portrait, and cross-column does not mean landscape.
- Does the two-column paper use single-column assets where compact questions allow them, with cross-column overviews/composites where needed? Mark an unexplained all-wide group or repeated wide-strip canvas `REVISE`; landscape single-column plots are valid. Check scientific reasons rather than imposing a count or shape ratio.
- Was a wide composition recomposed for single-column placement instead of merely shrunk? Inspect final-size labels, legends, line widths, marker separation and scientific detail. Panel count alone cannot justify cross-column width.
- Do plan → handoff → exported bounding box → actual manuscript span/scale agree? In two-column LaTeX, check `figure`/`figure*`, the relevant `\columnwidth`/`\textwidth`, and local `\linewidth` inside panels; use equivalent controls in other editors.
- Do figure height, caption and first callout fit the manuscript page without excessive blanks or a chain of unnecessary wide floats? Record actual preview/PDF pages for executed checks; planning-only tasks keep export/insertion checks `NOT_EXECUTED`.

## Blockers

Mark `BLOCKER` for misleading encoding, wrong or invented data, synthetic physical evidence presented as real, missing central evidence, irreproducible comparison conditions, or a visual contradicting the text.

## Output

Return `KEEP`, `REVISE`, `MERGE`, `DELETE`, or `ADD`, plus the evidence role, exact subtype, rendering route, and executable repair. For whole-paper work, also return a pass/fail decision for `PAPER_FIGURE_DESCRIPTION.md`.
