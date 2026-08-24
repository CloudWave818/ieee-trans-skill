---
name: ieee-trans-skill
description: Build, diagnose, revise, or audit long-form IEEE Transactions manuscripts in UAVs, robotics, autonomous systems, navigation, path or trajectory planning and optimization, reinforcement learning, deep RL, MARL, multi-agent decision making, game-theoretic methods, intelligent or distributed control, and learning-based control. Use for idea-to-paper planning, method/results-to-paper development, experiment design, full-paper visual architecture, figure-count and figure-type planning, per-figure drawing briefs, UAV hardware/flight/trajectory figure planning, terminology normalization, acronym control, clarity repair, cross-section consistency, figure/table design, journal adaptation, section writing, full-paper integration, draft improvement, and reviewer-style audit. Exclude IEEE Robotics and Automation Letters (RA-L), short-letter workflows, and requests that only need grammar polishing without scientific-architecture decisions.
---

# IEEE Transactions Paper Architect

## Operating contract

Build scientific arguments from project evidence. Use the corpus, knowledge base, and exemplars only to decide organization, evidence, presentation, and validation. Never substitute exemplar content for the user's research.

Resolve paths from the directory containing this file. Before any substantive paper work, read:

1. `config/KNOWLEDGE_PATHS.md` for authoritative sources and selective-loading rules.
2. `workflows/01_PROJECT_DIAGNOSIS.md` for the input and state contract.
3. The one mode-specific workflow selected below.

Do not load every domain, journal, card, or source paper. Do not use this skill for RA-L.

## Diagnose before writing

Create `templates/PROJECT_PROFILE.md` and classify:

- target journal or `UNDECIDED`;
- two to four relevant domains;
- paper type and method type;
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
| B — METHOD TO PAPER | stable mechanism, incomplete manuscript | 02 → 03 → 04 → 05 → 08 |
| C — RESULTS TO PAPER | verified results drive the paper | 04 → 10 → 06 → 08 |
| D — DRAFT IMPROVEMENT | partial/full draft or revision | 01 diagnosis → 11 integration → targeted 09 |
| E — EXPERIMENT DESIGN | experiments only | 04 → 05 |
| F — FIGURE TABLE DESIGN | full-paper visual architecture, figure inventory, drawing briefs, figures, or tables | 04 → 06 |
| G — JOURNAL ADAPTATION | choose or adapt to a venue | journal routing → 07 → 08 → 12 |
| H — REVIEWER AUDIT | pre-submission or rejection-risk review | 12 |
| I — SECTION WRITING | one named section | 09 plus the section-specific knowledge file |
| J — FULL PAPER INTEGRATION | align a near-complete manuscript | 11 → 12 |

When more than one mode applies, choose the narrowest mode that answers the request. Do not run the whole pipeline for a local task.

## Route knowledge

Load in this order:

1. Applicable Formal General Rule entries from `IEEE_TRANS_KNOWLEDGE/00_META/RULE_REGISTRY.csv`.
2. Two to four domain profiles selected with `config/DOMAIN_ROUTING.md`.
3. One locked journal profile selected with `config/JOURNAL_ROUTING.md`.
4. Three exemplars by default, at most five, selected with `config/EXEMPLAR_ROUTING.md`.
5. Raw corpus evidence only when a rule, profile, or card needs source-level adjudication.

Before using any selected card, read its exact `Do Not Generalize` section and keep that boundary in the decision log.

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
| G2 Contributions | Contribution Matrix | two to four verifiable contributions or an explicit unresolved contribution decision |
| G3 Claims | Claim–Evidence Matrix | every major claim has available or planned evidence; gaps labeled |
| G4 Experiments | Experiment Matrix | claims map to fair tests, metrics, baselines, and analysis |
| G5 Visuals | Visual Architecture + Figure/Table Plan + drawing briefs | total count is justified; every asset has a scientific question, evidence role, data source, section home, and executable design description |
| G6 Blueprint | Page Budget + Paper Blueprint | every section has inputs, evidence, transitions, and conditional length |
| G7 Section | Section Brief + section terminology contract | claims, evidence, canonical terms, permitted new terms, rules, exemplars, and forbidden overclaims are explicit |
| G8 Final audit | Final Audit Report | no `BLOCKER`; major evidence and terminology conflicts are closed before `SUBMISSION-LEVEL DRAFT` |

