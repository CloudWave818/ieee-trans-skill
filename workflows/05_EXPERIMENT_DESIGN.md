# 05 Experiment Design

## Entry

Require a Claim–Evidence Matrix. Use for Modes A, B, E, or when audit identifies insufficient evidence.

## Design from claims

For each nonclosed claim, define:

1. scientific question and failure criterion;
2. controlled variables, changed variables, and operating conditions;
3. proposed method and fair baseline configuration;
4. dataset, simulator, platform, hardware, or environment actually available;
5. metrics with direction and scientific meaning;
6. seeds, trials, uncertainty summaries, and statistical test only when feasible and relevant;
7. required ablation, robustness, generalization, runtime, complexity, scalability, safety, or physical layer according to routed rules;
8. planned analysis and evidence-bearing visualization;
9. reproducibility information and known constraints.

## Conditional evidence

- Use ablation for a modular learning mechanism when removal or replacement tests its claim; do not require it universally.
- Vary the named disturbance or uncertainty for a robustness claim.
- Change task, environment, scenario, agent count, or domain for a generalization claim.
- Report runtime, latency, control/inference frequency, or resource use when efficiency or online feasibility is claimed.
- Require physical validation for deployment/real-world claims or a strong system/journal expectation; otherwise state the simulation boundary.
- Use proof or controlled analysis, rather than forced ablation, when that directly identifies a theory-led mechanism.

## Fairness gate

Check shared data, information, sensing, compute budget, tuning effort, constraints, and evaluation conditions. Disclose unavoidable asymmetry. Never invent a missing baseline or result.

## Exit

Produce `templates/EXPERIMENT_MATRIX.md`. Every experiment must close or diagnose a claim; every metric and baseline must have a reason. Delete ornamental experiments and mark unavailable layers `NEEDS_EXPERIMENT`.
