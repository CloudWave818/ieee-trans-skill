# Retrieval Architecture

## Input contract

Normalize the request into: target journal, research domains, paper type, method type, current writing task, current section, evidence need, and optional Rule IDs.

## Retrieval sequence

1. Filter out cards whose `Do Not Generalize` boundary conflicts with the new paper.
2. Compute the transparent score in `ROUTING_RULES.md` from `EXEMPLAR_ROUTING.csv`.
3. Require at least one primary-role or evidence-need match.
4. Return the top 3 cards by default; return 4–5 only for a genuinely cross-domain or multi-section task.
5. Break ties by higher role match, then domain match, then teaching value. Do not use citation count as a routing feature.

## Context control

Never read all cards. Load only the registry rows first, score them, then open the selected 3–5 cards. Apply knowledge in the order General rule → relevant domains → target journal → exemplar.
