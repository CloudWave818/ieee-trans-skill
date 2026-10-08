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
- Can each central result be traced through the actual run IDs, log fields, filtering/aggregation, metric denominator, uncertainty and plotted/table value to its caption and prose? Baseline names and evaluation conditions must remain identical along that chain.
- Does the decisive controlled comparison test the claimed mechanism, and would a null or negative outcome lead to narrowing the claim? A proposed protocol is not a completed experiment.
- For a detailed physical-scene brief, are indoor/outdoor, obstacles/no obstacles, spatial placement, flight/events, camera/frame selection, publication dimensions and external-model handoff concrete and scientifically motivated?
- Are actual flight, nonflight hardware, recorded datasets, simulation and renderer separated per source panel? Are simultaneous agents, one-flight time ghosts and multiple registered trials distinguishable?
- Are proposed venue/dimensions/poses labeled as proposed, with measured trajectory and photo/trial association grounded separately? Does the brief remain useful for a proposed illustration when real evidence assembly is still pending?

## Blockers

Mark `BLOCKER` for unfair comparison, missing central baseline, fabricated setup/result, leakage, invalid metric, or absent evidence for a central claim.

## Output

Report experiment ID, affected claim, severity, repair, resources required, and whether the repair is analysis-only or needs new runs.
