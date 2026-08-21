# Reviewer Audit

Simulate a skeptical reviewer for the locked target journal.

## Attack surface

- novelty and prior-art boundary;
- scientific significance and nonincrementality;
- mechanism clarity and assumptions;
- missing or unfair baselines;
- weak, incomplete, or cherry-picked experiments;
- robustness, generalization, runtime, physical validation, or theory when claim-relevant;
- statistical and reproducibility weaknesses;
- overclaims and causal overinterpretation;
- engineering feasibility and system constraints;
- journal scope and evidence fit;
- figure/table credibility and readability;
- limitations concealed by presentation quality.

## Procedure

1. State the paper's strongest defensible contribution in one sentence.
2. Ask: “If the target were rejection, where is the easiest defensible attack?”
3. List the three most damaging attacks with manuscript evidence.
4. Distinguish a fatal scientific flaw from repairable missing evidence or exposition.
5. Predict which claim each attack weakens.
6. Convert every valid attack into a revision, experiment, reference, or author-decision action.
7. Re-run affected audits after the action.

## Severity

Classify each attack as `BLOCKER`, `MAJOR`, `MODERATE`, or `MINOR` using the Final Audit definitions. A skeptical possibility without manuscript evidence is not a finding.

## Output

Return summary, strengths, weaknesses, questions, reproducibility concerns, journal-fit concerns, severity-ranked rejection risks, and an evidence-bounded recommendation. Never predict acceptance from prose fluency alone.
