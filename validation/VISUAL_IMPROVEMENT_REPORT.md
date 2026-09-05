# Visual-design improvement — 2026-09-05

## What was changed

The project now has a separately maintained inspected-case layer: **20 A-level papers, 38 specified figures, 20 case groups**. This is selected-figure review, not a claim of full visual reading of 20 papers or all 100 A-level papers.

Each case records a DOI, exact PDF page/figure scope, source PDF SHA-256, local page and adjacent-text files, panel construction, scientific purpose, limitations, transferable design, data-collection needs and an abstract layout sketch. All reviews are explicitly **Codex AI inspection, not human review**. The original caption candidates and upstream rule/card registries were not relabeled or overwritten.

- [Case index](../references/visual_cases/INDEX.md)
- [Local viewer with source pages](../../IEEE_TRANS_VISUAL_LIBRARY/index.html)
- [Three-layer evidence and execution contract](../references/VISUAL_DESIGN_EVIDENCE.md)
- [Standalone web planning protocol](../references/WEB_GPT_FIGURE_PLANNER.md)

The Skill entry, Mode F workflow, consolidated figure template, standalone brief, figure audit and experiment template now distinguish corpus prior, inspected reference and manuscript-derived design. A matching corpus ID is no longer mandatory for a scientifically justified new design. Key figures require an explicit operation/decision change, a layout sketch and collection dependencies. Specification, rendered draft, actual visual check and independent handoff are recorded separately.

## Concrete source findings

1. **P001 Fig.2** has six visible panels; the automated caption record estimated three. The reviewed case preserves this discrepancy without silently changing corpus statistics.
2. **P017 Figs.5–6** align disturbance bands with controller signals and error. Their x axis is trajectory sampling index, not seconds; the shaded-range definition remains incompletely resolved in the reviewed context.
3. **P028 Fig.4** uses three method rows and four common time columns. **P033 Fig.5** uses twelve policy panels, not twelve time steps. A generic “trajectory grid” label would lose this distinction.
4. **P082 Figs.12–13** pair physical behavior with minimum-distance curves and separately summarize repeated trials. The 32-trial population belongs to the position-exchange experiment; simulated lidar observations must not be described as real onboard lidar evidence.
5. **P031 Figs.14–15** provide a useful spatial/runtime pairing but contain local equation-number and runtime-description discrepancies. The case keeps those limits instead of promoting all presentation choices into best practices.

## Validation evidence

### Source provenance and retrieval

`scripts/validate_visual_cases.py --local-sources` passed. It checks unique records, exact selected-figure coverage, source/page/context presence and PDF hashes, and retrieval behavior: an unrelated query returns no forced match, a merely rendered record is excluded from inspected references, result limits hold, and the robust-action case is retrievable. This certifies record integrity and retrieval behavior, **not visual interpretation correctness**.

The actual 20 source page images and their captions/body discussion were viewed during this task. The browser viewer loaded all 20 images; its search narrowed `robust_rl` to one case. Desktop and 390-pixel mobile checks found no horizontal overflow. The desktop preview was visually inspected.

### Independent execution test: published-mechanism reconstruction

The independent executor received only [BRIEF.md](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/input/BRIEF.md), without the original figure or case analysis. It produced:

- [Editable SVG](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/output/robust_action_selection.svg)
- [Rendered PNG](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/output/robust_action_selection.png)
- [Execution record](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/output/EXECUTION.md)
- [Final-width preview](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/output/column_width_preview.png)

The executor reported zero clarification requests and no scientific guesses. Parent review confirmed the required five nodes, four directed edges, lower-bound rule and nominal-rule distinction, with no performance data or safety guarantee invented. The actual final-width preview was inspected at 680 pixels (approximately 180 mm at 96 dpi). This was not a print proof or vector-editor round trip.

Two useful implementation corrections emerged: the narrow edge label needed wrapping, and 18 SVG units at the specified physical scale equal about 8.5 pt rather than the requested 9 pt. The executor used 19.2 units, about 9.07 pt, and re-rendered. The Skill now supplies the physical font-conversion formula and requires longest-label checks before silently shrinking type.

This test establishes execution of **one supplied schematic specification**. It does not establish planning quality from a new manuscript, quantitative plotting, photograph synchronization, or publication readiness.

### Independent forward test: unfamiliar mechanism with absent data

The independent executor applied the updated Skill to [PLANNING_FIXTURE.md](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/input/PLANNING_FIXTURE.md), a declared synthetic temporal-decoder fragment. Its outputs are the [one-figure specification](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/planning_output/PAPER_FIGURE_DESCRIPTION.md), [editable planning SVG](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/planning_output/temporal_decoder_plan.svg), [preview](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/planning_output/temporal_decoder_plan.png), and [execution/friction record](../../IEEE_TRANS_VISUAL_LIBRARY/handoff_test/planning_output/EXECUTION.md).

Parent inspection confirmed that it allowed MANUSCRIPT_DERIVED construction with no exact matching inspected reference; drew only the stated symbolic operation; left all five measurement strips visibly empty; preserved absent thresholds, units and scheduling semantics as unresolved; and kept the empirical figure NOT_READY. It independently identified repeated freeze events and goal progress as necessary to test the non-blocking claim. No new manuscript or experiment was represented as real.

The test revealed four instruction frictions. The final patch explicitly exempts one-figure work from default full-paper exemplar/journal/profile overhead; assigns routes per panel for composites; separates a provisional plan from scoped SPEC_READY/G5 completion; and permits returning provisional planning with unresolved evidence claims while blocking unsupported result prose. Those targeted instruction corrections were reviewed for consistency and passed the existing regression suite; they have not undergone another fresh independent forward test. The prior behavior test remains evidence about the pre-correction instructions, not proof of the final corrections' behavioral effect.

### Regression checks

The existing Phase 4 structural/routing suite passes 295/295 checks, including 9/9 synthetic routing scenarios. `git diff --check` reports no whitespace errors. The number 295 is not a drawing-quality score.

## Remaining work and limits

- The remaining figures of these 20 papers and other corpus papers have not been visually certified by this work.
- No new author manuscript or raw experimental dataset was supplied. Validation on real manuscript-to-figure planning is still pending.
- Published cases are not automatically ideal figures; unresolved units, statistical definitions, synchronization and local source inconsistencies remain explicit.
- The lexical case retriever supports discovery, not semantic applicability judgment. Read the selected case's limits before use.
- Original page images and extracted text stay in the separate local library. Portable installations retain cards and source locators; fresh inspection requires access to the identified local PDFs.
- The work is saved locally and not committed or published.
