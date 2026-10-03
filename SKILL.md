---
name: ieee-trans-skill
description: Draft, revise, and design IEEE Transactions or Letter papers in UAVs, robotics, planning, RL/MARL and control using the user's 29 reference papers. Match selected originals in manuscript structure, writing rhythm, figures, framework layout, captions, citations and experiment organization; turn a topic or research plan into a source-matched blueprint and concrete visuals while keeping claims and results grounded in the new project. Use for full papers, sections, experiments and figure work; exclude grammar-only edits without reference-style or scientific-architecture decisions.
---

# IEEE Reference-Matched Paper Architect

## Operating contract

Build scientific arguments from project evidence. Use the corpus, knowledge base, and exemplars only to decide organization, evidence, presentation, and validation. Never substitute exemplar content for the user's research.

Resolve paths from the directory containing this file. Before any substantive paper work, read:

1. `config/KNOWLEDGE_PATHS.md` for authoritative sources and selective-loading rules.
2. `workflows/01_PROJECT_DIAGNOSIS.md` for the input and state contract.
3. `workflows/13_REFERENCE_MATCHED_PRODUCTION.md` to select and lock the user's actual reference style, then the one mode-specific workflow selected below. For a local task use only its relevant contract fields.

Do not load every domain, journal, card, or source paper. RA-L and short Letters use `config/RAL.md` and an inspected compact reference, rather than inheriting long-form Transactions budgets.

## Match the supplied papers first

The user's 29 PDFs control presentation for this workflow. Select one main paper for structure and writing, and one concrete original figure for each major framework. Read `references/preferred_29/MANUSCRIPT_STYLE_PLAYBOOK.md`, the selected manuscript profile, and `references/preferred_29/EVIDENCE_AND_CITATION_PLAYBOOK.md` when experiments or citations matter. Use `scripts/select_style_reference.py` for candidate retrieval and `templates/REFERENCE_STYLE_CONTRACT.md` to record the mapping. Source-informed decisions must cite paper ID and PDF page, not a generic “IEEE style” label.

Match section and paragraph duties, relative space, equation-to-prose rhythm, figure sequence, table/caption form and citation placement. Framework drawings must inspect real source crops from `references/preferred_29/framework_anchors/`; preserve the chosen figure's layout skeleton, relative proportions, pictogram grammar, palette and connectors as far as the new scientific topology permits. Do not replace them with arbitrary rounded boxes or enforce the historical single-image style on every paper. Old sketches are planning drafts, not original figures.

Use `references/preferred_29/framework_anchors/SELECTION_AND_CRITIQUE.md` to compare the originals' distinct strengths. Choose again for each new method and figure purpose; R06 and any generated test drawing are not universal defaults. Preserve visual grammar while removing original slots that have no scientific counterpart. A whole-paper figure plan may use different layouts for overview, mechanism, network, training/deployment and experiments while keeping terminology, typography and caption rules consistent.

Keep science and presentation separate: imitate visual and rhetorical structure closely; rebuild mechanism, sentences, citations and experimental data from the new project. Compare actual renderings side by side and record deviations. A detailed drawing brief or passing structural test does not certify a similar-looking finished paper.

## Diagnose before writing

Create `templates/PROJECT_PROFILE.md` and classify:

- target journal or `UNDECIDED`;
- two to four relevant domains;
- paper type, method type and article form (`LETTER`, `TRANSACTIONS`, `CONFERENCE`, `OTHER`, or `UNDECIDED`), distinguished from the local reference PDF's observed layout;
- primary scientific problem and application system;
- theoretical level and physical-experiment availability;
- manuscript state: `IDEA_ONLY`, `METHOD_READY`, `EXPERIMENT_PARTIAL`, `EXPERIMENT_COMPLETE`, `DRAFT_PARTIAL`, `FULL_DRAFT`, or `REVISION`;
- available results, figures, tables, contributions, and known limitations;
- existing terminology, acronyms, notation, aliases, and known naming conflicts;
- missing inputs using only `MISSING_INPUT`, `NEEDS_EXPERIMENT`, `NEEDS_REFERENCE`, or `NEEDS_AUTHOR_DECISION`.

Never draft full prose before this diagnosis. For a tightly scoped user request, diagnose only the fields that can change the local decision and mark the rest `NOT_REQUIRED_FOR_LOCAL_TASK`.

