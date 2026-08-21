# Domain Routing

Select two to four material domains. Include a domain only when it changes scientific architecture, evidence, or writing decisions.

| Domain | Strong signals | Profile |
|---|---|---|
| `UAV_AUTONOMY` | UAV, drone, aerial robot, quadrotor, flight autonomy | `IEEE_TRANS_KNOWLEDGE/06_DOMAINS/UAV_AUTONOMY.md` |
| `ROBOTICS` | robot system, manipulator, SLAM, embodied autonomy, robot hardware | `IEEE_TRANS_KNOWLEDGE/06_DOMAINS/ROBOTICS.md` |
| `NAVIGATION_PLANNING` | navigation, path planning, exploration, obstacle avoidance | `IEEE_TRANS_KNOWLEDGE/06_DOMAINS/NAVIGATION_PLANNING.md` |
| `TRAJECTORY_OPTIMIZATION` | trajectory planning/optimization, optimal motion, MPC trajectory | `IEEE_TRANS_KNOWLEDGE/06_DOMAINS/TRAJECTORY_OPTIMIZATION.md` |
| `RL_MARL` | reinforcement learning, deep RL, MARL, policy/value learning | `IEEE_TRANS_KNOWLEDGE/06_DOMAINS/RL_MARL.md` |
| `MULTI_AGENT_DECISION` | multi-agent, swarm, cooperative/competitive decision, game | `IEEE_TRANS_KNOWLEDGE/06_DOMAINS/MULTI_AGENT_DECISION.md` |
| `CONTROL` | intelligent, adaptive, distributed, learning-based, predictive, or nonlinear control | `IEEE_TRANS_KNOWLEDGE/06_DOMAINS/CONTROL.md` |

## Combination examples

- UAV navigation with DRL: `UAV_AUTONOMY`, `NAVIGATION_PLANNING`, `RL_MARL`.
- Multi-UAV pursuit with MARL: `UAV_AUTONOMY`, `RL_MARL`, `MULTI_AGENT_DECISION`.
- Trajectory tracking with adaptive control: `CONTROL`, `TRAJECTORY_OPTIMIZATION`, plus `UAV_AUTONOMY` or `ROBOTICS` only when the platform materially matters.
- Autonomous vehicle learning control: `CONTROL`, `RL_MARL`, `NAVIGATION_PLANNING`.

## Tie breaking

Rank by: primary scientific object → core mechanism → evidence implications → application context. Prefer the more specific domain as primary. Do not load all seven domains. Record excluded adjacent domains when ambiguity could affect later decisions.
