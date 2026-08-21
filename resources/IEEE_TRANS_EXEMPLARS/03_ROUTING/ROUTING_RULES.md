# Routing Rules

The score is deterministic and totals 100:

- Domain match: 30 (all requested domains covered = 30; one primary/secondary domain = 20; adjacent domain = 10).
- Role/current-section match: 25 (exact = 25; compatible secondary role = 15).
- Paper-type match: 15 (exact = 15; compatible hybrid = 8).
- Target-journal match: 15 (exact = 15; same domain but different journal = 0, handled by domain score).
- Evidence-need match: 10 (all requested evidence types = 10; partial = 5).
- Formal-rule match: 5 (requested Rule ID linked = 5).

Hard gates: a card with a conflicting `Do Not Generalize` boundary is excluded; a result below 35 is not returned unless fewer than three cards pass. Default return = 3; maximum = 5.