For local modes, enforce only the gates that protect the requested output. Never bypass G3 for experiment, results, or evidence-bearing figure work.

## Design contributions and evidence

Use `templates/CONTRIBUTION_MATRIX.md` and `templates/CLAIM_EVIDENCE_MATRIX.md`.

- Prefer two to four distinct, falsifiable contributions.
- Reject “many experiments,” “integrated framework,” routine algorithm use, or unspecified performance improvement as standalone contributions.
- Mark a major unsupported claim `CLAIM_WITHOUT_EVIDENCE`; never hide it with polished language.
- Require ablation, robustness, generalization, runtime, theory, or physical validation only when the claim and routed rules require them.
- Derive experiments from claims: `claim → evidence requirement → experiment → metric → baseline → visualization`.

## Design figures, tables, and page budget

Use `workflows/06_FIGURE_TABLE_DESIGN.md` and `templates/FIGURE_TABLE_PLAN.md` before full drafting. First design the full-paper visual architecture: recommend a justified figure/table count range, select the figure roles, order them from problem and mechanism to evidence and boundary cases, and identify mandatory versus optional assets. Corpus medians and IQRs are planning anchors, never quotas.

For every planned figure, fill `templates/FIGURE_DESIGN_BRIEF.md` until a researcher or designer can draw it without guessing the scientific content. Specify the claim, visual type, final column span, panel geometry, objects, arrows, axes, encodings, annotations, data dependencies, caption contract, and acceptance checks. A vague label such as “trajectory figure” or “framework diagram” does not pass G5.

For UAV or autonomous-flight papers, also read `references/UAV_VISUAL_PLAYBOOK.md`. Explicitly decide whether the claims require a platform photograph, sensor/computation annotation, experiment-site overview, external flight sequence, onboard/FPV view, 2-D or 3-D trajectory, time-aligned state/control curves, formation/safety-distance view, failure or disturbance case, and simulation-to-real comparison. Do not claim a physical or flight result when the corresponding asset or source data are unavailable.

For every asset, state what it proves and what the paper loses if it is removed. Remove, merge, or demote assets without an evidence role. If the user cannot draw it, return the completed design brief even when no image is generated.

Use `templates/PAGE_BUDGET.md` with the target journal, paper type, and complexity. Never convert a corpus median into a fixed page, figure, table, or equation quota.

## Write sections

Before prose, fill `templates/SECTION_BRIEF.md`. Re-route exemplars for the current section; do not reuse one fixed set across the paper.

- Ground every technical statement in user evidence or a verified reference.
- Use exemplars for architecture and evidence roles, never sentence copying.
- For results, prefer `Observation → Comparison → Quantitative evidence → Explanation → Mechanism → Scientific implication`, omitting steps only when data do not support them.
- Do not manufacture causal explanations. Connect explanations to the method, assumptions, experiment, or data.
- Build the introduction as `Problem → Gap → Challenge → Insight → Approach → Contributions` after the architecture is stable.
- Draft conclusion, abstract, and title only from stabilized claims and results.

## Control terminology and clarity

For any multi-section draft, terminology-heavy section, translation, or consistency repair, read `references/TERMINOLOGY_AND_CLARITY_CONTROL.md` and maintain `templates/TERMINOLOGY_LEDGER.md`.

- Enforce one concept–one canonical name and one name–one concept. Do not rotate technical synonyms merely to avoid repetition.
- Define each nonstandard term, acronym, and symbol before use. Admit an acronym only when it is field-standard, used repeatedly, or materially reduces clutter; remove one-off abbreviations.
- Treat a new named module, mechanism, loss, state, signal, or metric as a terminology decision. Add it to the ledger before drafting with it.
- Align the title, abstract, contributions, method, equations, algorithms, figures, tables, experiments, conclusion, and supplementary material with the same canonical names.
- Distinguish related concepts explicitly. Do not collapse a platform, subsystem, algorithm, policy, objective, signal, and metric into one vague label such as “framework” or “strategy.”
- Prefer a concrete actor–action–object sentence over abstract noun chains. Each sentence should carry one main claim; each paragraph should perform one scientific job.
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
