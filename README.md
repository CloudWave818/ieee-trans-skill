# ieee-trans-skill

A portable Codex skill for planning, drafting, auditing, and revising long-form IEEE Transactions manuscripts in UAV autonomy, robotics, navigation and planning, trajectory optimization, reinforcement learning, multi-agent decision making, and control.

The repository contains the skill plus its compact derived Knowledge and Exemplar resources. It intentionally does **not** contain the 120 source-paper PDFs.

## Install on Windows

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills\ieee-trans-skill"
git clone https://github.com/CloudWave818/ieee-trans-skill.git $dest
```

Restart Codex after installation. Then invoke it explicitly, for example:

```text
Use $ieee-trans-skill to design the claim-evidence architecture for my T-RO paper.
```

## Update

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills\ieee-trans-skill"
git -C $dest pull
```

## Verify

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills\ieee-trans-skill"
python "$dest\scripts\run_synthetic_tests.py"
```

Expected result: all synthetic routing cases pass.

## Data layout

- `SKILL.md`: skill entry point and operating contract.
- `resources/IEEE_TRANS_KNOWLEDGE`: generalized rules and profiles.
- `resources/IEEE_TRANS_EXEMPLARS`: bounded teaching cards and routing metadata.
- `workflows`, `audits`, and `templates`: task execution assets.
- `scripts`: deterministic router and validation tools.

Original PDFs remain local and separate for copyright and repository-size reasons. Routine skill use does not require them.
