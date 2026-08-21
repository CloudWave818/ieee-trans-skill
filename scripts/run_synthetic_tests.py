#!/usr/bin/env python3
"""Run Phase-4 routing and workflow tests and write human-readable reports."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from route_project import KNOWLEDGE, route  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "validation/synthetic_cases.json"
RESULTS = ROOT / "validation/SYNTHETIC_RESULTS.json"


def run_case(case: dict) -> dict:
    expected = case["expected"]
    checks = []
    try:
        result = route(case)
    except ValueError as exc:
        result = {"status": "OUT_OF_SCOPE", "reason": str(exc), "case_id": case["case_id"]}

    def check(name: str, passed: bool, detail: str = ""):
        checks.append({"check": name, "status": "PASS" if passed else "FAIL", "detail": detail})

    expected_status = expected.get("status", "ROUTED")
    check("status", result.get("status") == expected_status, f"actual={result.get('status')} expected={expected_status}")
    if expected_status == "OUT_OF_SCOPE":
        check("ral_boundary", "RA-L" in result.get("reason", ""), result.get("reason", ""))
    else:
        check("mode", result["mode"] == expected["mode"], f"actual={result['mode']} expected={expected['mode']}")
        check("domains", set(expected["domains"]).issubset(result["domains"]), f"actual={result['domains']}")
        check("domain_limit", 2 <= len(result["domains"]) <= 4, str(result["domains"]))
        check("journal", result["target_journal"] == expected["journal"] and result["journal_locked"], result["target_journal"])
        check("journal_profile", Path(result["knowledge"]["journal_profile"]).name == f"{expected['journal']}.md")
        check("general_rules", set(expected["general_rules"]).issubset(result["knowledge"]["general_rule_ids"]), str(result["knowledge"]["general_rule_ids"]))
        check("domain_rules", bool(result["knowledge"]["domain_rule_ids"]), str(result["knowledge"]["domain_rule_ids"]))
        check("journal_rule", result["knowledge"]["journal_rule_ids"] == [f"JRN-{expected['journal']}-001"], str(result["knowledge"]["journal_rule_ids"]))
        check("workflow", expected["workflow"] in result["workflows"], str(result["workflows"]))
        exemplars = result["exemplars"]
        check("default_or_complex_count", len(exemplars) == (5 if case.get("complex_task") or len(result["domains"]) >= 4 or case.get("multi_section") else 3), str(len(exemplars)))
        check("maximum_five", len(exemplars) <= 5, str(len(exemplars)))
        check("unique_exemplars", len({x["exemplar_id"] for x in exemplars}) == len(exemplars))
        check("score_threshold", all(x["score"] >= 35 for x in exemplars), str([(x["exemplar_id"], x["score"]) for x in exemplars]))
        check("role_or_evidence_gate", all(x["score_breakdown"]["role"] > 0 or x["score_breakdown"]["evidence"] > 0 for x in exemplars))
        check("domain_relevance", all(x["score_breakdown"]["domain"] > 0 for x in exemplars), str([(x["exemplar_id"], x["score_breakdown"]["domain"]) for x in exemplars]))
        check("boundary_loaded", all(x["do_not_generalize"] and x["boundary_gate"] == "REVIEW_REQUIRED_BEFORE_USE" for x in exemplars))
        check("no_ral", result["target_journal"] != "RA-L")

        # Verify returned domain and journal rules against the authoritative registry scopes.
        rules = {r["Rule_ID"]: r for r in __import__("route_project").read_csv(KNOWLEDGE / "00_META/RULE_REGISTRY.csv")}
        check("domain_scope_integrity", all(rules[x]["Scope"].split(":", 1)[1] in result["domains"] for x in result["knowledge"]["domain_rule_ids"]))
        check("journal_scope_integrity", all(rules[x]["Scope"] == f"JOURNAL:{result['target_journal']}" for x in result["knowledge"]["journal_rule_ids"]))

    return {
        "case_id": case["case_id"],
        "description": case.get("task", ""),
        "status": "PASS" if all(x["status"] == "PASS" for x in checks) else "FAIL",
        "checks": checks,
        "route": result,
    }


def write_reports(results: list[dict]):
    passed = sum(x["status"] == "PASS" for x in results)
    routing_lines = [
        "# Routing Tests", "",
        "Synthetic tests execute `scripts/route_project.py` against the live Phase-2/3 registries.", "",
        f"Result: **{passed}/{len(results)} cases passed**.", "",
        "| Case | Status | Domains | Journal | Exemplars |",
        "|---|---|---|---|---|",
    ]
    workflow_lines = [
        "# Workflow Tests", "",
        "The same cases verify automatic Mode A–J selection and required workflow entry points.", "",
        f"Result: **{passed}/{len(results)} cases passed**.", "",
        "| Case | Status | Mode | Workflow chain |",
        "|---|---|---|---|",
    ]
    for item in results:
        route_result = item["route"]
        if route_result.get("status") == "OUT_OF_SCOPE":
            routing_lines.append(f"| {item['case_id']} | {item['status']} | excluded | RA-L out of scope | 0 |")
            workflow_lines.append(f"| {item['case_id']} | {item['status']} | excluded | RA-L boundary |")
        else:
            routing_lines.append(f"| {item['case_id']} | {item['status']} | {'; '.join(route_result['domains'])} | {route_result['target_journal']} | {'; '.join(x['exemplar_id'] for x in route_result['exemplars'])} |")
            workflow_lines.append(f"| {item['case_id']} | {item['status']} | {route_result['mode']} | {' → '.join(route_result['workflows'])} |")
    failures = [(item["case_id"], c) for item in results for c in item["checks"] if c["status"] == "FAIL"]
    routing_lines += ["", "## Failure details", ""] + ([f"- {case}: {c['check']} — {c['detail']}" for case, c in failures] or ["- None."])
    workflow_lines += ["", "## Coverage", "", "- Cases 1–5 cover the five required domain/journal combinations.", "- Case 6 covers full-draft revision.", "- Case 7 covers experiment-only routing.", "- Case 8 covers figure-only routing.", "- Case 9 enforces the RA-L boundary."]
    (ROOT / "validation/ROUTING_TESTS.md").write_text("\n".join(routing_lines), encoding="utf-8")
    (ROOT / "validation/WORKFLOW_TESTS.md").write_text("\n".join(workflow_lines), encoding="utf-8")


def main() -> int:
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    results = [run_case(case) for case in cases]
    payload = {
        "overall_status": "PASS" if all(x["status"] == "PASS" for x in results) else "FAIL",
        "cases": len(results),
        "passed": sum(x["status"] == "PASS" for x in results),
        "failed": sum(x["status"] == "FAIL" for x in results),
        "results": results,
    }
    RESULTS.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    write_reports(results)
    print(json.dumps({k: payload[k] for k in ["overall_status", "cases", "passed", "failed"]}, ensure_ascii=False, indent=2))
    return 0 if payload["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