## Select a mode

| Mode | Trigger | Primary workflow |
|---|---|---|
| A — IDEA TO PAPER | idea or problem only | 02 → 03 → 04 → 05 → 06 → 07 → 08 |
| B — METHOD TO PAPER | stable mechanism, incomplete manuscript | 02 → 03 → 04 → 05 → 06 → 07 → 08 |
| C — RESULTS TO PAPER | verified results drive the paper | 04 → 10 → 06 → 08 |
| D — DRAFT IMPROVEMENT | partial/full draft or revision | 01 diagnosis → 11 integration → targeted 09 |
| E — EXPERIMENT DESIGN | experiments only | 04 → 05 |
| F — FIGURE TABLE DESIGN | full-paper visual architecture, figure inventory, AI-ready figure-description Markdown, drawing briefs, figures, or tables | 04 → 06 |
| G — JOURNAL ADAPTATION | choose or adapt to a venue | journal routing → 07 → 08 → 12 |
| H — REVIEWER AUDIT | pre-submission or rejection-risk review | 12 |
| I — SECTION WRITING | one named section | 09 plus the section-specific knowledge file |
| J — FULL PAPER INTEGRATION | align a near-complete manuscript | 11 → 12 |

When more than one mode applies, choose the narrowest mode that answers the request. Do not run the whole pipeline for a local task.

For a one-figure Mode F request, embed the relevant diagnosis and claim checks in the requested figure document. Leave the journal UNDECIDED when it does not affect this decision; do not select a venue or create a full-paper profile/budget. Retrieve one to three relevant inspected visual cases instead of loading three full-paper exemplars. Zero matching cases is permitted with an explicit MANUSCRIPT_DERIVED rationale. Load only the rules/profiles that affect this figure and audit only its applicable claims, inputs and rendering. This local exception controls the broader default routing and completion instructions below and in supporting configs/workflows; the deterministic full-project router retains its existing defaults.

## Route knowledge

First lock the selected preferred-29 references. Then load supporting knowledge in this order:

1. Applicable Formal General Rule entries from `IEEE_TRANS_KNOWLEDGE/00_META/RULE_REGISTRY.csv`.
2. Two to four domain profiles selected with `config/DOMAIN_ROUTING.md`.
3. One locked journal profile selected with `config/JOURNAL_ROUTING.md`, or the local `config/RAL.md` Letter overlay.
4. Supporting historical candidates only for a question not covered by the locked preferred source. The deterministic router returns three exemplars by default, at most five; these are a candidate pool, not mandatory extra reading. Use zero when the main preferred source is sufficient.
5. Raw corpus evidence only when a rule, profile, or card needs source-level adjudication.

Before using any selected historical exemplar card, read its exact `Do Not Generalize` section and keep that boundary in the decision log. The older three exemplars supplement evidence burden; they do not displace the preferred main manuscript/figure style.

Use `scripts/route_project.py --input <project.json>` for deterministic routing when a normalized JSON project profile is available. Record chosen rules, profiles, cards, exclusions, and unresolved conflicts in the work product.

## Resolve conflicts

Read `IEEE_TRANS_KNOWLEDGE/08_SYNTHESIS/CONFLICT_RESOLUTION.md` whenever two instructions disagree.

- Load broad-to-narrow, but let the narrowest applicable scope control: journal-specific over domain-specific over general tendency.
- Never average theory-led and system-led evidence burdens.
- Treat corpus medians and frequencies as planning anchors, not quotas.
- Treat missing automated signals as unknown, not absence.
- Treat an exemplar as an illustration, exception, or counterexample according to its registered relationship; never promote one card into a rule.
- If applicability remains ambiguous, emit `NEEDS_AUTHOR_DECISION` and show both consequences.

## Enforce the production sequence

For full-paper work, use this order unless an existing manuscript justifies targeted revision:

`Question → Gap → Challenges → Insight → Method architecture → Contributions → Claim–evidence matrix → Experiments → Figures/tables → Page budget → Blueprint → Method/formulation → Experiments → Results interpretation → Introduction → Related work → Conclusion → Abstract → Title`

Write the title and abstract last. Do not begin with a fluent abstract that outruns the evidence.

## Apply gates

Advance only when the current gate has evidence:

