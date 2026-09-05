# From inspected figures to executable manuscript figures

Read this for Mode F. Retrieve UAV cases from `preferred_29/INDEX.md` first, supplementing with `visual_cases/INDEX.md` by the scientific relationship (uncertainty propagation, causal intervention, synchronized motion, safety-versus-progress), not only by the word “trajectory.” These are bounded visual layers; the original automated caption catalog remains unchanged.

## Three evidence layers

1. **CORPUS_PRIOR**: a count, frequency, or role from the registered corpus. It supports a scale or role decision, not a panel geometry, chart type, or causal interpretation.
2. **INSPECTED_REFERENCE**: paper ID/DOI, figure, one-based PDF page, inspected image, caption and nearby body discussion. State the observed construction, reusable relationship, manuscript adaptation, and limits. A rendered page or caption-only candidate is not an inspected reference.
3. **MANUSCRIPT_DESIGN**: exact manuscript location, scientific question, variables and source artifacts. This layer is mandatory. A new construction is allowed without a matching corpus ID; record `MANUSCRIPT_DERIVED`, the rationale, alternative considered, and validation needed. Never present it as a corpus finding.

An absent reference means `NO_MATCHING_INSPECTED_REFERENCE`, not “the literature has no such figure.” It does not block a scientifically justified design. Missing result data blocks execution, not provisional planning. Deliberately imitate the user's preferred palette relationships, grouping, pictogram style, connectors and panel composition, redrawing the manuscript's actual objects and operations. Keep reference images in the learning library; do not present source photographs, measured curves or claims as the new paper's evidence.

## Review a source figure

Open the actual page at readable resolution. Check the caption against the visible number and panels, then read the paragraphs interpreting that figure. Automated callout matching can mistake a sentence beginning “Fig. 8 shows…” for a caption.

Record observations separately from design inferences:

- source locator and local image link; review scope and unresolved text;
- panel count, relative areas, reading order, axes/units, series, symbols, reference/threshold lines, inset and legend sharing;
- which panels belong to the same trial, time range or population, and what is unknown;
- body-supported scientific purpose, what the figure cannot establish, and figure-specific weaknesses;
- reusable construction and the manuscript conditions needed to use it;
- data collection required to recreate the relationship using the author's own evidence.

Use `CAPTION_ONLY`, `RENDERED_NOT_REVIEWED`, `VISUALLY_INSPECTED`, or `VISUAL_AND_CONTEXT_REVIEWED`. AI inspection is identified as AI inspection; never call it human review. Reviewing one figure does not certify its paper's other figures. Preserve the raw caption catalog rather than silently upgrading all entries. For a conflict in a particular figure’s panel count or construction, prefer its visually inspected case for that exact PDF version and record the discrepancy; do not silently recompute corpus-wide statistics from this selected sample.

## Mechanism specificity

Before drawing a method diagram, write:

`baseline bottleneck → changed operation → input/output or decision change → observable consequence → validating experiment`

Draw the changed operation inside the flow, not just a colored box bearing a new module name. Label the actual signals and where they enter the controller, planner or policy. Distinguish training, inference and physical feedback. State whether a mechanism arrow is implemented, hypothesized, or merely an explanation. Apply the rename test: if changing module names alone makes the diagram fit an unrelated paper, expose the missing operation or decision boundary.

## Layout and collection contract

For key mechanism and composite figures include a small ASCII, SVG or native-shape layout sketch. Empty axes and labeled panels are sufficient; a sketch must not invent result curves. State final dimensions, relative panel areas, alignment and shared legend. Convert drawing units to final font points: `font_pt = font_units × width_mm / viewBox_width × 72 / 25.4`. Check the longest real node/edge labels at that size; allow wrapping or a documented layout adjustment rather than silently shrinking below the stated minimum. Adapt these to the content rather than impose one universal grid.

For cross-modal panels record trial ID, clocks, time origin, synchronization method and tolerance, frame/event IDs, coordinate transforms and calibration, sampling rates, units and missing-data policy. Define the representative-run selection rule before choosing an attractive trajectory. Keep individual-run examples separate from multi-run summaries. A photograph plus a curve does not imply synchronization unless the source mapping proves it.

## Handoff verification

Separate four statuses:

- `SPEC_READY`: required scientific inputs and drawing instructions exist.
- `DRAFT_RENDERED`: an executor produced an editable figure and preview from the declared bundle.
- `VISUALLY_CHECKED`: an actual preview was inspected at intended column size for semantics, labels, occlusion and readability.
- `INDEPENDENT_HANDOFF_TESTED`: an independent executor received only the brief and permitted source bundle; its questions, output and reviewer findings are recorded.

Schema/keyword/routing tests certify none of the last three. Do not mark an unrendered plan visually checked. For absent assets, record `NOT_READY`; do not substitute generated measurements or photographs.

For an independent test, preserve the supplied brief/bundle, executable output, preview, clarification count, scientific guesses, node/edge or data mismatches, final-width issues, corrective edits and rerun result. A reconstruction using a published paper tests specification transfer only; it is not validation on a new author's manuscript. A synthetic fixture tests mechanics only. Use an actual author manuscript when assessing manuscript-to-figure planning quality.
