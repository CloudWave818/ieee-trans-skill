# Figure Description Taxonomy

## Purpose

Use this reference to identify what each manuscript figure is, decide why that type fits the scientific question, and produce an executable description for a plotting agent, vector-design agent, image tool, or researcher. Classification is functional: a figure is named by the evidence relationship it communicates, not by its visual decoration.

## Rendering routes

| Route | Use for | Required source | Downstream instruction |
|---|---|---|---|
| `DATA_PLOT` | measured, simulated, learned, or computed quantitative evidence | actual data/logs plus metric definitions | generate reproducibly with plotting code; values, curves, axes, and uncertainty must come from data |
| `VECTOR_SCHEMATIC` | architecture, block diagram, mechanism, geometry, algorithm, or conceptual scenario | manuscript method, equations, notation, and interface definitions | draw editable nodes, edges, groups, and labels; no invented modules or signals |
| `PHOTO_COMPOSITE` | hardware, test site, flight sequence, onboard view, qualitative result | traceable real photos, frames, maps, screenshots, or sensor outputs | compose and annotate real sources; never synthesize evidence |
| `TABLE` | exact multi-method values, settings, components, or hardware specifications | verified values and definitions | typeset structured rows/columns with consistent units and precision |
| `NOT_READY` | source data or evidence is unavailable | approved missing-state label | describe the planned figure but do not fabricate the missing content |

## Type-selection rules

| Scientific relationship | Preferred type | Minimum specification | Common misuse |
|---|---|---|---|
| System components and signal flow | architecture/block diagram | system boundary, modules, inputs/outputs, arrows, proposed components | generic boxes with no signal labels |
| Sequential logic, decisions, or loops | algorithm flowchart/state machine | start/end, operations, decisions, branches, loop condition, notation | duplicating pseudocode without clarifying control flow |
| Training and learning progress | convergence/learning curve | x=episodes/steps/time; y=return/loss/success; seeds, evaluation cadence, center, band, smoothing | one lucky run, hidden smoothing, incompatible horizons |
| Temporal physical response | state/control/error time series | aligned time axis, variables, units, events, constraints, reference | mixing variables with incompatible scales or omitting bounds |
| Continuous stress or parameter response | robustness/sensitivity line plot | ordered stress/parameter x, performance y, method series, uncertainty | disconnected bars that hide the trend |
| Categorical method comparison | grouped bar, interval/dot plot, or compact table | categories, methods, metric direction, uncertainty, fair conditions | 3-D bars, cropped zero-based quantities, overcrowded groups |
| Component contribution | ablation bar/line/table | full method, controlled variants, claimed module, matched metric | arbitrary variants unrelated to contribution claims |
| Accuracy-cost or two-variable tradeoff | scatter/Pareto plot | x and y metrics, units, method markers, Pareto direction, resource condition | claiming dominance without comparable hardware/conditions |
| Distribution or variability | box/violin/histogram/CDF | samples, statistic meaning, n, grouping, outliers, normalization | replacing a distribution with a mean-only bar |
| Classwise error | confusion matrix/heatmap | class labels, count or normalization rule, color scale, imbalance context | raw color without values or normalization definition |
| Spatial motion or path quality | 2-D/3-D trajectory plot | coordinates/units, start/goal, direction, obstacles, reference, executed paths | decorative paths with no provenance or scale |
| Feasible set, geometry, or theoretical property | geometry/property illustration | coordinate frame, regions, boundaries, variables, theorem/property link | unlabeled conceptual shapes that imply exact geometry |
| Network/graph interaction | topology graph | node meaning, edge meaning/direction, time or communication condition | dense hairball with unstable identities |
| Hardware and implementation | annotated platform/setup figure | real source photo, relevant components, signal/hardware inset, provenance | stock photograph or labels unrelated to reproducibility |
| Physical task progression | flight/experiment sequence | ordered real frames, timestamps/phases, consistent annotations, viewpoint | attractive but untraceable snapshots |
| Perception or qualitative behavior | qualitative result panel | input, output, ground truth/reference, failure/success cases, selection rule | cherry-picked successes without context |
| Several linked evidence modes | multi-panel composite | one role per panel, coherent reading order, shared encodings, full panel caption | squeezing unrelated plots into a collage |

## Type-specific description contracts

### Architecture or block diagram

