#!/usr/bin/env python3
"""Deterministically route an IEEE Transactions paper project.

The router selects knowledge paths, active rules, a journal overlay, workflows,
and three to five exemplar cards.  It never writes upstream assets.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def resolve_data_root() -> Path:
    """Prefer the portable embedded data, then support the legacy workspace."""
    candidates = [SKILL_ROOT / "resources", SKILL_ROOT.parent]
    for root in candidates:
        if (root / "IEEE_TRANS_KNOWLEDGE").is_dir() and (root / "IEEE_TRANS_EXEMPLARS").is_dir():
            return root
    return candidates[0]


DATA_ROOT = resolve_data_root()
KNOWLEDGE = DATA_ROOT / "IEEE_TRANS_KNOWLEDGE"
EXEMPLARS = DATA_ROOT / "IEEE_TRANS_EXEMPLARS"

ALLOWED_DOMAINS = [
    "UAV_AUTONOMY", "ROBOTICS", "NAVIGATION_PLANNING",
    "TRAJECTORY_OPTIMIZATION", "RL_MARL", "MULTI_AGENT_DECISION", "CONTROL",
]

DOMAIN_PATTERNS = {
    "UAV_AUTONOMY": [r"\buav\b", r"drone", r"aerial", r"quadrotor", r"无人机"],
    "ROBOTICS": [r"robot", r"manipulator", r"\bslam\b", r"机器人"],
    "NAVIGATION_PLANNING": [r"navigation", r"path planning", r"exploration", r"obstacle avoidance", r"导航", r"路径规划"],
    "TRAJECTORY_OPTIMIZATION": [r"trajectory", r"motion optimization", r"optimal motion", r"轨迹"],
    "RL_MARL": [r"reinforcement learning", r"deep rl", r"\bdrl\b", r"\bmarl\b", r"q-learning", r"policy learning", r"强化学习"],
    "MULTI_AGENT_DECISION": [r"multi[- ]agent", r"swarm", r"cooperative", r"pursuit", r"game[- ]theoretic", r"多智能体", r"集群", r"博弈"],
    "CONTROL": [r"control", r"controller", r"adaptive", r"distributed control", r"stability", r"\bmpc\b", r"tracking", r"控制"],
}

ADJACENT = {
    "UAV_AUTONOMY": ["NAVIGATION_PLANNING", "CONTROL"],
    "ROBOTICS": ["NAVIGATION_PLANNING", "CONTROL"],
    "NAVIGATION_PLANNING": ["ROBOTICS", "TRAJECTORY_OPTIMIZATION"],
    "TRAJECTORY_OPTIMIZATION": ["CONTROL", "NAVIGATION_PLANNING"],
    "RL_MARL": ["CONTROL", "MULTI_AGENT_DECISION"],
    "MULTI_AGENT_DECISION": ["CONTROL", "RL_MARL"],
    "CONTROL": ["TRAJECTORY_OPTIMIZATION", "MULTI_AGENT_DECISION"],
}

JOURNALS = {"TAC", "TAES", "TASE", "TCNS", "TCST", "TCYB", "TIE", "TIV", "TMECH", "TNNLS", "TRO", "TSMCS", "TVT"}
RAL_ALIASES = {"RAL", "RA-L", "IEEE RA-L", "IEEE ROBOTICS AND AUTOMATION LETTERS"}

MODE_WORKFLOWS = {
    "A": ["01_PROJECT_DIAGNOSIS", "02_RESEARCH_ARCHITECTURE", "03_CONTRIBUTION_DESIGN", "04_CLAIM_EVIDENCE_DESIGN", "05_EXPERIMENT_DESIGN", "06_FIGURE_TABLE_DESIGN", "07_PAGE_BUDGET", "08_SECTION_OUTLINE"],
    "B": ["01_PROJECT_DIAGNOSIS", "02_RESEARCH_ARCHITECTURE", "03_CONTRIBUTION_DESIGN", "04_CLAIM_EVIDENCE_DESIGN", "05_EXPERIMENT_DESIGN", "08_SECTION_OUTLINE"],
    "C": ["01_PROJECT_DIAGNOSIS", "04_CLAIM_EVIDENCE_DESIGN", "10_RESULTS_INTERPRETATION", "06_FIGURE_TABLE_DESIGN", "08_SECTION_OUTLINE"],
    "D": ["01_PROJECT_DIAGNOSIS", "11_FULL_PAPER_INTEGRATION", "09_SECTION_WRITING", "12_FINAL_AUDIT"],
    "E": ["01_PROJECT_DIAGNOSIS", "04_CLAIM_EVIDENCE_DESIGN", "05_EXPERIMENT_DESIGN"],
    "F": ["01_PROJECT_DIAGNOSIS", "04_CLAIM_EVIDENCE_DESIGN", "06_FIGURE_TABLE_DESIGN"],
    "G": ["01_PROJECT_DIAGNOSIS", "07_PAGE_BUDGET", "08_SECTION_OUTLINE", "12_FINAL_AUDIT"],
    "H": ["01_PROJECT_DIAGNOSIS", "12_FINAL_AUDIT"],
    "I": ["01_PROJECT_DIAGNOSIS", "09_SECTION_WRITING"],
    "J": ["01_PROJECT_DIAGNOSIS", "11_FULL_PAPER_INTEGRATION", "12_FINAL_AUDIT"],
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def split_set(value: object) -> set[str]:
    return {x.strip() for x in re.split(r"[;|,]", str(value or "")) if x.strip()}


def normalized_text(project: dict) -> str:
    keys = ["title", "description", "research_problem", "paper_type", "method_type", "application_system", "task", "current_section"]
    parts = [str(project.get(k, "")) for k in keys]
    parts.extend(str(x) for x in project.get("keywords", []))
    return " ".join(parts).lower()


def select_domains(project: dict) -> tuple[list[str], dict[str, int]]:
    explicit = [str(x).upper().strip() for x in project.get("domains", [])]
    explicit = [x for x in explicit if x in ALLOWED_DOMAINS]
    text = normalized_text(project)
    scores = {d: 0 for d in ALLOWED_DOMAINS}
    for i, domain in enumerate(explicit):
        scores[domain] += 100 - i
    for domain, patterns in DOMAIN_PATTERNS.items():
        scores[domain] += 10 * sum(bool(re.search(p, text, re.I)) for p in patterns)
    ranked = sorted(ALLOWED_DOMAINS, key=lambda d: (-scores[d], ALLOWED_DOMAINS.index(d)))
    chosen = [d for d in ranked if scores[d] > 0][:4]
    if not chosen:
        chosen = ["ROBOTICS", "CONTROL"]
    if len(chosen) == 1:
        for adjacent in ADJACENT[chosen[0]]:
            if adjacent not in chosen:
                chosen.append(adjacent)
                break
    return chosen[:4], scores


def normalize_journal(value: object) -> str:
    journal = str(value or "").strip().upper().replace("IEEE TRANSACTIONS ON ", "")
    if journal in RAL_ALIASES or journal.replace("-", "") == "RAL":
        raise ValueError("RA-L is outside this long-form IEEE Transactions skill.")
    return journal if journal in JOURNALS else "UNDECIDED"


def journal_candidates(domains: list[str], project: dict) -> list[str]:
    text = normalized_text(project)
    candidates: list[str] = []
    if "CONTROL" in domains and re.search(r"theor|stability|convergence|distributed control", text):
        candidates += ["TAC", "TCNS", "TCST"]
    if "RL_MARL" in domains or "MULTI_AGENT_DECISION" in domains:
        candidates += ["TCYB", "TNNLS", "TSMCS"]
    if "ROBOTICS" in domains or "NAVIGATION_PLANNING" in domains:
        candidates += ["TRO", "TMECH", "TIE", "TASE"]
    if re.search(r"vehicle|vehicular", text):
        candidates += ["TIV", "TVT"]
    if "UAV_AUTONOMY" in domains:
        candidates += ["TRO", "TAES", "TVT"]
    result = []
    for j in candidates or ["TRO", "TCST", "TIE"]:
        if j not in result:
            result.append(j)
    return result[:4]


def select_mode(project: dict) -> str:
    task = f"{project.get('task','')} {project.get('current_section','')}".lower()
    state = str(project.get("manuscript_state", "IDEA_ONLY")).upper()
    if re.search(r"reviewer|peer review|审稿", task): return "H"
    if re.search(r"journal fit|journal adaptation|venue|期刊适配|选刊", task): return "G"
    if re.search(r"figure|table|visual|图表|作图|表格", task): return "F"
    if re.search(r"experiment design|design experiment|实验设计|experiments? only", task): return "E"
    if re.search(r"revis|improv|修改|润色全文", task) or state in {"REVISION", "FULL_DRAFT", "DRAFT_PARTIAL"}: return "D"
    if re.search(r"introduction|related work|method section|problem formulation|abstract|conclusion|section|章节|引言", task): return "I"
    if re.search(r"full paper integration|integrate manuscript|全文整合", task): return "J"
    if re.search(r"result", task) or state == "EXPERIMENT_COMPLETE": return "C"
    if re.search(r"method|architecture|contribution|paper plan|论文架构", task) or state in {"METHOD_READY", "EXPERIMENT_PARTIAL"}: return "B"
    return "A"


def requested_roles(project: dict, mode: str) -> list[str]:
    task = f"{project.get('task','')} {project.get('current_section','')}".lower()
    roles: list[str] = []
    mapping = [
        (r"introduction|引言", ["INTRODUCTION"]),
        (r"problem formulation|formulation|问题建模", ["PROBLEM_FORMULATION"]),
        (r"method|mechanism|方法", ["METHODOLOGY"]),
        (r"theor|proof|stability|convergence|理论", ["THEORY"]),
        (r"experiment|实验", ["EXPERIMENT_ARCHITECTURE", "COMPARATIVE_EXPERIMENT"]),
        (r"figure|visual|图", ["FIGURE_ARCHITECTURE", "FIGURE"]),
        (r"table|表", ["TABLE_ARCHITECTURE", "TABLE"]),
        (r"result|结果", ["RESULT_NARRATIVE"]),
        (r"real[- ]world|physical|hardware|实机", ["REAL_WORLD_VALIDATION", "REAL_WORLD"]),
        (r"control|控制", ["CONTROL"]),
        (r"planning|navigation|规划|导航", ["PLANNING", "NAVIGATION_PLANNING"]),
        (r"multi[- ]agent|marl|多智能体", ["MULTI_AGENT", "RL_MARL"]),
        (r"trajectory|轨迹", ["TRAJECTORY_OPTIMIZATION"]),
        (r"uav|drone|无人机", ["UAV"]),
    ]
    for pattern, additions in mapping:
        if re.search(pattern, task):
            roles.extend(additions)
    defaults = {
        "A": ["PROBLEM_FORMULATION", "METHODOLOGY"], "B": ["METHODOLOGY", "PROBLEM_FORMULATION"],
        "C": ["RESULT_NARRATIVE", "EXPERIMENT_ARCHITECTURE"], "D": ["STRUCTURE", "RESULT_NARRATIVE"],
        "E": ["EXPERIMENT_ARCHITECTURE"], "F": ["FIGURE_ARCHITECTURE", "TABLE_ARCHITECTURE"],
        "G": ["STRUCTURE"], "H": ["STRUCTURE", "RESULT_NARRATIVE"],
        "I": ["STRUCTURE"], "J": ["STRUCTURE", "RESULT_NARRATIVE"],
    }
    roles.extend(defaults[mode])
    return list(dict.fromkeys(roles))


def select_rules(project: dict, domains: list[str], journal: str, rules: list[dict[str, str]]) -> dict[str, list[str]]:
    text = normalized_text(project)
    evidence = {str(x).upper() for x in project.get("evidence_needs", [])}
    general: list[str] = []
    if re.search(r"formulation|theor|control|trajectory|architecture|建模|理论|控制|轨迹", text): general.append("GEN-ARCH-001")
    if re.search(r"experiment|simulation|system|learning|robot|uav|vehicle|实验|仿真", text): general.append("GEN-EVD-001")
    if evidence & {"RUNTIME", "COMPUTATIONAL_COMPLEXITY", "SCALABILITY"} or re.search(r"runtime|latency|efficient|real[- ]time|online|运行时间|实时", text): general.append("GEN-EVD-002")
    if "ROBUSTNESS" in evidence or re.search(r"robust|disturbance|noise|uncertainty|鲁棒", text): general.append("GEN-EVD-004")
    if "GENERALIZATION" in evidence or re.search(r"generalization|cross[- ]scenario|transfer|泛化", text): general.append("GEN-EVD-005")
    if evidence & {"REAL_WORLD", "SIM_TO_REAL"} or re.search(r"physical|hardware|real[- ]world|deployment|实机|部署", text): general.append("GEN-EVD-006")
    if re.search(r"figure|visual|trajectory|spatial|system|robot|uav|图|轨迹", text): general.append("GEN-VIS-001")
    requested = [str(x) for x in project.get("rule_ids", [])]
    general.extend(x for x in requested if x.startswith("GEN-"))
    valid_ids = {r["Rule_ID"] for r in rules}
    general = [x for x in dict.fromkeys(general) if x in valid_ids]
    domain_ids = [r["Rule_ID"] for r in rules if r["Scope"].startswith("DOMAIN:") and r["Scope"].split(":", 1)[1] in domains]
    journal_ids = [r["Rule_ID"] for r in rules if r["Scope"] == f"JOURNAL:{journal}"]
    return {"general": general, "domain": domain_ids, "journal": journal_ids}


def resolve_card_path(card_path: str, exemplar_id: str) -> Path:
    path = Path(card_path)
    if path.is_file():
        return path
    return EXEMPLARS / "01_CARDS" / f"{exemplar_id}.md"


def extract_boundary(card_path: str, exemplar_id: str) -> str:
    path = resolve_card_path(card_path, exemplar_id)
    if not path.is_file(): return "MISSING_INPUT: exemplar card unavailable"
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?ms)^## Do Not Generalize\s+(.*?)(?=^## |\Z)", text)
    return re.sub(r"\s+", " ", match.group(1)).strip() if match else "NEEDS_AUTHOR_DECISION: boundary not found"


def score_exemplars(project: dict, domains: list[str], journal: str, mode: str, selected_rules: dict[str, list[str]], routes: list[dict[str, str]], registry: list[dict[str, str]]) -> list[dict]:
    roles = set(requested_roles(project, mode))
    evidence = {str(x).upper() for x in project.get("evidence_needs", [])}
    requested_rule_ids = set(project.get("rule_ids", [])) | set(selected_rules["general"]) | set(selected_rules["journal"])
    requested_domains = set(domains)
    paper_type = str(project.get("paper_type", "")).strip().lower()
    registry_by_id = {r["Exemplar_ID"]: r for r in registry}
    excluded = set(project.get("excluded_exemplar_ids", []))
    scored = []
    for row in routes:
        ex_id = row["Exemplar_ID"]
        if ex_id in excluded: continue
        card_domains = split_set(row["Domain_Tokens"])
        card_roles = split_set(row["Role_Tokens"])
        card_evidence = split_set(row["Evidence_Needs"])
        card_rules = split_set(row["Rule_IDs"])
        overlap = requested_domains & card_domains
        if requested_domains and requested_domains <= card_domains:
            domain_score = 30
        elif overlap:
            domain_score = 20
        elif any(set(ADJACENT[d]) & card_domains for d in requested_domains):
            domain_score = 10
        else:
            domain_score = 0
        primary_role = registry_by_id.get(ex_id, {}).get("Primary_Role", "")
        if primary_role in roles:
            role_score = 25
        elif roles & card_roles:
            role_score = 15
        else:
            role_score = 0
        route_type = row["Paper_Type"].lower()
        if paper_type and paper_type == route_type:
            paper_score = 15
        elif paper_type and (set(re.findall(r"[a-z]+", paper_type)) & set(re.findall(r"[a-z]+", route_type)) - {"paper", "method"}):
            paper_score = 8
        else:
            paper_score = 0
        journal_score = 15 if journal != "UNDECIDED" and row["Journal"] == journal else 0
        if evidence and evidence <= card_evidence:
            evidence_score = 10
        elif evidence & card_evidence:
            evidence_score = 5
        else:
            evidence_score = 0
        rule_score = 5 if requested_rule_ids & card_rules else 0
        total = domain_score + role_score + paper_score + journal_score + evidence_score + rule_score
        role_or_evidence_gate = role_score > 0 or evidence_score > 0
        if not role_or_evidence_gate: continue
        resolved_card_path = resolve_card_path(registry_by_id.get(ex_id, {}).get("Card_Path", ""), ex_id)
        scored.append({
            "exemplar_id": ex_id,
            "paper_id": registry_by_id.get(ex_id, {}).get("Paper_ID", ""),
            "title": registry_by_id.get(ex_id, {}).get("Title", ""),
            "journal": row["Journal"],
            "score": total,
            "score_breakdown": {"domain": domain_score, "role": role_score, "paper_type": paper_score, "journal": journal_score, "evidence": evidence_score, "rule": rule_score},
            "matched_domains": sorted(overlap),
            "matched_roles": sorted(roles & card_roles),
            "matched_evidence": sorted(evidence & card_evidence),
            "card_path": str(resolved_card_path),
            "do_not_generalize": extract_boundary(registry_by_id.get(ex_id, {}).get("Card_Path", ""), ex_id),
            "boundary_gate": "REVIEW_REQUIRED_BEFORE_USE",
        })
    scored.sort(key=lambda x: (-x["score"], -x["score_breakdown"]["role"], -x["score_breakdown"]["domain"], x["exemplar_id"]))
    passing = [x for x in scored if x["score"] >= 35]
    pool = passing if len(passing) >= 3 else scored
    complex_task = bool(project.get("complex_task")) or len(domains) >= 4 or bool(project.get("multi_section"))
    count = 5 if complex_task else 3
    return pool[: min(count, 5)]


def route(project: dict) -> dict:
    required = [KNOWLEDGE / "00_META/RULE_REGISTRY.csv", EXEMPLARS / "00_META/EXEMPLAR_ROUTING.csv", EXEMPLARS / "00_META/EXEMPLAR_REGISTRY.csv"]
    missing = [str(p) for p in required if not p.is_file()]
    if missing:
        return {"status": "MISSING_INPUT", "missing": missing}
    journal = normalize_journal(project.get("target_journal"))
    domains, domain_scores = select_domains(project)
    mode = select_mode(project)
    rules = read_csv(required[0])
    selected_rules = select_rules(project, domains, journal, rules)
    candidates = journal_candidates(domains, project) if journal == "UNDECIDED" else [journal]
    journal_profile = str(KNOWLEDGE / "07_JOURNALS" / f"{journal}.md") if journal != "UNDECIDED" else "NEEDS_AUTHOR_DECISION"
    routes = read_csv(required[1]); registry = read_csv(required[2])
    selected_cards = score_exemplars(project, domains, journal, mode, selected_rules, routes, registry)
    missing_states = []
    if journal == "UNDECIDED": missing_states.append({"state": "NEEDS_AUTHOR_DECISION", "item": "Target journal", "options": candidates})
    if not str(project.get("research_problem", "")).strip(): missing_states.append({"state": "MISSING_INPUT", "item": "Primary scientific problem"})
    return {
        "status": "ROUTED",
        "case_id": project.get("case_id", "UNSPECIFIED"),
        "mode": mode,
        "manuscript_state": str(project.get("manuscript_state", "IDEA_ONLY")).upper(),
        "domains": domains,
        "domain_signal_scores": {d: domain_scores[d] for d in domains},
        "target_journal": journal,
        "journal_locked": journal != "UNDECIDED",
        "journal_candidates": candidates,
        "knowledge": {
            "general_rule_ids": selected_rules["general"],
            "domain_rule_ids": selected_rules["domain"],
            "journal_rule_ids": selected_rules["journal"],
            "domain_profiles": [str(KNOWLEDGE / "06_DOMAINS" / f"{d}.md") for d in domains],
            "journal_profile": journal_profile,
            "conflict_resolution": str(KNOWLEDGE / "08_SYNTHESIS/CONFLICT_RESOLUTION.md"),
        },
        "requested_roles": requested_roles(project, mode),
        "workflows": MODE_WORKFLOWS[mode],
        "exemplars": selected_cards,
        "exemplar_count": len(selected_cards),
        "default_exemplar_count": 3,
        "maximum_exemplar_count": 5,
        "missing_states": missing_states,
        "constraints": [
            "Read each selected card's Do Not Generalize boundary before use.",
            "Use user project evidence before corpus or exemplar content.",
            "Do not treat corpus statistics as quotas.",
            "Do not fabricate missing scientific evidence.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="UTF-8 JSON project profile")
    parser.add_argument("--output", help="Optional UTF-8 JSON output path")
    args = parser.parse_args()
    project = json.loads(Path(args.input).read_text(encoding="utf-8"))
    try:
        result = route(project)
    except ValueError as exc:
        result = {"status": "OUT_OF_SCOPE", "reason": str(exc), "case_id": project.get("case_id", "UNSPECIFIED")}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered)
    return 0 if result["status"] in {"ROUTED", "OUT_OF_SCOPE"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
