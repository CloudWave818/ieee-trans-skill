# UAV Visual Playbook

## Purpose

Use this reference to plan the complete visual argument of a UAV/autonomous-flight Transactions paper and to write executable figure briefs. It does not require every paper to contain every listed figure.

## Corpus anchor and limits

The 35 A-level papers classified primarily as UAV autonomy contain a median of 10 figures, IQR 8–15, observed range 2–23. The caption classifier identifies at least 61 quantitative-result, 48 scenario, 45 trajectory, 24 problem, 17 method-framework, and 10 explicit real-world figure entries across these papers. Because 244 entries remain unclassified, these are conservative lower bounds, not complete prevalence estimates.

Use 8–15 figures as an initial long-paper planning band, then adjust by claim count, paper type, physical validation, multi-agent complexity, and target-journal page budget. Do not use ten figures as a quota.

## Recommended UAV visual architecture

| Argument stage | Candidate visual | Include when | Minimum content |
|---|---|---|---|
| Problem | Task/scenario or motivating failure | geometry, constraints, or failure mode is not obvious | UAV, environment, target, obstacles, constraints, coordinate frame |
| System | Closed-loop system boundary | perception, planning, learning, and control interact | sensors → estimator → planner/policy → controller → UAV/environment feedback |
| Method | Overall architecture | more than one proposed module or train/deploy path | proposed modules, data/signals, training and deployment distinction |
| Mechanism | Algorithm/controller/network detail | the novelty is internal rather than only system-level | variables consistent with equations/pseudocode; loops and decisions |
| Protocol | Simulation/physical scenario matrix | several environments, disturbances, or task variants are tested | map/site, obstacles, initial/goal states, wind/communication/sensing conditions |
| Main evidence | Quantitative comparison | superiority or efficiency is claimed | fair baselines, primary metric, uncertainty/repeats, condition labels |
| Behavior | 2-D/3-D trajectory or time-lapse | path quality, formation, avoidance, tracking, or safety is claimed | reference/target, executed paths, baselines, direction, start/end, obstacles |
| Dynamics | State/error/control time series | tracking, stability, smoothness, constraint satisfaction, or control effort is claimed | aligned time axis; position, velocity, attitude, error, input, bounds as needed |
| Boundary | Robustness/generalization/failure | wind, noise, delay, dropout, unseen scene, or safety claims are made | stress axis/conditions, negative or failure cases, safety margin |
| Deployment | Platform/setup figure | a physical, onboard, real-time, or deployment claim is made | platform photo, sensors, onboard computer, communication, control rate/test site |
| Closure | Real-flight sequence plus physical trajectory | real flight is a central contribution | external snapshots, optional onboard view, time order, executed trajectory, quantitative closure |

## Practical working counts

Select from these patterns; explain every deviation.

### UAV method or learning paper without physical flight

Usually 8–11 figures:

1. problem/task;
2. method overview;
3. key network/controller mechanism;
4. training/deployment or algorithm flow;
5. scenarios/protocol;
6. main comparison;
7. trajectories/qualitative behavior;
8. state/error/control curves;
9. ablation;
10. robustness/generalization;
11. runtime/sensitivity when claimed.

### UAV system paper with physical flight

Usually 10–14 figures:

1. motivating task or teaser;
2. system/closed-loop architecture;
3. core method;
4. key mechanism;
5. simulation and physical protocol;
6. main simulation comparison;
7. simulation trajectories;
8. robustness/disturbance evidence;
9. platform and onboard stack;
10. test site/environment;
11. external flight sequence and onboard view;
12. real-flight trajectory;
13. real-flight state/error/control curves;
14. failure/safety/runtime closure when claimed.

### Multi-UAV/swarm paper

Usually 10–14 figures. Add topology/communication, agent identity, time-ordered formation behavior, minimum-separation evidence, scaling with swarm size, and failure/reconfiguration cases. Avoid unreadable “spaghetti” trajectories; use time stamps, small multiples, or selected-agent views.

### Theory/control-led UAV paper

