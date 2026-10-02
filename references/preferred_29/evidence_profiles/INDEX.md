# Evidence profiles for all 29 supplied papers

Read the closest method/form card, then [EVIDENCE_AND_CITATION_PLAYBOOK.md](../EVIDENCE_AND_CITATION_PLAYBOOK.md). Selective loading is expected; do not load all cards for one manuscript.

Each card contains actual experiment order, comparison roles, metric definitions, controls, stress tests, hardware/physical scope, table/caption inheritance and transfer limits. Page numbers refer to the supplied PDF file. These are observations, not official venue rules.

| Card | Form | Method | Experiment pages |
|---|---|---|---|
| [R01 — Fast-Tracker: A Robust Aerial System for Tracking Agile Target in Cluttered Environments](R01.md) | IEEE_COMPACT | tracking, prediction, trajectory_optimization | 5, 6 |
| [R02 — Distributed Swarm Trajectory Optimization for Formation Flight in Dense Environments](R02.md) | IEEE_COMPACT | formation, distributed_planning, trajectory_optimization | 5, 6 |
| [R03 — Bubble Planner: Planning High-speed Smooth Quadrotor Trajectories using Receding Corridors](R03.md) | IEEE_COMPACT | corridor, high_speed_navigation, trajectory_optimization | 6, 7, 8 |
| [R04 — Robust and Efficient Trajectory Planning for Formation Flight in Dense Environments](R04.md) | IEEE_LONG | formation, distributed_planning, trajectory_optimization | 11, 12, 13, 14, 15, 16 |
| [R05 — Catch Planner: Catching High-Speed Targets in the Flight](R05.md) | IEEE_NUMBERED_PREPRINT | catching, high_level_rl, trajectory_optimization | 7, 8, 9 |
| [R06 — Intention-Aware Planner for Robust and Safe Aerial Tracking](R06.md) | IEEE_COMPACT | tracking, intention_prediction, visibility | 6, 7 |
| [R07 — ColAG: A Collaborative Air-Ground Framework for Perception-Limited UGVs’ Navigation](R07.md) | IEEE_COMPACT | air_ground, uncertainty, scheduling | 5, 6 |
| [R08 — Simultaneous Time Synchronization and Mutual Localization for Multi-robot System](R08.md) | IEEE_COMPACT | localization, time_synchronization, optimization | 5, 6 |
| [R09 — Collaborative Planning for Catching and Transporting Objects in Unstructured Environments](R09.md) | IEEE_COMPACT_WITH_SUPPLEMENT | multi_robot, catching, trajectory_optimization | 6, 7, 8, 9 |
| [R10 — Edge Accelerated Robot Navigation With Collaborative Motion Planning](R10.md) | IEEE_LONG | edge_computing, motion_planning, multi_robot | 6, 7, 8, 9, 10 |
| [R11 — Adaptive Tracking and Perching for Quadrotor in Dynamic Scenarios](R11.md) | IEEE_LONG | tracking, perching, visibility, trajectory_optimization | 11, 12, 13, 14, 15, 16, 17 |
| [R12 — Learning Speed Adaptation for Flight in Clutter](R12.md) | IEEE_RAL_HEADER_OBSERVED | high_level_rl, speed_adaptation, navigation | 6, 7 |
| [R13 — Sparse-Graph-Enabled Formation Planning for Large-Scale Aerial Swarms](R13.md) | IEEE_COMPACT | formation, graph_sparsification, scalability | 5, 6, 7 |
| [R14 — Safe and Agile Transportation of Cable-Suspended Payload via Multiple Aerial Robots](R14.md) | IEEE_LONG | payload_transport, planning_control, trajectory_optimization | 12, 13, 14, 15, 16, 17 |
| [R15 — Flying on Point Clouds with Reinforcement Learning](R15.md) | IEEE_COMPACT | direct_control_rl, point_cloud, navigation | 5, 6, 7 |
| [R16 — FLOAT Drone: A Fully-actuated Coaxial Aerial Robot for Close-Proximity Operations](R16.md) | IEEE_COMPACT | fully_actuated_uav, hardware, control | 6, 7 |
| [R17 — Efficient Trajectory Generation Based on Traversable Planes in 3D Complex Architectural Spaces](R17.md) | IEEE_COMPACT | terrain, plane_graph, trajectory_optimization | 5, 6 |
| [R18 — LEMON-Mapping: Loop-Enhanced Large-Scale Multi-Session Point Cloud Merging and Optimization for Globally Consistent Mapping](R18.md) | IEEE_LONG | slam, mapping, multi_session, optimization | 9, 10, 11, 12, 13, 14, 15 |
| [R19 — Shape-Adaptive Planning and Control for a Deformable Quadrotor](R19.md) | IEEE_COMPACT | morphing_uav, planning_control, grasping | 5, 6, 7 |
| [R20 — Reactive Aerobatic Flight via Reinforcement Learning](R20.md) | IEEE_COMPACT | direct_control_rl, aerobatics, curriculum | 6, 7 |
| [R21 — Number Adaptive Formation Flight Planning via Affine Deformable Guidance in Narrow Environments](R21.md) | IEEE_NUMBERED_PREPRINT | formation, number_adaptation, affine_guidance | 6, 7, 8, 9, 10 |
| [R22 — DPNet: Doppler LiDAR Motion Planning for Highly-Dynamic Environments](R22.md) | IEEE_RAL_HEADER_OBSERVED | doppler_lidar, tracking, mpc, dynamic_navigation | 5, 6, 7 |
| [R23 — Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](R23.md) | IEEE_COMPACT | monocular_rgb, direct_control_rl, domain_adaptation | 5, 6, 7 |
| [R24 — USS-Nav: Unified Spatio-Semantic Scene Graph for Lightweight UAV Zero-Shot Object Navigation](R24.md) | IEEE_LETTER_SELF_DESCRIPTION | scene_graph, object_navigation, llm, edge_computing | 6, 7, 8 |
| [R25 — High-Speed Vision-Based Flight in Clutter with Safety-Shielded Reinforcement Learning](R25.md) | IEEE_COMPACT | direct_control_rl, safety_shield, high_speed_navigation | 5, 6, 7 |
| [R26 — NavDreamer: Video Models as Zero-Shot 3D Navigators](R26.md) | SINGLE_COLUMN_NUMERIC_PREPRINT | video_model, navigation, metric_scale, vlm | 5, 6, 7, 8 |
| [R27 — Primitive-based Truncated Diffusion for Efficient Trajectory Generation of Differential Drive Mobile Manipulators](R27.md) | IEEE_COMPACT | diffusion, mobile_manipulator, trajectory_optimization | 6, 7, 8 |
| [R28 — D-VLC: Decentralized Vision-Language Collaboration for Heterogeneous Embodied Multi-Robot Systems in Unknown Environments](R28.md) | TWO_COLUMN_AUTHOR_YEAR_PREPRINT | heterogeneous_multi_robot, vlm, decentralized_exploration | 5, 6, 7 |
| [R29 — Hand-like autonomous flying robot for airborne grasping and interaction](R29.md) | NATURE_COMMUNICATIONS_PUBLISHER | aerial_manipulation, hardware, adaptive_control | 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15 |

Canonical machine-readable file: [profiles.json](profiles.json), schema 1.0, root key `profiles`; join `paper_id` to `papers.json` field `paper` for title/source SHA256.

Validation: `python validate_profiles.py --render-cards`; add `--no-cache` to verify using only bundled PDFs (requires PyMuPDF or pypdf). `--workspace <root>` optionally selects an existing review cache. Checks cover source hashes, PDF-page locators and short source witnesses; they do not certify scientific correctness or final publication metadata.