| Gate | Required output | Exit condition |
|---|---|---|
| G0 Diagnosis | Project Profile + Terminology Baseline | state, task, domains, paper type, journal status, and existing naming risks identified |
| G1 Architecture | Research architecture | Problem→Gap→Challenge→Mechanism→Claim→Evidence chain complete or explicitly provisional |
| G2 Contributions | Contribution Matrix | verifiable contributions at the selected source's granularity; a focused Letter may have one principal contribution |
| G3 Claims | Claim–Evidence Matrix | every major claim has available or planned evidence; gaps labeled |
| G4 Experiments | Experiment Matrix | claims map to fair tests, metrics, baselines, and analysis |
| G5 Visuals | Visual Architecture + Figure/Table Plan + `PAPER_FIGURE_DESCRIPTION.md` | total count is justified; every asset has a scientific question, evidence role, source data, rendering route, section home, and executable drawing or plotting specification |
| G6 Blueprint | Page Budget + Paper Blueprint | every section has inputs, evidence, transitions, and conditional length |
| G7 Section | Section Brief + section terminology contract | claims, evidence, canonical terms, permitted new terms, rules, exemplars, and forbidden overclaims are explicit |
| G8 Final audit | Final Audit Report | no `BLOCKER`; major evidence and terminology conflicts are closed before `SUBMISSION-LEVEL DRAFT` |

For local modes, enforce only the gates that protect the requested output. Never bypass G3 for experiment, results, or evidence-bearing figure work.

Gate outputs may be sections of one requested blueprint or drawing document. Consolidate shared conventions and repeated status fields; do not produce separate boilerplate files or unrelated historical-card audits just to satisfy a count.

## Design contributions and evidence

Use `templates/CONTRIBUTION_MATRIX.md` and `templates/CLAIM_EVIDENCE_MATRIX.md`.

- Use distinct, falsifiable contributions at the chosen manuscript's granularity. Two to four are common planning candidates; a source-matched focused Letter can use one principal contribution rather than manufacturing extra items.
- Reject “many experiments,” “integrated framework,” routine algorithm use, or unspecified performance improvement as standalone contributions.
- Mark a major unsupported claim `CLAIM_WITHOUT_EVIDENCE`; never hide it with polished language.
- Require ablation, robustness, generalization, runtime, theory, or physical validation only when the claim and routed rules require them.
- Derive experiments from claims: `claim → evidence requirement → experiment → metric → baseline → visualization`.

## Design figures, tables, and page budget

Use `workflows/06_FIGURE_TABLE_DESIGN.md` and `templates/FIGURE_TABLE_PLAN.md` before full drafting. First design the full-paper visual architecture: recommend a justified figure/table count range, select the figure roles, order them from problem and mechanism to evidence and boundary cases, and identify mandatory versus optional assets. Corpus medians and IQRs are planning anchors, never quotas.

For a whole paper or multi-figure request, read `references/FIGURE_DESCRIPTION_TAXONOMY.md` and produce one consolidated project artifact from `templates/PAPER_FIGURE_DESCRIPTION.md`. Classify every figure by primary type and rendering route, then state exactly what an author, plotting agent, vector-design agent, or image tool must create.

For UAV visual design, the user's 29 preferred papers are the primary style and construction library: read `references/preferred_29/STYLE_PLAYBOOK.md`, then retrieve specific figures with `scripts/query_visual_cases.py`. Use `references/preferred_29/INDEX.md` for paper stories and the 281 figure records; select detailed cards rather than loading them all. Deliberately adapt their color relationships, grouping, pictograms, connectors and panel composition to the manuscript's actual mechanism. These visual sources may be used regardless of their publication venue; the RA-L writing exclusion does not exclude a supplied visual reference. Older cases supplement missing relationships. For learning-based UAV work read `references/preferred_29/RL_FIGURE_PLAYBOOK.md`; actual RL training normally needs a learning-process figure considered alongside final task, safety, ablation and transfer evidence. A network or a frozen zero-shot model alone does not imply RL.

For a method framework, network architecture, system architecture or algorithm overview, read the user's dedicated [framework-style module](modules/ieee-trans-framework-style/SKILL.md). Inspect the selected preferred-29 original figure crop and transfer its actual geometry, hierarchy, typography, palette, pictograms and connectors. The historical `assets/reference-framework-style.jpg` is an optional anchor, not a universal override. Derive every module and connection from the current manuscript. Apply this module only to framework figures; other figure families retain their existing workflows. Keep raster previews and editable vector deliverables accurately labeled.