Usually 6–10 figures. Favor property/feasible-region illustration, controller architecture, representative trajectory, tracking/constraint curves, robustness conditions, and one implementation or case-study figure. Do not force photographs when the claim is explicitly theoretical.

## UAV figure construction rules

### Platform/setup figure

- Show the actual platform used, not a generic stock UAV.
- Annotate only components that affect the method or reproducibility: camera/LiDAR/UWB/IMU, onboard computer, radio, payload, propulsion, ground truth, and ground station.
- Pair the photograph with a compact signal/data-flow diagram when hardware and software responsibilities matter.

### Flight sequence

- Use four to six ordered frames with timestamps or phase labels.
- Keep the camera viewpoint stable when possible.
- Mark UAV, target, obstacles, reference state, or safety boundary consistently.
- Add an onboard/FPV row only when perception or visual servoing is part of the claim.
- Do not use photographs as decoration; the sequence must show task progress, avoidance, tracking, reconfiguration, or recovery.

### Trajectory figure

- Distinguish reference/target, proposed method, baselines, and obstacles by color plus line/marker redundancy.
- Mark start, goal, direction, time or speed encoding, and coordinate units.
- For 3-D trajectories, include a readable view angle and, when occlusion matters, top/front/side projections or an inset.
- For real flight, say how trajectory ground truth was obtained and label the panel `real-world`.

### State/control curves

- Align position, velocity, attitude, error, control input, and disturbance by time.
- Draw constraint/safety bounds explicitly.
- Use consistent event markers for takeoff, disturbance, avoidance, target change, and landing.
- Avoid many tiny axes; group only variables that share scale and interpretation.

### Swarm/formation figure

- Keep agent IDs and colors stable across panels.
- Show formation topology separately when edges would obscure trajectories.
- Pair qualitative time-lapse motion with minimum-distance, collision count, formation error, or success-rate evidence.
- Include scaling or communication-cost evidence when the claim mentions scalability or distributed operation.

## Visually inspected corpus examples

Use these only as role examples, never as layouts to copy.

| Paper ID | Figure(s) | Reusable evidence role |
|---|---|---|
| P059, TIM 2023 | Fig. 14–17 | outdoor flight snapshots → real 3-D trajectory → velocity → attitude closure |
| P109, TAES 2026 | Fig. 8–12 | external tracking sequence + onboard FPV → UAV/target trajectories → prediction errors |
| P017, TASE 2025 | Fig. 7–9 | real quadrotor tasks under wind and dense obstacles with onboard views and measured trajectories |
| P048, TIE 2026 | Fig. 6 | platform/site photographs + map/trajectory + explored-volume curves in one composite |
| P082, TRO 2025 | Fig. 10–12 | swarm hardware setup and architecture → time-lapse multi-agent safety tasks + minimum-distance plots |
| P094, TSMCS 2023 | Fig. 15–18 | annotated DJI M100 platform → software/data flow → inspection trajectory/point cloud → estimation curves |

## Mandatory output for a planned UAV figure

Do not return only a title. State:

1. claim and scientific question;
2. exact panel count and geometry;
3. objects, axes, variables, units, and conditions;
4. platform/photo viewpoint and annotations when physical;
5. trajectory, color, marker, time, and safety encodings;
6. source data and missing inputs;
7. caption content and visible takeaway;
8. final column size and readability checks.

## Integrity boundary

Use `MISSING_INPUT` or `NEEDS_EXPERIMENT` for absent photos, logs, ground truth, repeated trials, safety distances, or control variables. A visually convincing simulated UAV scene is not real-world evidence. A platform photo alone is not a flight test. A trajectory without provenance is not proof of physical execution.

## Traceability

Statistics come from `../resources/IEEE_TRANS_KNOWLEDGE/00_META/PAPER_ANATOMY.csv` and `../resources/IEEE_TRANS_KNOWLEDGE/00_META/FIGURE_CATALOG.csv`. Example figure numbers were checked against rendered source pages. Automated categories are conservative and must not be treated as exhaustive.
