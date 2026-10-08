# 14 Real-World Experiment Scene, Capture and Presentation

## Entry and scoped output

Use when the author asks what a physical experiment should look like, where/how the UAV should fly, how to photograph it, or requests detailed text for another model to illustrate it. This is a local Mode E/F task. Read the manuscript's mechanism, physical section, captions and available asset/log inventory; diagnose only fields that affect this experiment. Do not run full-paper figure counting or draw an image unless requested.

Produce one filled `../templates/REAL_WORLD_EXPERIMENT_BRIEF.md`, normally in Chinese for this user. It must include a concrete recommended scene, flight/event sequence, capture plan, publication layout and a self-contained copy-ready description. A list of possible indoor/outdoor settings or a blank template is not completion. Use clearly proposed dimensions/positions when measured ones are unavailable, or normalized positions when a site has not been selected. Explain which choices require later site/vehicle feasibility checks; this is not a flight authorization or an executed test.

## 1. Establish the scientific job

Map `claim → physical question → controlled condition → observable event/metric → scene/capture → figure`. Separate execution feasibility, task success, mechanism validation and comparative advantage. Tracking a planned trajectory alone does not validate an observer's inference, collision avoidance, perception or task success.

Read the local source section before choosing a visually dramatic scene. No obstacles is a valid recommendation when obstacles do not test the mechanism. Do not add gates, chasing people, occlusion, forests, formation changes or aerobatics because a donor figure contains them. State a primary plan and a materially different alternative only when it answers another question. For a proposal, say what a negative result would change in the claim.

## 2. Retrieve actual physical cases

Read `../references/preferred_29/real_world_scenes/INDEX.md` and `PLAYBOOK.md`; select one to three cases by task and evidence role. Consult the selected records in `cases.json`, inspect the indicated bundled PDF pages, and read the nearby experimental text and caption. Record paper ID, PDF version/hash, one-based PDF page and figure number, the observed construction, transferred element and limit. The new scene records control physical-source classification when an older generic figure card disagrees. A reference supplied only as a summary must be labeled summary-based; do not claim fresh image inspection.

Classify evidence at figure/panel level: actual hardware flight, nonflight hardware, real recorded dataset, simulation, renderer or unknown. A photograph-like appearance, platform photograph or timing on a compute board is not by itself a physical closed-loop flight trial. Multiple vehicles in one picture can be simultaneous agents, samples of one flight, multiple independent trials registered afterwards, or a rendered model. Determine which, or keep it unknown. Do not infer long-exposure photography from the appearance of sequential snapshots.

## 3. Describe the scene as an executable spatial plan

Record separately `AUTHOR_EVIDENCE`, `PROPOSED_EXPERIMENT` and `ILLUSTRATIVE_LAYOUT_ASSUMPTION`. Source facts remain source facts; proposed values never become measured facts or verified platform limits. Distinguish experiment duration from takeoff/landing/capture lead-in, observed peak speed from a hard constraint, and simulation space from the physical venue.

Describe indoor/outdoor, site type, floor/ground, light, background, available tracking/localization and why this environment isolates the scientific question. Give a top-down coordinate convention and an object table: dimensions or normalized positions, start/goal/target, physical obstacles, moving objects, virtual constraints, cameras, platform count and identities. State obstacle count, material, shape, height, spacing and the gap to traverse when relevant. For a deliberate obstacle-free trial say so explicitly, including where floor markers and nonphysical annotation belong. Do not turn plotted goal candidates or a virtual safety boundary into physical barriers.

Give a time/event table covering setup/initial state, motion onset, decision/turn/avoidance/interception/reconfiguration events that actually belong to the task, end condition and capture stop. Describe the path with direction, relative bend, height behavior and target relation; derive a measured path from logs, and call an imagined path schematic. Specify method comparison and controlled scene/goal/task conditions. Do not prescribe guessed numerical waypoints as the author's optimized solution.

Inspect initial/final velocity as well as position before describing takeoff, hover or landing. A record may be a moving measurement window needing separate entry/braking segments. Shared start/end positions and duration do not establish common state boundary conditions; disclose differing initial/final motion states, and limit a comparison to execution when they confound factor attribution. A proposed common-boundary test needs newly verified reference trajectories, not a relabeled picture.

## 4. Choose capture and presentation together

Choose a primary camera view that reveals the mechanism: side for height/clearance, oblique for spatial context, overhead for planar path comparison, onboard for a perception claim. State camera position/elevation/view direction, field of view and visible fixed objects; illustrative viewpoints may use normalized composition coordinates instead of invented camera calibration. Add a second view only to resolve a scientific ambiguity. Describe the platform relative size and trajectory occupancy in the final panel.

Select one presentation and explain its advantage:

