# Journal Routing

## Locked-journal rule

If the user specifies a target, load exactly its profile from `IEEE_TRANS_KNOWLEDGE/07_JOURNALS/` and keep it locked during the manuscript workflow. Change only after an explicit author decision.

Supported core profiles: `TAC`, `TAES`, `TASE`, `TCNS`, `TCST`, `TCYB`, `TIE`, `TIV`, `TMECH`, `TNNLS`, `TRO`, `TSMCS`, and `TVT`. Use `EXTENDED_JOURNALS.md` only for the registered extended set.

`RA-L` and short Letters are supported through `config/RAL.md`, with `article_form=LETTER` and a source-matched compact blueprint. The historical embedded registry contains no RA-L rule; leave that journal-rule list empty and load the local overlay. Never impose Transactions medians or long-paper section budgets on this route.

## When the journal is undecided

Recommend two to four candidates from paper type, theory level, experiment level, application, method contribution, and physical validation. Separate recommendation from writing: present trade-offs, ask the user to select, then lock one profile before journal-specific drafting.

## Evidence tendencies, not mandates

- Theory/control-led profiles may emphasize visible assumptions, stability/convergence, and controlled simulation.
- System-oriented profiles may emphasize implementation, physical validation, runtime, and engineering feasibility.
- Apply only the active `JOURNAL:*` rule from the rule registry; do not infer journal requirements from a corpus frequency alone.
- Use medians and IQRs as planning anchors, never submission-format requirements. Verify current official author instructions separately when formatting or page-limit accuracy matters.
