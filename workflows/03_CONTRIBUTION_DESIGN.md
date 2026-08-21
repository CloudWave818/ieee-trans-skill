# 03 Contribution Design

## Entry

Require a stable or explicitly provisional research architecture and the user's actual method/results.

## Procedure

1. Copy `templates/CONTRIBUTION_MATRIX.md`.
2. Separate contribution types: problem/formulation, mechanism/method, theory, system/implementation, evidence/resource.
3. Prefer two to four contributions with distinct scientific functions.
4. For each contribution, bind novelty, addressed problem, mechanism, claim, evidence, experiment, figure/table, strength, and risk.
5. Compare contributions pairwise. Merge entries that make the same claim with different nouns.
6. Check that every contribution answers an earlier gap or challenge.
7. Downgrade novelty language when prior-art verification is absent and mark `NEEDS_REFERENCE`.

## Rejection rules

Do not accept these as standalone contributions without a concrete scientific mechanism and evidence:

- many or extensive experiments;
- an integrated/comprehensive framework;
- first use of a routine algorithm;
- improved performance without a causal or design contribution;
- application to a new dataset or platform alone.

## Risk grades

- `LOW`: distinct mechanism and direct evidence exist.
- `MEDIUM`: plausible distinction but evidence or prior-art boundary is incomplete.
- `HIGH`: mainly packaging, performance, or application novelty.
- `BLOCKER`: contradicts available evidence or depends on fabricated/missing work.

## Exit

Every retained contribution is falsifiable, nonredundant, linked to the architecture, and has an evidence status. Otherwise return to Research Architecture or mark the unresolved author decision.