- One flight / one fixed camera: actual frame composite for motion progression, plus measured trajectory/state where needed.
- Several methods: aligned separate panels with identical viewpoint, world geometry, scale and representative-run rule. Alternative: one measured-trajectory comparison with method legend. Do not depict independent runs as simultaneous drones in a real scene.
- Event-dependent task: ordered timestamped frames, then synchronized state/error/distance trace. Frames need not be equally spaced if event timing is the question.
- Several real flights: registered trial trajectories or maps, explicitly called multiple trials; not a same-flight pose sequence.
- Swarm: stable agent IDs and selected common instants; distinguish same-agent time ghosts from different physical agents.
- Sim-to-real: label every row/panel, including generated-view rows, and compare the same task conditions where available.

For a real composite require trial ID, original frame/time, camera clock/log clock/zero point, synchronization method/tolerance, coordinate transform/calibration and representative-run rule. A context photo without authenticated trial mapping can show the venue/platform only; keep it separate from the trial-specific measured path. Mark the real composite NOT_READY when these central inputs are missing while still completing the proposed capture specification.

## 5. Specify the motion treatment

Give exact frame selection by timestamps or events; do not universally impose four-to-six frames. Specify which is the latest/current UAV and how earlier silhouettes progress in opacity, e.g. a clearly proposed 25/40/60/80/100% schedule. Draw every real pose only from its actual frame, with retained occlusions and background registration. For a planning illustration an assumed path and ghost poses may be described, but label the whole image illustrative and do not imply an actual observation.

Explain the requested “虚化” concretely: historical instances may be less opaque and mildly desaturated while the current instance remains crisp. Record that as display processing. A planning illustration may use a specified faint blur/trail; actual evidence keeps identifiable real frame silhouettes and does not generate intermediate poses or use blur to conceal missing registration. Do not equate ghosting with a verified long-exposure capture process.

Give the path source, thickness at print size, line/dash/arrow treatment, method/time/speed meaning and legend. Use one primary color meaning per trajectory: a time gradient cannot simultaneously encode algorithm identity or speed. A speed colorbar needs actual values and units. A subtle illustrative glow may improve legibility but is not uncertainty, measured light, speed or a confidence envelope; default to a crisp line for evidence. State whether a “trail” is an annotation, genuine exposure or sequential-frame composite. Never reproduce a donor's asserted interval as the new camera's measured interval.

## 6. Lock the publication layout

Apply workflow06 §6a: actual template single/full width; if unknown, explicit provisional sizes. Choose span separately from landscape/square/portrait. Give final width × height mm, panel bounding boxes or relative percentages, reading order, gutters, legend/label location, minimum final font and line sizes. A wide scene plus vertically stacked compact state plots, a single-column portrait event sequence, or paired algorithm panels are all valid. Do not default every physical figure to a wide horizontal strip. Avoid shrinking complex spatial detail into one column.

Give two count decisions when useful: how many figures for the experiment, and how many panels inside each. A photo, trajectory and time trace may jointly answer one question; several algorithms do not automatically require several figures. Specify what would make the plan split or merge. Describe caption content and the visible, supported takeaway.

## 7. Deliver a self-contained external-model handoff

Select the handoff purpose independently of the rendering route:

- `PROPOSED_SCENE_ILLUSTRATION`: a model may illustrate the proposed environment, schematic route and pose sequence. Say “proposed experiment / illustrative scene” in the handoff and image caption. It may have realistic materials and perspective, but is not a replacement for a real experimental photograph or measured results. Route as a planning illustration/schematic; no new global evidence-rendering route is needed.
- `REAL_EVIDENCE_ASSEMBLY`: a layout/image editor uses only the supplied real frames/photos and a reproducibly plotted path from actual logs. Route panels through PHOTO_COMPOSITE/DATA_PLOT. Specify the source bundle and missing dependencies. Do not synthesize intermediate poses, scene objects or measurements.

Write a complete natural-language block containing the purpose, scientific task, environment, platform count, object positions, motion/time sequence, viewpoint, panel structure, dimensions, labels, trajectory/opacity encodings and permitted changes. Do not rely on “imitate R05,” inaccessible local files or an external template for critical facts. State source references outside the handoff for traceability and spell out the transferable construction inside it. If both purposes are useful, give separately labeled blocks; do not mix them into an ambiguous photorealistic “experiment result.”

If an evidence-assembly handoff includes data panels, also copy their exact fields/units, time-zero definition, alignment/interpolation policy, metric formula/weighting, valid-window and missing-trial rules into that block (workflow06/template E1 supplies the full plotting contract). Include representative-trial selection and exactly which planned/measured line belongs on a photo. A complete rule elsewhere in the brief does not fix an ambiguous standalone prompt. Mechanism parameters also need their actual meaning; do not turn a generic progress parameter into arc length or constant physical speed.

## Exit and acceptance

Read the output as the downstream recipient. Can they place every essential object, understand how many actual UAVs there are, follow the task, choose the view, lay out the figure at print size and know which objects/paths are assumed versus measured? If not, revise the actual description. Keep operational capture dependencies visible without drowning the main visual description in audit language.

Record description completeness, experiment execution, source readiness, rendering and independent handoff separately. A finished text/spec is not a finished experiment, image or visual-quality check. For a description-only request the completed local brief is the deliverable; no full-paper PAPER_FIGURE_DESCRIPTION, unrelated blueprint, new figure or compilation is required.
