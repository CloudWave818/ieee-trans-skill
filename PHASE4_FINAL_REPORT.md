# Phase 4 Final Report

Status: `PHASE 4 IEEE TRANS WRITING SKILL CONSTRUCTED / READY FOR REAL-PAPER VALIDATION`

## 1. Skill architecture

`SKILL.md` is the concise control plane. Five files in `config/` define knowledge, journal, domain, exemplar, and paper-type routing. Twelve workflow files implement diagnosis through final audit. Nine audit files, nine reusable templates, deterministic scripts, and validation artifacts provide execution and quality control. The Skill contains no copied corpus.

## 2. Routing architecture

Project Diagnosis normalizes journal, domains, paper type, method, scientific problem, evidence, state, and local task. `scripts/route_project.py` selects two to four domains, one locked journal overlay, active rules, the appropriate Mode A–J workflow, and three exemplars by default. Complex cross-domain/multi-section requests may receive up to five. RA-L is rejected as out of scope.

## 3. Workflow architecture

Full-paper work follows Question→Gap→Challenge→Insight→Mechanism→Contributions→Claims/Evidence→Experiments→Visuals→Budget→Blueprint→section drafting→integration→audit. Local tasks enter the narrowest protecting workflow. Existing drafts use diagnosis and `KEEP/REVISE/RESTRUCTURE/DELETE/ADD` rather than restart-from-zero rewriting.

## 4. Knowledge invocation

The Skill reads the active rule registry, then loads applicable General rules, two to four domain profiles, and the locked journal profile. Section, evidence, visual, and writing files load only when the current task needs them. Corpus statistics remain descriptive ranges, never quotas.

## 5. Exemplar invocation

The live Exemplar routing registry is scored on Domain (30), Role (25), Paper Type (15), Journal (15), Evidence Need (10), and Rule (5). A role/evidence match is mandatory; scores below 35 are excluded unless fewer than three cards pass. Each selected card exposes its `Do Not Generalize` boundary for review. Different tasks re-route different cards.

## 6. Rule conflicts

Knowledge loads broad-to-narrow; the narrowest applicable scope controls. Journal-specific rules may override an inapplicable general tendency, and domain rules refine general rules. Theory-versus-system, proof-versus-ablation, physical-validation, section-split, and figure-density conflicts use `IEEE_TRANS_KNOWLEDGE/08_SYNTHESIS/CONFLICT_RESOLUTION.md`, never an averaged compromise.

## 7. Hallucination prevention

The Skill prohibits invented citations, results, baselines, statistics, hardware, theorems, runtime, datasets, author claims, stability, convergence, generalization, deployment, and improvement values. Missing material receives `MISSING_INPUT`, `NEEDS_EXPERIMENT`, `NEEDS_REFERENCE`, or `NEEDS_AUTHOR_DECISION`. Fluent prose cannot close missing evidence.

## 8. Incomplete research

Incomplete projects may produce provisional architecture, contribution risk, and executable evidence plans. `CLAIM_WITHOUT_EVIDENCE` blocks result, abstract, conclusion, and submission-readiness prose. The Skill never fills scientific blanks merely to produce a complete manuscript.

## 9. Reviewer audit

The eight-stage final pipeline audits scientific logic, contributions, claim evidence, experiments, figures/tables, journal fit, writing/AI patterns, and reviewer risk. Findings use `BLOCKER`, `MAJOR`, `MODERATE`, or `MINOR`. The reviewer simulation asks where a defensible rejection attack is easiest and routes valid attacks back into revision.

## 10. Validation results

- Required synthetic scenarios: 8/8 passed.
- Additional RA-L boundary scenario: 1/1 passed.
- Total synthetic cases: 9/9 passed.
- Independent completion audit: 179/179 checks passed.
- Official `skill-creator` quick validation: PASS.
- Every routed case loaded valid domain and journal scopes, selected the expected workflow, returned three relevant cards, enforced score and role/evidence gates, and stayed below the maximum of five.
- Final independent validation is recorded in `validation/PHASE4_FINAL_VALIDATION.json`.

## 11. Remaining issues

- Exemplar `Do Not Generalize` conflicts still require semantic review by the acting agent; the deterministic router surfaces but does not pretend to solve every boundary conflict.
- Official journal instructions can change and must be checked when exact format, page limit, or submission policy matters.
- The present domain and journal profiles inherit the sample sizes and uncertainty documented in the Knowledge Base.
- The skill folder and callable frontmatter name both use the same lowercase hyphen-case name: `ieee-trans-skill`.

## 12. Real-paper tests still required

Phase 5 must use at least one real manuscript to test whether routing remains stable across changing sections; whether the scientific architecture matches author intent; whether requested experiments are executable; whether figure plans survive real data constraints; whether prose preserves terminology and evidence boundaries; and whether reviewer findings improve the draft without over-rewriting. Only after that phase may the Skill be called stable.

Upstream Corpus, Knowledge, and Exemplars were not modified or expanded. No RA-L skill was started.
