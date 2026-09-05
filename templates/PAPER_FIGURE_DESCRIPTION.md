# Paper Figure Description

This is the consolidated, AI-readable visual specification for one manuscript. It describes what every figure is, why it exists, which real inputs it requires, and how a plotting or design system should construct it without inventing scientific content.

## Document control

- Project/manuscript:
- Manuscript version/date:
- Target journal:
- Paper archetype:
- Source manuscript and supplements:
- Experiment/log/code/photo locations:
- Claim–Evidence Matrix location/version:
- Terminology Ledger location/version:
- Description status: `PROVISIONAL_FROM_TITLE` / `PROVISIONAL` / `DATA_PENDING` / `READY_TO_DRAW` / `AUDITED`

Description status audits the specification only. Actual rendering, final-width visual checks, and independent execution must be supported separately in the collection/execution record.

## Visual thesis and sequence

- One-sentence visual thesis:
- Reader journey: problem → system/setup → method → mechanism → protocol → main evidence → boundary/physical closure
- Minimum defensible figure count:
- Recommended working figure count:
- Tables planned:
- Figures to merge/delete and why:
- Major claims without a planned visual or nonvisual proof:

## Figure classification summary

| ID | Existing/proposed | Current action (`KEEP`/`REDESIGN`/`MERGE`/`DELETE`/`ADD`) | Proposed number/title | Primary family | Exact subtype | Rendering route (`DATA_PLOT`/`VECTOR_SCHEMATIC`/`PHOTO_COMPOSITE`/`TABLE`/`NOT_READY`) | 100-paper corpus rule ID(s), if applicable | Manuscript trigger | Main claim | Source inputs | Section | Width | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Reference figure-pattern evidence

For UAV figures prioritize the user's preferred 29. Deliberately adapt their color relationships, grouping, pictogram grammar, connectors and panel composition to manuscript-specific objects and mechanisms. Identify the exact borrowed construction and changes. Do not pass reference photographs, measured curves or claims off as the author's evidence.

| Source paper/ID | Figure number | Observed exact subtype | Evidence role learned | Construction principle reusable here | Why applicable | Do-not-copy boundary |
|---|---|---|---|---|---|---|

## Cross-figure visual dictionary

- Proposed method color / line / marker:
- Recent-learning baseline encoding:
- Traditional/model-based baseline encoding:
- Reference/target encoding:
- Unsafe region / constraint / failure encoding:
- Train versus deployment encoding:
- Simulation versus real-world encoding:
- Agent identity scheme:
- Canonical terminology and symbol source:
- Grayscale/accessibility redundancy:
- Panel-label, font, and unit conventions:

---

## Figure [ID]: [working title]

Repeat this entire block for every figure. Do not leave a vague placeholder such as “result graph.”

### A. Identity and scientific function

- Proposed number:
- Origin: `EXISTING` / `PROPOSED`
- Current action: `KEEP` / `REDESIGN` / `MERGE` / `DELETE` / `ADD`
- Existing figure/caption source, if any:
- Related section and first citation point:
- Core claim defended:
- Scientific question answered:
- Evidence role:
- 100-paper corpus rule ID(s), if applicable; scope of support:
- Inspected case ID, figure/page, source image and review status; or `NO_MATCHING_INSPECTED_REFERENCE`:
- `MANUSCRIPT_DERIVED` design rationale and alternative, when applicable:
- Manuscript-specific trigger and location:
- Three-layer inclusion decision (CORPUS_PRIOR / INSPECTED_REFERENCE / MANUSCRIPT_DESIGN):
- Priority: `MANDATORY` / `CONDITIONAL`
- What the paper loses if removed:
- Reference figure-pattern entries used:
- Do-not-copy boundary:

### B. Classification decision

- Primary family: conceptual/schematic / quantitative / spatial/trajectory / physical/qualitative / composite
- Exact subtype:
- Rendering route: `DATA_PLOT` / `VECTOR_SCHEMATIC` / `PHOTO_COMPOSITE` / `NOT_READY`
- Relationship the reader must perceive: structure / sequence / trend / category difference / distribution / spatial behavior / physical evidence
- Why this type is appropriate:
- Why the main alternative type is weaker:

### C. One-paragraph visual description

Describe exactly what the finished figure should look like from left to right and top to bottom. Include the first element the reader should notice, the visual hierarchy, panel relationship, and visible takeaway. This paragraph should be understandable without seeing the manuscript.

### D. Canvas and panel layout

- Target width: one-column / two-column / page-wide
- Target aspect ratio:
- Panel grid and reading order:
- Shared axes/legend/colorbar:
- Minimum final text size:
- Layout sketch (required for key mechanisms/composites; no invented result curves):
- Bottleneck → changed operation → signal/decision change → observable consequence → experiment:

| Panel | Evidence job | Exact content | Axes/units or spatial layout | Series/objects and encoding | Required annotations | Source dependency |
|---|---|---|---|---|---|---|

### E1. Data schema and plotting specification — complete for `DATA_PLOT`

| Field/column | Scientific meaning | Unit | Plot role (x/y/group/facet/error/annotation) | Filtering | Aggregation/transformation | Source file/log |
|---|---|---|---|---|---|---|

- Methods/baselines and authoritative names:
- Scenario/dataset/test condition:
- Metric definition and higher/lower direction:
- Common budget/fairness condition:
- Runs/seeds/folds and selected-trial rule:
- Center statistic:
- Uncertainty/error bar/band:
- Smoothing, normalization, interpolation, or log scale and justification:
- Axis limits/ticks/reference lines/events/bounds:
- Missing-data and outlier handling:
- Values or geometry that must come only from data:

