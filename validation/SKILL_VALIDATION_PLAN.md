# Skill Validation Plan

## Gates

1. **Structure** — every required config, workflow, audit, template, script, and validation artifact exists.
2. **Skill format** — `SKILL.md` has valid two-field frontmatter, no TODOs, remains under 500 lines, and passes `skill-creator/scripts/quick_validate.py`.
3. **Upstream contract** — active counts remain 42 rules, 27 cards, and 189 rule links; Corpus, Knowledge, and Exemplars are not rewritten by Phase 4.
4. **Routing** — execute Cases 1–8 plus the RA-L boundary against live registries; verify correct General/Domain/Journal layers, relevant cards, score threshold, default/maximum count, and card boundaries.
5. **Workflow** — verify Mode selection and required workflow entry for every synthetic case.
6. **Safety** — verify missing-state labels, fabrication prohibitions, claim-evidence gate, conflict resolution, user-evidence priority, and readiness criteria are encoded.
7. **Report** — emit `PHASE4_FINAL_VALIDATION.json` and `PHASE4_FINAL_REPORT.md` only after all checks pass.

## Commands

```powershell
python scripts/run_synthetic_tests.py
python scripts/validate_phase4.py
python <skill-creator>/scripts/quick_validate.py .
```

## Completion boundary

Passing Phase 4 proves construction and synthetic behavior only. It does not prove stability on a real manuscript. The only allowed completion status is:

`PHASE 4 IEEE TRANS WRITING SKILL CONSTRUCTED / READY FOR REAL-PAPER VALIDATION`
