# Figure Design Brief

## Identity and evidence

- Figure ID / proposed number:
- Working title:
- Related section and first in-text citation:
- Core claim defended:
- Scientific question answered:
- Evidence role:
- Corpus prior and support scope (if applicable):
- Inspected case / figure / PDF page, or `NO_MATCHING_INSPECTED_REFERENCE`:
- Preferred-29 construction to imitate (palette / groups / pictograms / connectors / panels), and the manuscript-specific replacement:
- Manuscript trigger; `MANUSCRIPT_DERIVED` rationale if no reference matches:
- Primary family and exact subtype:
- Rendering route: `DATA_PLOT` / `VECTOR_SCHEMATIC` / `PHOTO_COMPOSITE` / `TABLE` / `NOT_READY`
- Priority: `MANDATORY` / `CONDITIONAL`
- What the paper loses if removed:

## Final layout

- Figure type: architecture / algorithm / scenario / trajectory / time series / comparison / robustness / hardware / flight sequence / composite / other
- Publication span: `SINGLE_COLUMN` / `DOUBLE_COLUMN` / `PAGE_WIDTH`
- Final width × height, mm; template source or provisional assumption:
- Why this span; compact arrangement considered:
- Target aspect ratio and landscape/square/portrait shape (independent of span):
- Panel grid and reading order:
- Shared legend/axis strategy:
- Minimum final text size:
- Layout sketch for key mechanism/composite figure:
- Bottleneck → changed operation → observable consequence → validating experiment:

## Drawing specification

### Global composition

Describe the full canvas from left to right and top to bottom. State the visual hierarchy and the first element the reader should notice.

### Panel specification

| Panel | Purpose | Objects/data shown | Axes/units or spatial layout | Encoding and annotations | Data/source dependency |
|---|---|---|---|---|---|

### Input-data schema for `DATA_PLOT`

| Field/column | Meaning | Unit | Role (x/y/group/facet/error/annotation) | Filtering/aggregation | Source file |
|---|---|---|---|---|---|

- Plot statistic and uncertainty:
- Runs/seeds/folds:
- For RL: training vs fixed evaluation metric; reward version; environment-step/update/wall-clock budget; pretraining/adaptation cost; independent-seed vs parallel-environment distinction:
- Smoothing or transformation, if justified:
- Required reference lines/bounds/events:

### Node-edge schema for `VECTOR_SCHEMATIC`

| ID | Node/group label | Scientific meaning | Inputs | Outputs | Position/group | Visual treatment |
|---|---|---|---|---|---|---|

| From | To | Arrow/signal label | Direction/style | Scientific meaning |
|---|---|---|---|---|

### Visual grammar

- Proposed method color/line/marker:
- Recent baseline color/line/marker:
- Traditional baseline color/line/marker:
- Reference/target trajectory:
- Obstacles/unsafe region/safety envelope:
- Time order or flight-phase encoding:
- Coordinate frames and orientation:
- Required labels, callouts, arrows, and units:
- Grayscale redundancy:

## UAV/hardware/flight specification

Complete when applicable.

- Platform model and visible components:
- Sensor, computer, communication, and actuator annotations:
- External camera viewpoint and flight phases:
- Onboard/FPV/perception inset:
- Environment, obstacles, target, wind/disturbance, and safety boundary:
- Reference path, executed path, baselines, start/end points, and direction arrows:
- For swarms: agent IDs, formation topology, time stamps, and minimum separation:
- Time-aligned position/velocity/attitude/control/error panels:
- Simulation/real-world label and photo provenance:

## Data and integrity contract

- Source files:
- Experiment/scenario ID:
- Methods/baselines:
- Metric definitions and direction:
- Runs/seeds/repeats:
- Center and uncertainty:
- Missing information:
- Elements that must not be invented or manually altered:

## Caption contract

- What is shown:
- Testbed/scenario and condition:
- Panel definitions:
- Encoding definitions:
- Metric/direction:
- Visible takeaway:
- Details delegated to main text:

## Downstream AI/designer handoff

- Copy-ready task specification:
- Required source files/data:
- Elements that may be visually optimized:
- Elements that must remain exact:
- Negative constraints / do not draw:
- Expected editable output:
- Locked publication span, final width × height, panel grid and final font/line sizes:
- Manuscript insertion environment/control and width expression:

## Acceptance checks

- [ ] Supports one identifiable claim.
- [ ] Every panel has a distinct evidence role.
- [ ] Readable at final IEEE column size.
- [ ] Brief, export and manuscript placement use the same span/physical size; pending execution stages are stated.
- [ ] Axes, units, legends, symbols, and panel labels are complete.
- [ ] Baseline comparison and uncertainty are fair where applicable.
- [ ] Photos, screenshots, and trajectories are traceable to the experiment.
- [ ] Simulation and physical evidence cannot be confused.
- [ ] Caption explains the figure without overstating the evidence.
- [ ] A researcher or designer can draw the figure without guessing scientific content.

## Capture and execution

For time-aligned composites, record trial IDs, representative-run selection, clocks/zero point, synchronization method/tolerance, frame/event IDs, units and coordinate transforms. See `references/VISUAL_DESIGN_EVIDENCE.md`.

For a real-world UAV scene/flight brief, use [workflow14](../workflows/14_REAL_WORLD_SCENE_AND_CAPTURE.md) and embed or link the filled [scene template](REAL_WORLD_EXPERIMENT_BRIEF.md). State indoor/outdoor, obstacle/no-obstacle reasoning and placement, flight/events, camera view, temporal/comparative treatment and final panel dimensions. Give a self-contained proposed-scene illustration handoff separately from real-source evidence assembly; a description-only request stops at the complete text specification.

Record specification readiness, actual editable draft/preview, final-width inspection, and independent handoff separately. Include execution questions, scientific guesses and repairs. Never call an unrendered brief visually checked.
