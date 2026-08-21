# Experiment Audit

## Checks

- Does each experiment answer a named claim or scientific question?
- Are proposed method and baselines compared under fair data, information, constraints, compute, tuning, and evaluation conditions?
- Are baseline choices current and relevant, or explicitly bounded?
- Are datasets, simulators, hardware, scenarios, and splits actually available and identified?
- Do metrics measure the claim rather than only convenient performance?
- Are trials, seeds, uncertainty, and statistical procedures appropriate and truthfully reported?
- Is ablation used only when it identifies a modular mechanism?
- Does robustness vary the named uncertainty or disturbance?
- Does generalization change a meaningful task/environment/scenario/agent count/domain?
- Is runtime measured for efficiency, latency, onboard, or real-time claims?
- Is physical validation required and available for deployment claims?
- Are failures, trade-offs, complexity, and reproducibility addressed?

## Blockers

Mark `BLOCKER` for unfair comparison, missing central baseline, fabricated setup/result, leakage, invalid metric, or absent evidence for a central claim.

## Output

Report experiment ID, affected claim, severity, repair, resources required, and whether the repair is analysis-only or needs new runs.