For a training convergence curve additionally state training versus evaluation measurements, evaluation cadence, total training budget, stopping/convergence criterion, raw versus smoothed traces, and whether all methods use the same x-axis budget.

### E2. Node-edge specification — complete for `VECTOR_SCHEMATIC`

| Node/group ID | Exact label | Scientific role | Inputs | Outputs | Position/group | Shape/treatment |
|---|---|---|---|---|---|---|

| From | To | Signal/action label | Arrow direction/style | Feedback/condition | Scientific meaning |
|---|---|---|---|---|---|

- System boundary:
- Training-only path:
- Deployment/inference path:
- Proposed components to emphasize:
- Standard/context components to de-emphasize:
- Loops, decisions, constraints, or coordinate frames:
- Details deliberately omitted:

### E3. Real-source composition — complete for `PHOTO_COMPOSITE`

| Panel/frame | Real source file | Provenance/experiment ID | Crop/viewpoint | Factual annotations | Time/phase | Redaction needed |
|---|---|---|---|---|---|---|

- Relation to quantitative data:
- Platform/site/object identity:
- Frames excluded and selection rule:
- Elements that must not be generated, replaced, or beautified:

### F. Visual encoding

- Proposed method:
- Baselines:
- Reference/target:
- Constraints/unsafe region:
- Time/order/direction:
- Line/marker/hatch redundancy:
- Labels, callouts, units, and coordinate frames:
- Accessibility/grayscale behavior:

### G. Copy-ready downstream handoff

#### For a plotting/code agent (`DATA_PLOT`)

```text
Create [exact plot subtype] from the supplied [file/table/log]. Use only the named columns and verified transformations below. [Describe panel layout, axes, series, uncertainty, events, styling, and export size.] Do not infer or fabricate missing values, error bars, seeds, units, baselines, or statistical significance. If an input is absent, stop and report it.
```

#### For an AI/vector design agent (`VECTOR_SCHEMATIC`)

```text
Create an editable IEEE-style [architecture/block/algorithm/mechanism] diagram using exactly the listed nodes, groups, arrows, labels, and layout. [Insert the complete node-edge and layout description.] Preserve all technical names and directions. Do not add modules, signals, equations, claims, hardware, or decorative elements not listed. Return editable vector output plus a preview.
```

#### For a photo/layout editor (`PHOTO_COMPOSITE`)

```text
Compose only the supplied real images/frames into the specified panel order. Apply the listed crops and factual annotations. Do not synthesize, replace, remove, or relocate experimental objects; do not create a fake platform, site, flight, trajectory, sensor output, or event.
```

- Required source bundle:
- Editable output expected:
- Preview/export expected:
- Visually flexible elements:
- Scientifically exact elements:
- Negative constraints / do not draw:

### G2. Collection and execution record

- Trial IDs and representative-run selection rule:
- Clocks/time origin/synchronization method and tolerance:
- Event/frame IDs, source files, coordinate frames and transforms:
- Sampling, units, calibration, missing-data handling:
- Scientific input readiness: `SPEC_READY` / `NOT_READY`:
- Editable draft and preview paths; executor and supplied brief/bundle:
- Execution status: `NOT_EXECUTED` / `DRAFT_RENDERED` / `VISUALLY_CHECKED` / `INDEPENDENT_HANDOFF_TESTED`:
- Final-width inspection evidence; clarification count and unresolved guesses:
- Errors found, repair and rerun result:

### H. Caption and manuscript contract

- Caption draft:
- What is shown:
- Dataset/testbed and condition:
- Panel definitions:
- Encoding definitions:
- Metric direction and uncertainty:
- Visible takeaway:
- Details delegated to main text:
- Required in-text interpretation:

### I. Missing inputs and integrity

- Available sources:
- `MISSING_INPUT`:
- `NEEDS_EXPERIMENT`:
- `NEEDS_AUTHOR_DECISION`:
- Claims this figure must not make:
- Elements that must not be invented or manually altered:

### J. Acceptance checks

- [ ] Exact subtype and rendering route are declared.
- [ ] The figure answers one identifiable scientific question.
- [ ] Every panel has a distinct evidence role.
- [ ] Data schema or node-edge/photo-source specification is complete.
- [ ] A downstream tool can execute without guessing scientific content.
- [ ] Quantitative geometry and uncertainty come from actual data.
- [ ] Physical/qualitative evidence is traceable to real sources.
- [ ] Terminology matches the manuscript, equations, algorithms, and ledger.
- [ ] Readable at final IEEE column size and in grayscale.
- [ ] Caption describes the visible evidence without overclaiming.

---

## Whole-document handoff checklist

- [ ] Every planned figure appears in the classification summary and has a full block.
- [ ] Every existing figure has a justified `KEEP`, `REDESIGN`, `MERGE`, or `DELETE` decision.
- [ ] Every new figure has a justified `ADD` decision.
- [ ] Every included figure has a manuscript-specific trigger and separates corpus prior, inspected reference, and manuscript-derived design; missing references are explicit.
- [ ] Reference papers inform only evidence roles and construction principles, with do-not-copy boundaries recorded.
- [ ] Figure order follows the manuscript argument.
- [ ] No two figures duplicate the same evidence role without justification.
- [ ] All major claims have visual/table evidence or an explicit nonvisual proof.
- [ ] Every `DATA_PLOT` has real source data and a schema.
- [ ] Every `VECTOR_SCHEMATIC` has a node-edge specification.
- [ ] Every `PHOTO_COMPOSITE` has provenance for every source.
- [ ] Missing inputs are labeled rather than fabricated.
- [ ] Visual encodings and canonical terminology remain consistent across the paper.
- [ ] Final captions and in-text interpretations are planned.
