# Figure/Table Audit

## Checks

- Does every asset answer a scientific question and support a claim?
- Is its evidence role distinct from nearby assets?
- Would deleting it remove information rather than decoration?
- Is a figure used for relationships and a table for exact comparisons/settings appropriately?
- Does the sequence follow the argument and paper type?
- Are axes, units, legends, uncertainty, baselines, and conditions complete and consistent?
- Do captions explain context and encoding without replacing results interpretation?
- Are tables and figures free of duplicated data unless the dual view has a scientific reason?
- Are callouts, numbering, panel labels, and cross-references consistent?
- Do visuals avoid implying unavailable significance, hardware, scenarios, or precision?

## Blockers

Mark `BLOCKER` for misleading encoding, wrong data, missing central evidence, irreproducible comparison conditions, or a visual contradicting the text.

## Output

Return `KEEP`, `REVISE`, `MERGE`, `DELETE`, or `ADD`, plus the evidence role and exact repair.
