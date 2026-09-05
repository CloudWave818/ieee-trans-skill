# 06 Full-Paper Visual Architecture and Figure/Table Design

## Entry

Require a provisional claim–evidence matrix. Use for Mode F or before a full Paper Blueprint. If claims are not stable, produce a provisional visual architecture and label evidence gaps; do not guess results.

## Required output levels

Produce all three levels unless the user explicitly asks for only one figure.

1. **Full-paper visual architecture** — how many figures/tables are justified, which roles are mandatory or optional, and how Fig. 1 through Fig. N carry the paper's argument.
2. **Consolidated figure-description document** — one project-level `PAPER_FIGURE_DESCRIPTION.md` containing the figure inventory and a complete, AI-readable specification for every planned figure.
3. **Per-figure drawing briefs** — optional standalone extractions precise enough for the author, a plotting agent, a vector designer, or another tool to execute without inventing scientific content.

## Procedure

### 0. Inventory existing and missing visuals

Read the manuscript, captions, figure/table callouts, supplied image files, and result artifacts. For every current or proposed item, record `EXISTING` or `PROPOSED` and assign `KEEP`, `REDESIGN`, `MERGE`, `DELETE`, or `ADD`. Do not discard a scientifically correct existing figure merely because another style is possible.

### 1. Establish the visual evidence contract

For each major claim, record:

`claim → required evidence → experiment/source → metric/observation → visual asset`

For every proposed asset also record:

`CORPUS_PRIOR (when applicable) + INSPECTED_REFERENCE (when available) + manuscript claim/evidence trigger → include/omit decision`

Read `../references/VISUAL_DESIGN_EVIDENCE.md`. For UAV figures first read `../references/preferred_29/STYLE_PLAYBOOK.md` and retrieve preferred cards with `scripts/query_visual_cases.py`; use the older `../references/visual_cases/INDEX.md` only to supplement missing relationships. The manuscript trigger is required; for title-only requests state provisional assumptions and produce concrete plans/sketches immediately. A 100-paper corpus rule ID supports scale or role only. Permit `MANUSCRIPT_DERIVED` construction with explicit rationale when no reference matches; do not fabricate a reference. Record `NO_MATCHING_INSPECTED_REFERENCE` where appropriate.

Do not plan figures from section titles alone. A method contribution normally needs a mechanism view; a performance claim needs a fair comparison; a real-time claim needs runtime/resource evidence; a UAV deployment claim needs platform and flight evidence.

### 2. Classify the paper and figure types

Classify the paper before estimating the count:

- theory/control-led;
- algorithm/RL-led;
- navigation/trajectory-led;
- multi-agent or swarm-led;
- UAV system/physical-validation-led;
- hybrid method-system.

Read `../resources/IEEE_TRANS_KNOWLEDGE/04_VISUALS/FIGURE_ARCHITECTURE.md`, `FIGURE_TYPES.md`, and `VISUAL_SEQUENCE.md`, plus `../references/FIGURE_DESCRIPTION_TAXONOMY.md`. For UAV work, also read `../references/UAV_VISUAL_PLAYBOOK.md`; for learning-based work read `../references/preferred_29/RL_FIGURE_PLAYBOOK.md`. Use routed journal/domain exemplars for evidence burden, while the preferred 29 control the requested visual style. Record the exact source figure/page and deliberately adapt its palette relationships, pictogram grammar, grouping, connectors and panel organization. Redraw with manuscript objects and implemented interfaces; do not pass reference photographs, measured curves or scientific mechanisms off as the author's evidence. Source venue does not restrict visual-reference eligibility.

Classify every planned asset by:

- primary family: conceptual/schematic, quantitative, spatial/trajectory, physical/qualitative, composite, or table;
- exact subtype: e.g., architecture block diagram, algorithm flowchart, grouped bar chart, convergence curve, robustness curve, time-series response, Pareto scatter, heatmap, 2-D/3-D trajectory, hardware photograph, or flight sequence;
- rendering route: `DATA_PLOT`, `VECTOR_SCHEMATIC`, `PHOTO_COMPOSITE`, `TABLE`, or `NOT_READY`.

Select the type from the variable and scientific question, not from visual fashion. Continuous ordered x variables normally require curves; categorical comparison requires bars, interval/dot plots, or tables; distributions require box/violin/CDF views; spatial motion requires trajectories; system logic requires block or flow diagrams.

### 3. Recommend a count range, then a working count

Report:

- corpus anchor with eligible population and uncertainty;
- minimum defensible count;
- recommended working count;
- expansion conditions;
- merge/delete conditions.

For the current UAV A-level corpus, the planning anchor is median 10 figures, IQR 8–15, not a quota. Let claim count, experiment breadth, physical validation, and journal/page budget determine the recommendation. Never answer only “about ten figures.”

### 4. Build the figure-role inventory

Choose only roles required by the claims:

1. problem/motivation or visual abstract;
2. system boundary and task scenario;
3. overall method/closed-loop architecture;
4. key mechanism, network, controller, or algorithm flow;
5. theory/feasible-region/property illustration;
6. simulation/test scenarios and protocol;
7. main quantitative comparison;
8. representative trajectory or qualitative behavior;
9. tracking/state/control/safety curves;
10. ablation or mechanism verification;
11. robustness, generalization, disturbance, or failure cases;
12. runtime/resource/scalability tradeoff;
13. hardware platform and sensor/computation stack;
14. real flight sequence, onboard view, mapping, or physical trajectory.

