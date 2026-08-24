# 09 Section Writing

## Entry

Require a named target section, relevant project evidence, and either a Paper Blueprint or an explicit local-task contract.

## Prepare

1. Copy `templates/SECTION_BRIEF.md`.
2. Load the matching file in `IEEE_TRANS_KNOWLEDGE/02_SECTIONS/`.
3. Load only relevant writing guidance from `05_WRITING/`.
4. Re-route three exemplars for the target section, at most five for a complex section.
5. Load `templates/TERMINOLOGY_LEDGER.md` or create the relevant subset for this section.
6. Record claims, evidence, rules, exemplar roles/boundaries, forbidden overclaims, canonical terminology, allowed new terms, and expected output.

## Draft

- Give each paragraph one scientific function and a visible relation to the section purpose.
- Establish information before using it; keep notation and terminology stable.
- Use the canonical name from the ledger every time the same concept appears; stylistic variation is not a reason to invent an alias.
- Do not introduce a new acronym, symbol, module name, mechanism label, or metric name until it passes the term-admission test and is entered in the ledger.
- Define a permitted new term at first use, then use the same form in prose, equations, algorithms, captions, legends, and tables.
- Prefer concrete actor–action–object sentences; split a sentence when it carries more than one main claim or hides the logical condition.
- Bind claims to evidence or verified references at the correct rhetorical location.
- Use journal and domain profiles to adjust emphasis, not to imitate stock phrasing.
- Use exemplar architecture only; do not copy sentences, transitions, or contribution wording.
- Mark unsupported passages with the approved missing-state label rather than filling them.

## Section-specific rules

- Method/formulation: define object, assumptions, variables, constraints, mechanism, and outputs with traceable logic.
- Experiments: disclose setup and fairness before outcomes.
- Introduction: write after architecture; connect problem, gap, challenge, insight, approach, and contributions.
- Related Work: organize by the boundary needed to establish the gap, not a paper-by-paper list.
- Conclusion: restate only closed claims, limitations, and defensible future work.
- Abstract/title: write last from stabilized problem, gap, mechanism, key results, and conclusion.

## Exit

Run the relevant audit file, including `audits/TERMINOLOGY_CLARITY_AUDIT.md` when the section adds or uses technical terminology. The section must satisfy its brief, contain no fabricated evidence, preserve connections to previous/next sections, and introduce no unlogged aliases.
