# Terminology and Clarity Audit

## Entry

Use for any multi-section draft, translated manuscript, terminology-heavy method, full-paper integration, or final audit. Require the manuscript and `templates/TERMINOLOGY_LEDGER.md`; if no ledger exists, creating the baseline is the first audit action.

## Checks

### Concept identity

- Does one concept appear under multiple names across title, abstract, contributions, method, experiments, figures/tables, and conclusion?
- Does one name refer to multiple systems, modules, algorithms, signals, objectives, or metrics?
- Are related concepts such as state/observation, reward/loss/metric, planner/controller/policy, and platform/system/module distinguished?
- Do prose terms, symbols, equations, algorithms, code-facing labels, captions, legends, and table headers agree?
- Does every global rename cover all manuscript artifacts and preserve grammar?

### Definitions and acronyms

- Is every nonstandard term, acronym, and symbol defined before first substantive use?
- Is a body-text definition incorrectly assumed from the abstract alone?
- Are any acronyms unused, used only once, needlessly similar, or harder to remember than the full term?
- Are field-standard baseline, dataset, metric, and hardware names reproduced accurately?
- Does each newly coined term pass the term-admission test in `references/TERMINOLOGY_AND_CLARITY_CONTROL.md`?

### Terminology load

- Are ordinary procedural steps given decorative names without a scientific distinction?
- Can one-off terms be replaced by direct descriptions?
- Can overlapping terms be merged without erasing a meaningful distinction?
- Does the reader need to remember more names than the method architecture and evidence actually require?

### Sentence and paragraph clarity

- Can the actor, action, object, condition, and consequence/evidence be identified?
- Does any sentence hide multiple main claims, conditions, contrasts, or causal steps?
- Do abstract noun chains replace concrete operations?
- Are “this method,” “the above mechanism,” “the framework,” “it,” or “they” ambiguous?
- Does each paragraph perform one scientific job and expose its relation to the previous and next unit?
- Has ornate or fluent wording hidden a missing assumption, missing evidence, or unsupported causal claim?

## Severity

- `BLOCKER`: terminology or symbol ambiguity changes the method, equation, experiment, result, contribution, or truth conditions; the intended concept cannot be recovered safely.
- `MAJOR`: systematic cross-section drift, undefined central terminology, excessive acronym load, or method/ablation/metric names that obstruct review or reproduction.
- `MODERATE`: bounded vague antecedents, late definitions, noun stacks, overloaded sentences, or unnecessary terms that materially slow comprehension.
- `MINOR`: local verbosity or a harmless isolated inconsistency with an unambiguous repair.

## Output

Return both a diagnosis and an executable repair map:

| Severity | Location(s) | Observed wording | Problem type | Intended concept or missing information | Canonical replacement/repair | Global scope | Verification |
|---|---|---|---|---|---|---|---|

Also provide:

1. a same-concept/multiple-name list;
2. a same-name/multiple-concept list;
3. acronyms to keep, remove, or rename;
4. proposed ledger entries and unresolved `NEEDS_AUTHOR_DECISION` items;
5. a section-by-section global rename plan;
6. representative clarity rewrites that preserve the original scientific content;
7. a pass/fail statement for terminology consistency and clarity.

Do not silently guess between scientifically distinct meanings. Do not rewrite unaffected correct text merely for stylistic variation.
