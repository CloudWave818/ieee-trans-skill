# 12 Final Audit

## Entry

Use after architecture or manuscript integration, and directly for Mode H.

## Audit pipeline

Run in order:

1. `audits/SCIENTIFIC_LOGIC_AUDIT.md`
2. `audits/CONTRIBUTION_AUDIT.md`
3. `audits/CLAIM_EVIDENCE_AUDIT.md`
4. `audits/EXPERIMENT_AUDIT.md`
5. `audits/FIGURE_TABLE_AUDIT.md`
6. `audits/JOURNAL_FIT_AUDIT.md`
7. `audits/WRITING_STYLE_AUDIT.md` and `audits/AI_WRITING_AUDIT.md`
8. `audits/REVIEWER_AUDIT.md`

## Severity

- `BLOCKER`: invalidates central novelty, logic, evidence, fairness, or truthfulness.
- `MAJOR`: likely rejection risk affecting a primary claim or venue fit.
- `MODERATE`: meaningful weakness with bounded scientific impact.
- `MINOR`: local clarity, consistency, or presentation issue.

For every finding record evidence location, affected claim/contribution, required action, owner, and verification method in `templates/FINAL_AUDIT_REPORT.md`.

## Decision rules

- `PAPER ARCHITECTURE READY`: no architecture blocker; provisional or planned evidence remains explicitly labeled.
- `SUBMISSION-LEVEL DRAFT`: no blocker and every major scientific claim has closed evidence; journal fit and reproducibility risks are resolved or transparently bounded.
- `NOT READY`: any blocker, fabricated/ambiguous evidence, missing central baseline, or unsupported major claim remains.

English fluency cannot change readiness. Ask: “If the target were rejection, where is the easiest defensible attack?” Feed that attack into a revision loop and rerun affected audits.
