# Contribution Audit

Audit contribution distinctness, novelty boundary, and evidence linkage.

## Checks

- Does each contribution name a scientific object, mechanism, and verifiable effect?
- Does it answer an earlier gap or challenge?
- Is the novelty boundary supported by references or marked `NEEDS_REFERENCE`?
- Are two contributions duplicates separated only by implementation detail?
- Is a theory, system, dataset, or evidence contribution mislabeled as a method contribution?
- Is “extensive experiments,” “integrated framework,” routine algorithm use, or unspecified improvement presented as novelty?
- Does every contribution map to a claim, experiment/proof, and figure/table when applicable?
- Does the stated strength match available evidence?
- Are risks and failure conditions disclosed?

## Blockers

Mark `BLOCKER` when the main contribution is contradicted by prior art, depends on nonexistent evidence, or cannot be distinguished from routine assembly.

## Output

Return `KEEP`, `REVISE`, `MERGE`, `DELETE`, or `NEEDS_AUTHOR_DECISION` per contribution with rationale.