Specify canvas direction; system boundary; every node label and scientific role; group boundaries; input/output ports; arrow direction and signal labels; training-only versus deployment paths; feedback loops; proposed versus standard components; symbols that must match the manuscript; and which details must be omitted to prevent overload.

### Algorithm flowchart

Specify initialization, ordered operations, decision diamonds, branch conditions, loops, termination, returned output, and the exact variable names used in equations or pseudocode. Explain what the flowchart reveals that the algorithm listing does not.

### Training convergence curve

Specify:

- x variable: episode, environment step, optimizer step, wall-clock time, or sample count;
- y variable and direction: return, success rate, loss, constraint violation, or another named metric;
- evaluation versus training measurements and evaluation cadence;
- method/variant series and common training budget;
- number of seeds/runs, center statistic, and uncertainty band;
- smoothing window/method and whether faint unsmoothed traces remain visible;
- stopping condition, convergence criterion, and any event markers;
- axis limits or scale only when justified by the data.

Do not label a noisy single-run reward trace as convergence evidence.

### Comparison bar, dot, or interval plot

Specify category axis, method grouping, metric/unit, higher/lower direction, zero baseline where appropriate, error-bar definition, ordering, exact-value labels only when readable, and whether a table would communicate dense values more honestly.

### Robustness or sensitivity curve

Specify the stress or parameter axis with units, its tested values, fixed conditions, performance metric, method series, repeated-run uncertainty, failure threshold, and the domain beyond which no claim is made.

### Time-series response

Specify shared time base, sampling rate, state/reference/control/disturbance variables, units, constraint bounds, event markers, synchronization, selected trials, and whether the curve is representative or aggregated. Do not silently splice different trials.

### Trajectory or spatial map

Specify coordinate frame and units; 2-D/3-D view; reference, proposed, and baseline paths; start/goal; direction/time encoding; obstacles and safety envelope; agent identity; ground-truth source; and complementary projections or error panels needed to avoid 3-D occlusion.

### Scatter/Pareto plot

Specify x/y metrics and direction, units, marker identity, hardware/test condition, confidence intervals if relevant, Pareto frontier definition, and labels for points that drive the conclusion.

### Heatmap/confusion matrix

Specify row/column semantics, normalization, cell values, color scale and range, ordering, missing cells, class imbalance, and complementary metrics. Do not allow color intensity alone to encode exact results.

### Hardware/photo/flight composite

Specify every real source file and provenance; panel crop and viewpoint; chronological order; components or objects to annotate; factual labels; privacy/redaction needs; and the relation between the photo/frame and quantitative experiment. A generated platform or flight scene cannot support a real-world claim.

## Figure description decision sequence

For each proposed figure:

1. Write the exact claim and scientific question.
2. Identify the relationship that must be perceived: structure, sequence, trend, category difference, distribution, spatial behavior, physical evidence, or exact value.
3. Select the primary type and explain why it is preferable to the main alternative.
4. Select the rendering route and inventory the required source files.
5. Define every panel and ensure one panel has one evidence role.
6. For data plots, define the data schema before axes or styling.
7. For schematics, define nodes and edges before colors or icons.
8. For photo composites, establish provenance before cropping or annotation.
9. Write the copy-ready downstream handoff and negative constraints.
10. Check the result at final IEEE column size and against the caption claim.

## Using figures from reference papers

When inspecting selected papers, record the source paper/figure number, exact subtype, variables or objects shown, evidence role, panel logic, and why the pattern is applicable. Reuse only the abstract construction principle—for example, “trajectory followed by time-aligned safety-distance evidence.” Adapt generic panel organization and comparison principles to the manuscript; do not reproduce distinctive source artwork or import source data, labels, icons, photography, or scientific claims. Apply `VISUAL_DESIGN_EVIDENCE.md` and use inspected cases with exact figure/page locators; automated caption labels are not visual inspection. Preserve the exemplar's `Do Not Generalize` boundary in the project document.

## Integrity boundary

- Visual plausibility is not scientific validity.
- Never ask a generative-image model to create quantitative evidence.
- Never synthesize hardware, flight, field-site, perception, or failure evidence and present it as observed.
- Never invent axes, units, data values, error bars, seeds, statistical significance, or baseline conditions.
- When a needed input is absent, use `MISSING_INPUT`, `NEEDS_EXPERIMENT`, or `NEEDS_AUTHOR_DECISION` and keep the planned specification visible.