A title alone is enough to produce a concrete `PROVISIONAL_FROM_TITLE` visual plan and editable mechanism/layout sketch. Separate known inputs, design assumptions and unresolved mechanisms. Do not require a full manuscript to begin; do not turn assumed mechanisms into claims or invent results. See `examples/preferred_uav_rl/PAPER_FIGURE_DESCRIPTION.md` for a worked example.

When the user wants to perform the same planning in a standalone web chat without this Skill, provide `references/WEB_GPT_FIGURE_PLANNER.md`. It is the portable, self-contained protocol. Use the three-layer evidence contract in `references/VISUAL_DESIGN_EVIDENCE.md`: CORPUS_PRIOR informs scale/roles; INSPECTED_REFERENCE supports construction; the manuscript-specific claim/evidence trigger determines content. Permit MANUSCRIPT_DERIVED designs without a matching corpus ID when justified. Retrieve the preferred cases first, and `references/visual_cases/INDEX.md` for supplemental relationships; record reference scope and uncertainty. Include a layout sketch for key figures, the mechanism change, and the experiment-collection contract. Distinguish SPEC_READY, DRAFT_RENDERED, VISUALLY_CHECKED, and INDEPENDENT_HANDOFF_TESTED; structural checks cannot certify drawing quality.

For every planned figure, complete its entry in `PAPER_FIGURE_DESCRIPTION.md`; use `templates/FIGURE_DESIGN_BRIEF.md` as an optional standalone extraction for a designer. Specify the claim, exact visual subtype, final column span, panel geometry, objects, arrows, axes, series, aggregation, uncertainty, encodings, annotations, data dependencies, caption contract, and acceptance checks. A vague label such as “trajectory figure,” “result plot,” or “framework diagram” does not pass G5.

Assign one rendering route:

For a mixed composite, assign a route to each panel and a whole-figure readiness status. Missing central measurements keep the full figure NOT_READY; an available symbolic mechanism or empty layout can still be rendered as an explicitly provisional planning draft. A completed plan does not make missing empirical panels SPEC_READY or close G5.

- `DATA_PLOT`: quantitative chart or trajectory generated from named source data and a reproducible plotting specification; never ask an image generator to invent values, curves, error bars, or axes.
- `VECTOR_SCHEMATIC`: architecture, block, mechanism, geometry, or algorithm diagram described by explicit nodes, edges, groups, labels, and layout constraints.
- `PHOTO_COMPOSITE`: real platform, site, flight, or qualitative evidence assembled only from traceable source photographs, frames, maps, or screenshots.
- `TABLE`: exact values or configurations presented as a structured table.
- `NOT_READY`: the necessary data or visual source is missing; use an approved missing-state label.

For UAV or autonomous-flight papers, also read `references/UAV_VISUAL_PLAYBOOK.md`. Explicitly decide whether the claims require a platform photograph, sensor/computation annotation, experiment-site overview, external flight sequence, onboard/FPV view, 2-D or 3-D trajectory, time-aligned state/control curves, formation/safety-distance view, failure or disturbance case, and simulation-to-real comparison. Do not claim a physical or flight result when the corresponding asset or source data are unavailable.

For every asset, state what it proves and what the paper loses if it is removed. Remove, merge, or demote assets without an evidence role. If no image is generated, the completed `PAPER_FIGURE_DESCRIPTION.md` is still a required deliverable and must be sufficiently explicit for a downstream AI or researcher to execute without guessing scientific content.

Use `templates/PAGE_BUDGET.md` with the target journal, paper type, and complexity. Never convert a corpus median into a fixed page, figure, table, or equation quota.

## Write sections

Before prose, fill `templates/SECTION_BRIEF.md` with the selected preferred manuscript's section/paragraph moves and source pages. Preserve the main style lock across the paper; re-route supporting exemplars only when their scientific role changes.

For reference-matched prose or a complaint that writing reads like a manual, read `references/preferred_29/PROSE_ARGUMENT_PLAYBOOK.md`, `references/preferred_29/SENTENCE_CRAFT_PLAYBOOK.md` and the chosen `writing_moves/` card. Inspect the actual applicable source unit, including its adjacent sentences. Transfer argument dependencies and sentence choices: scientific subject, precise predicate, information order, condition scope, comparison/numeric role, antecedent and calibrated evidence strength. Section counts and generic antipattern statistics cannot establish sentence craft. Keep production contracts in working notes, preserve project facts, and validate the change with actual before/after prose read both sentence by sentence and as a paragraph.

