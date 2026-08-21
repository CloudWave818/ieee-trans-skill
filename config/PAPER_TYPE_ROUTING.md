# Paper Type and State Routing

## Paper identity

Choose the primary type that controls the burden of proof; add material secondary types without averaging their requirements.

| Primary type | Main architecture | Evidence emphasis |
|---|---|---|
| theory-led control | assumptions → formulation → theorem/analysis → controlled validation | correctness, stability/convergence when claimed, boundary conditions |
| algorithmic method | problem → mechanism → algorithm → complexity/evaluation | mechanism isolation, fair baselines, runtime when efficiency is claimed |
| learning method | task/MDP → representation/policy → training → evaluation | comparisons, ablation when modular, robustness/generalization when claimed |
| robotics/autonomous system | system problem → architecture → implementation → validation | physical/system evidence, runtime, failure modes, reproducibility |
| navigation/planning | environment/model → formulation → planner/controller → trajectories | safety/feasibility, runtime, scenarios, qualitative and quantitative outcomes |
| hybrid method-system | formal mechanism plus deployed system | satisfy both mechanism and deployment claims; do not dilute either |

## Manuscript state to mode

| State | Default mode | Prohibited shortcut |
|---|---|---|
| `IDEA_ONLY` | A | full prose before provisional architecture |
| `METHOD_READY` | B | contribution claims without evidence plan |
| `EXPERIMENT_PARTIAL` | E or B | results narrative that implies missing tests exist |
| `EXPERIMENT_COMPLETE` | C | abstract before claim/results stabilization |
| `DRAFT_PARTIAL` | D or I | rewriting unaffected sections |
| `FULL_DRAFT` | D or J | restart from zero |
| `REVISION` | D | answer reviewers before manuscript diagnosis |

Local user intent overrides the default mode but never the evidence gates protecting that local output.
