# Terminology and Clarity Control

## Purpose

Use this reference to stop terminology drift, acronym overload, concept-name ambiguity, and prose that sounds formal but hides the engineering logic. Technical consistency outranks stylistic synonym variety.

## Core invariants

1. **One concept–one canonical name.** Repeated use of the same technical term is desirable when it preserves identity.
2. **One name–one concept.** If two objects differ in role, input, output, scope, or mathematical meaning, give them distinct names.
3. **Define before use.** A reader should never have to infer a term, acronym, or symbol from later text.
4. **Rename globally.** A local rename is prohibited. Update prose, equations, algorithms, figures, tables, captions, legends, and supplementary material together.
5. **Name only useful distinctions.** A term earns a name when the distinction is field-standard, contribution-critical, needed for derivation, or required for reproduction.

## Build the terminology ledger

Inventory candidate terms from the title, abstract, contribution list, headings, method, notation, equations, algorithms, figures, captions, tables, experiments, conclusion, and supplements. Group observed labels by underlying concept before selecting a canonical form.

For each concept, record:

- its plain-language definition and scientific role;
- canonical English term, acronym if admitted, and symbol if used;
- allowed grammatical variants that do not change identity;
- forbidden aliases and easily confused neighboring concepts;
- first-definition location and every section that consumes it;
- source of authority: author decision, field convention, equation, code, dataset, or hardware label.

Do not choose the most frequent label automatically. Prefer the label that is technically accurate, field-recognizable, shortest without losing meaning, and compatible with the method and equations.

## Term-admission test

Before naming a new module, mechanism, loss, policy, state, signal, dataset split, metric, or experimental condition, answer:

1. Does the distinction change the method, mathematics, experiment, evidence, or reproduction?
2. Is there an established field term that already names it accurately?
3. Will the term be reused enough to reduce explanation rather than add memory burden?
4. Can a reader define it in one plain sentence and distinguish it from neighboring terms?

Reject or merge the term when these answers do not justify a separate name. Prefer a direct description for a one-off procedural step.

## Acronym control

Admit an acronym when at least one strong reason applies: it is a standard field abbreviation, it recurs throughout the paper, or the unabbreviated form materially obstructs readability. As a practical review trigger, scrutinize any acronym used fewer than three times after definition; this is a diagnostic threshold, not a universal quota.

- Define the full term and acronym at first substantive use in the main text.
- Do not define it in the abstract and assume that definition carries into the body.
- Avoid two acronyms that differ by one letter or refer to neighboring concepts.
- Remove an acronym used only in one paragraph, figure, or table unless it is a standard unit or field convention.
- Keep baseline, dataset, metric, and hardware names exactly consistent with their authoritative sources.

## Naming hierarchy

Keep these categories distinct:

| Category | Naming question | Typical error |
|---|---|---|
| System/platform | What physical or simulated system operates? | calling the UAV, controller, and full architecture “the system” interchangeably |
| Module/subsystem | What bounded component has defined inputs and outputs? | renaming one module in every section |
| Algorithm/policy/controller | What procedure maps inputs to decisions or actions? | calling an optimizer a policy or a controller a framework |
| Mechanism | Why does a designed interaction change behavior? | using “mechanism” as a decorative synonym for method |
| Objective/loss/reward | What scalar criterion is optimized or learned? | treating loss, reward, and evaluation metric as equivalent |
| State/observation/feature/signal | What information exists at which interface? | collapsing sensed observation and latent state |
| Metric/measure/index | How is performance evaluated? | using a training objective name for a reported metric |
| Scenario/condition/dataset split | Under what evidence boundary is a result valid? | changing test-condition labels between setup and results |

## Cross-section terminology contract

- **Title and abstract:** use only central terms that survive into the method and evidence.
- **Introduction and contributions:** name the problem, mechanism, and outputs exactly as later formalized.
- **Method and notation:** define every object once and keep its prose name, symbol, and algorithm label aligned.
- **Experiments and results:** use authoritative baseline, dataset, condition, metric, and module names; ablation labels must match the method decomposition.
- **Figures and tables:** legends, panel labels, captions, and callouts must use ledger names, not shortened local aliases.
- **Conclusion:** return to the same claims and objects; do not introduce a grander label for the method at the end.

## Clarity repair

For each difficult sentence, recover five items: actor, action, object, condition, and consequence/evidence. If one is absent, add it only when supported; otherwise mark the missing information.

- Replace noun stacks with verbs: “performance improvement realization” becomes the supported action that caused the measured change.
- Replace empty subjects: name the estimator, policy, controller, experiment, or result instead of “this framework” or “it.”
- Split sentences that contain multiple claims, conditions, contrasts, or causal steps.
- Keep conditions next to the claim they limit.
- Prefer a familiar field term over an ornate synonym.
- Delete signposting that adds no logical relation. A transition should express contrast, cause, consequence, condition, or scope.
- Do not simplify away assumptions, uncertainty, or evidence boundaries.

## Conflict-resolution sequence

1. Detect all observed variants and locations.
2. Decide whether they are aliases of one concept or genuinely distinct concepts.
3. Select canonical terms and record forbidden aliases.
4. Produce a global replacement map before editing prose.
5. Apply replacements across every artifact.
6. Reread for grammar because global term replacement can change articles, plurality, and verb agreement.
7. Run the audit and close or explicitly escalate every ambiguity.

## Non-goals

- Do not remove legitimate field terminology merely to make the paper sound popular.
- Do not replace precise repetition with synonyms for literary elegance.
- Do not use fluent rewriting to hide missing definitions, weak logic, or unsupported claims.
- Do not treat an acronym count as a universal acceptance or rejection rule.
