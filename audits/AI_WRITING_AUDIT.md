# AI Writing Audit

Audit for automated-writing patterns that obscure science rather than for superficial phrase policing.

## Checks

- Are contributions packaged into a fixed count without scientific distinction?
- Are generic claims such as “significantly improves” unsupported by values/tests?
- Are paragraphs symmetrical, repetitive, or transition-heavy without information gain?
- Are “comprehensive,” “novel,” “robust,” “efficient,” or “real-world” used beyond evidence?
- Does text invent plausible-but-unverified citations, data, baselines, datasets, hardware, theorems, runtime, or statistics?
- Are mechanism explanations generic stories detached from method, assumptions, experiment, or data?
- Are limitations replaced by vague future work?
- Are exemplar sentence patterns copied or lightly paraphrased?
- Are placeholder specifics presented as facts?
- Has fluent prose hidden `MISSING_INPUT` or `NEEDS_EXPERIMENT`?

## Blockers

Any fabricated scientific fact, result, reference, or experiment is a `BLOCKER`. Do not repair it by softer wording; remove it or obtain evidence.

## Output

Separate scientific fabrication risk, overclaim risk, template-pattern risk, and local style risk. Preserve legitimate repeated terminology required for technical consistency.
