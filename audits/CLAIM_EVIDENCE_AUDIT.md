# Claim–Evidence Audit

## Checks

- Is every major claim present in the Claim–Evidence Matrix?
- Does the evidence test the exact object, condition, and comparator in the claim?
- Are planned, partial, and completed evidence kept distinct?
- Are robustness, generalization, safety, efficiency, scalability, feasibility, and deployment claims tested at their stated scope?
- Are negative, neutral, and failure-case results retained when relevant?
- Is the claimed mechanism isolated by proof, ablation, controlled comparison, or another direct test?
- Are reference-based statements backed by verified citations?
- Do abstract, introduction, results, and conclusion use consistent claim strength?
- Are unknown or undetected signals incorrectly treated as zero or absence?

## Blockers

Mark `BLOCKER` for fabricated evidence, a central `CLAIM_WITHOUT_EVIDENCE`, a claim/evidence scope mismatch, or a conclusion that exceeds the body evidence.

## Output

For each claim, report status, missing evidence, affected sections, permitted wording, and the experiment/reference/author decision needed to close it.