- Ground every technical statement in user evidence or a verified reference.
- Use exemplars for architecture and evidence roles, never sentence copying.
- For results, check observation, comparison, evidence, supported explanation and scientific consequence as applicable roles. The inspected donor and experiment question control their order, grouping and emphasis; each paragraph need not contain every role.
- Do not manufacture causal explanations. Connect explanations to the method, assumptions, experiment, or data.
- Repair defensive repetition and experiment-as-procedure prose using the preferred prose guide. Preserve necessary scope, fair-comparison conditions, negative findings and replication detail; internal audit states stay in working notes.
- Use `Problem → Gap → Challenge → Insight → Approach → Contributions` as an introduction coverage check after the architecture is stable; the inspected donor and the new argument control order, grouping and contribution form.
- Draft conclusion, abstract, and title only from stabilized claims and results.

## Control terminology and clarity

For any multi-section draft, terminology-heavy section, translation, or consistency repair, read `references/TERMINOLOGY_AND_CLARITY_CONTROL.md` and maintain `templates/TERMINOLOGY_LEDGER.md`.

- Enforce one concept–one canonical name and one name–one concept. Do not rotate technical synonyms merely to avoid repetition.
- Define each nonstandard term, acronym, and symbol before use. Admit an acronym only when it is field-standard, used repeatedly, or materially reduces clutter; remove one-off abbreviations.
- Treat a new named module, mechanism, loss, state, signal, or metric as a terminology decision. Add it to the ledger before drafting with it.
- Align the title, abstract, contributions, method, equations, algorithms, figures, tables, experiments, conclusion, and supplementary material with the same canonical names.
- Distinguish related concepts explicitly. Do not collapse a platform, subsystem, algorithm, policy, objective, signal, and metric into one vague label such as “framework” or “strategy.”
- Prefer a concrete actor–action–object relation over abstract noun chains. Keep the main judgment and its conditions or comparisons readable; preserve tightly related clauses rather than forcing every sentence into one simple fact. Each paragraph should perform one scientific job.
- Repair unclear antecedents such as “this method,” “the above mechanism,” or “it” when more than one referent is possible.
- Rename globally: if a canonical term changes, log the rename and apply it throughout, including captions, legends, symbols, pseudocode, and cross-references.

Run `audits/TERMINOLOGY_CLARITY_AUDIT.md` before full-paper integration is closed and again during Final Audit. Fluent wording does not pass when the reader cannot identify the object, operation, condition, or evidence.

## Revise existing manuscripts

Do not restart a full draft from zero. First classify each unit as `KEEP`, `REVISE`, `RESTRUCTURE`, `DELETE`, or `ADD` using `workflows/11_FULL_PAPER_INTEGRATION.md`. Route only affected sections through Section Writing.

Preserve correct technical content and canonical user terminology unless a logged scientific, ambiguity, consistency, or journal-fit reason requires change. Record every global rename in the Terminology Ledger.

## Prevent fabrication and overautomation

Never invent citations, data, baselines, statistical significance, hardware tests, theorems, runtime, datasets, author claims, stability, convergence, generalization, deployment, or improvement numbers.

When evidence is missing, stop the affected claim and emit one of the approved missing-state labels. Offer a provisional plan, not fabricated completion.

## Audit completion

Run `workflows/12_FINAL_AUDIT.md` and all relevant files in `audits/`, including the terminology and clarity audit for manuscript text. Classify findings as `BLOCKER`, `MAJOR`, `MODERATE`, or `MINOR` and fill `templates/FINAL_AUDIT_REPORT.md`.

- Mark `PAPER ARCHITECTURE READY` only with no blocker in the scientific architecture.
- Mark `SUBMISSION-LEVEL DRAFT` only when major scientific evidence is closed.
- Never infer submission readiness from fluent English alone.
- Ask the reviewer audit: “If the target were rejection, where is the easiest defensible attack?” Feed that risk back into revision.

Phase 4 construction status is not a stability claim. Real-paper validation is required before calling this skill stable.