Mark each role `MANDATORY`, `CONDITIONAL`, or `OMIT` and give the reason.

### 5. Sequence the argument

Prefer:

`problem/task → system/setup → method overview → mechanism → protocol → main result → behavior/trajectory → stress/boundary evidence → hardware/real-world closure`

Change the order when the journal or paper type justifies it. Place setup before results that cannot be interpreted without it. Place real-world evidence late enough to close the simulation-to-deployment argument, but cite the platform earlier when implementation details affect the method.

### 6. Produce the consolidated description and briefs

Copy `../templates/FIGURE_TABLE_PLAN.md`, then create one `PAPER_FIGURE_DESCRIPTION.md` from `../templates/PAPER_FIGURE_DESCRIPTION.md`. For every figure, complete the corresponding document block and optionally extract `../templates/FIGURE_DESIGN_BRIEF.md`. Specify:

- one-sentence claim and scientific question;
- figure type and final one-/two-column placement;
- exact panel grid and reading order;
- objects, modules, signals, arrows, coordinate frames, obstacles, maps, vehicles, or photos;
- x/y/z variables, units, sampling/aggregation, transformations, axis ranges when known, metrics, baselines, and uncertainty;
- semantic color, marker, line-style, photo annotations, and trajectory encodings;
- data/file dependencies and missing items;
- caption contract and in-text interpretation;
- what is lost if removed;
- drawing and final-size QA checks.

For a data figure, give the expected input-data schema and plotting specification. For a schematic, give the exact nodes, groups, edges, arrow directions, labels, and layout. For a photo composite, list the real source files, viewpoints, cropping, ordering, and factual annotations. Include a copy-ready downstream handoff block, but never allow the downstream system to fabricate scientific evidence.

Use `MISSING_INPUT`, `NEEDS_EXPERIMENT`, or `NEEDS_AUTHOR_DECISION` instead of inventing content.

For key mechanism and composite figures, add a layout sketch with panel proportions and an explicit bottleneck → changed operation → observable consequence chain. Specify collection fields, clocks, synchronization tolerance, event IDs and representative-run selection before experiments. See the evidence reference for the full contract.

### 7. UAV-specific hard check

For UAV papers, explicitly answer:

- Is the platform itself visible and annotated?
- Is the environment/test site visible?
- Is actual flight shown externally, onboard, or both?
- Is the executed path distinguished from reference, baseline, target, obstacles, and safety envelope?
- Are position, velocity, attitude, control input, error, and minimum distance time-aligned where claimed?
- For swarms, are agent identity, formation topology, time order, collisions/near misses, and minimum separation readable?
- Are simulation and real-world panels unmistakably labeled?
- Can photos and trajectories be traced to the stated experiment?

If physical validation is claimed but none of platform, flight, or physical trajectory evidence is planned, mark `CLAIM_WITHOUT_EVIDENCE`.

### 8. Remove redundancy

Ask for every asset: “What does this prove?” and “What is lost if it is removed?” Merge or demote assets with duplicate answers. Do not use a plot and table to repeat identical numbers unless one gives exact values and the other reveals a distinct pattern.

## Format decisions

- Use figures for spatial, temporal, architectural, distributional, behavioral, or qualitative relationships.
- Use tables for exact multi-method/multi-metric values, configurations, hardware specifications, and compact comparisons.
- Prefer two-column width for dense architecture, more than two panels, multi-agent trajectories, or photo-plus-plot composites.
- Plan captions to state object, condition, encoding, metric, comparison, and visible takeaway without overstating causality.
- Treat column span, typography, panel count, and export type as explicit design decisions.

## Integrity

Do not create a graph before defining the experiment and evidence need. Do not imply unavailable error bars, significance, hardware, flight tests, disturbance cases, or scenarios. Do not use a generic “neural network” block to hide the closed-loop system. Do not show a decorative UAV photograph that is unrelated to the experiment. Do not send a quantitative result plot to a generative-image model as if plausible geometry were valid data; route it to reproducible plotting from actual source data.

## Exit

Pass G5 only when:

1. the total visual budget is justified;
2. every major claim maps to at least one suitable visual/table or an explicit nonvisual proof;
3. every planned asset has a unique evidence role, real data dependency, section home, and nonredundant caption function;
4. one consolidated `PAPER_FIGURE_DESCRIPTION.md` exists;
5. every figure has an executable drawing or plotting specification, rendering route, and copy-ready handoff block;
6. UAV physical/flight claims pass the UAV-specific hard check.

This passes specification readiness only (`SPEC_READY`) for the explicitly scoped, executable artifact/panels. Returning a useful `PROVISIONAL` gap-bearing plan does not close G5. For mixed composites, specify each panel's rendering route; an available mechanism may be rendered as a planning draft while missing empirical panels and the full evidence figure remain NOT_READY. Record rendered preview, final-size inspection and independent handoff separately. Never infer those statuses from G5 or a validation script.
