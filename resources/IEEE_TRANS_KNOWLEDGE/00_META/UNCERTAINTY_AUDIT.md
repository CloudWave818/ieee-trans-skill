# Uncertainty Audit

`UNKNOWN` is never converted to zero. `ESTIMATED` and `LOWER_BOUND` values remain unsuitable as exact editorial quotas.

| Field | UNKNOWN/blank | ESTIMATED | LOWER_BOUND | A papers |
|---|---:|---:|---:|---:|
| Title | 4 | 0 | 0 | 100 |
| Main_text_pages_status | 0 | 100 | 0 | 100 |
| Number_of_main_sections | 1 | 0 | 0 | 100 |
| Main_section_count_status | 1 | 99 | 0 | 100 |
| Subsection_count_status | 0 | 100 | 0 | 100 |
| Introduction_length_pages | 1 | 0 | 0 | 100 |
| Introduction_length_status | 1 | 99 | 0 | 100 |
| Methodology_length_pages | 81 | 0 | 0 | 100 |
| Methodology_length_status | 81 | 19 | 0 | 100 |
| Theory_section_length_pages | 98 | 0 | 0 | 100 |
| Theory_length_status | 98 | 2 | 0 | 100 |
| Experiment_section_length_pages | 44 | 0 | 0 | 100 |
| Experiment_length_status | 44 | 56 | 0 | 100 |
| Conclusion_length_pages | 28 | 0 | 0 | 100 |
| Conclusion_length_status | 28 | 72 | 0 | 100 |
| Figure_panel_status | 0 | 100 | 0 | 100 |
| Equation_count_status | 0 | 0 | 100 | 100 |
| Baseline_count_status | 0 | 0 | 100 | 100 |
| Contribution_count | 67 | 0 | 0 | 100 |
| Contribution_count_status | 67 | 33 | 0 | 100 |
| Major_claim_count_status | 0 | 100 | 0 | 100 |
| Introduction_rhetorical_sequence | 1 | 0 | 0 | 100 |
| Figure_types_detected | 4 | 0 | 0 | 100 |
| Table_types_detected | 37 | 0 | 0 | 100 |
| Evidence_types_detected | 1 | 0 | 0 | 100 |

## Rule impact

- Baseline and equation counts are lower bounds in all A-level records; no formal rule uses their exact numeric value.
- Figure/table rules use labelled presence or functional catalogs, not exact panel typography.
- Ablation, runtime, generalization, robustness, simulation, and physical evidence are positive-evidence detectors. A false value means no explicit evidence was detected in the bounded extraction region.
- Counterexample entries in the rule registry are candidate counterexamples and require source review before rhetorical use.
- The ablation rule was reclassified to RL/MARL domain scope; robustness remains OPTIONAL; generalization remains OPTIONAL because its eligible sample is small; runtime and physical-validation rules retain MEDIUM confidence; visual progression remains HIGH but explicitly paper-type-conditioned.

## Totals across status-bearing anatomy cells

- UNKNOWN/blank markers: 687
- ESTIMATED markers: 780
- LOWER_BOUND markers: 200
