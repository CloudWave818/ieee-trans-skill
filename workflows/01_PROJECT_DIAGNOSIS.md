# 01 Project Diagnosis

## Entry

Enter for every new paper task. For a local request, limit diagnosis to fields that can change the requested output.

## Inputs

Collect or mark unknown:

- target journal;
- research domains, paper type, method type, and application system;
- primary scientific problem;
- theoretical level and physical-experiment availability;
- manuscript state;
- available method, data, experiments, results, figures, tables, contributions, draft sections, reviewer comments, and limitations.

Never infer an available experiment from a planned experiment or a deployment claim from a simulation.

## State decision

1. Use `IDEA_ONLY` when neither mechanism nor evidence is stable.
2. Use `METHOD_READY` when the mechanism can be specified but validation is not complete.
3. Use `EXPERIMENT_PARTIAL` when some claim-bearing results are missing.
4. Use `EXPERIMENT_COMPLETE` when the evidence set is available but manuscript construction remains.
5. Use `DRAFT_PARTIAL` for incomplete prose with recoverable architecture.
6. Use `FULL_DRAFT` for an integrated manuscript without an active decision letter.
7. Use `REVISION` when editor/reviewer feedback controls the work.

## Procedure

1. Copy `templates/PROJECT_PROFILE.md` into the project work area.
2. Separate facts supplied by the user from interpretations and plans.
3. Route two to four domains with `config/DOMAIN_ROUTING.md`.
4. Lock the specified journal or create a two-to-four-journal decision set.
5. Select Mode A–J with `config/PAPER_TYPE_ROUTING.md` and the user task.
6. Identify which gates and workflows are required; skip unrelated ones.
7. Label every blocking gap with an approved missing-state label.
8. Create a route request for `scripts/route_project.py` when deterministic card/rule selection is useful.

## Exit

Exit only when project state, selected mode, task scope, domains, paper type, journal status, available evidence, and unresolved author decisions are explicit. The output is a completed Project Profile plus a routing decision log.
