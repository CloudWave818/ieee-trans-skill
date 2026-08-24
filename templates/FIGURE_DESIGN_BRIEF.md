# Figure Design Brief

## Identity and evidence

- Figure ID / proposed number:
- Working title:
- Related section and first in-text citation:
- Core claim defended:
- Scientific question answered:
- Evidence role:
- Priority: `MANDATORY` / `CONDITIONAL`
- What the paper loses if removed:

## Final layout

- Figure type: architecture / algorithm / scenario / trajectory / time series / comparison / robustness / hardware / flight sequence / composite / other
- Target width: one-column / two-column / page-wide
- Target aspect ratio:
- Panel grid and reading order:
- Shared legend/axis strategy:
- Minimum final text size:

## Drawing specification

### Global composition

Describe the full canvas from left to right and top to bottom. State the visual hierarchy and the first element the reader should notice.

### Panel specification

| Panel | Purpose | Objects/data shown | Axes/units or spatial layout | Encoding and annotations | Data/source dependency |
|---|---|---|---|---|---|

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

## Acceptance checks

- [ ] Supports one identifiable claim.
- [ ] Every panel has a distinct evidence role.
- [ ] Readable at final IEEE column size.
- [ ] Axes, units, legends, symbols, and panel labels are complete.
- [ ] Baseline comparison and uncertainty are fair where applicable.
- [ ] Photos, screenshots, and trajectories are traceable to the experiment.
- [ ] Simulation and physical evidence cannot be confused.
- [ ] Caption explains the figure without overstating the evidence.
- [ ] A researcher or designer can draw the figure without guessing scientific content.
