# Writing Style Audit

## Checks

- Does each paragraph have one scientific function and a clear logical relation to its neighbors?
- Are claims calibrated to evidence and conditions?
- Are technical nouns, notation, acronyms, tense, and comparator names consistent?
- Are definitions introduced before use?
- Are transitions argumentative rather than mechanical?
- Does Results interpret rather than transcribe every number?
- Does Introduction avoid generic field background and literature dumping?
- Does Related Work synthesize boundaries instead of listing papers?
- Do Abstract and Conclusion stay within verified results?
- Are sentences concise without deleting assumptions or scientific qualifiers?
- Can the reader identify the actor, action, object, condition, and evidence without decoding abstract noun chains?
- Does each sentence carry one main claim and each paragraph one scientific job?
- Are vague antecedents such as “this method,” “the above strategy,” and “it” resolved when multiple referents exist?
- Is journal emphasis respected without imitating exemplar phrases?

## Severity

Escalate a writing issue to `MAJOR` when wording changes the scientific claim, causal interpretation, evidence boundary, or reviewer understanding. Treat purely local readability defects as `MINOR` or `MODERATE`.

## Output

Provide location, problem, scientific consequence, revision instruction, and a verification question; do not rewrite correct unaffected text by default. Route terminology conflicts to `TERMINOLOGY_CLARITY_AUDIT.md` rather than treating them as cosmetic variety.
