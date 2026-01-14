"""
tools/dow_compliance_checker.py

Razor Stability Auditor
Audits an AI mission profile against Robbie’s Razor non-negotiables:

1) Compression Gates
2) Memory Integrity
3) Recursion Throttles

Outputs a Stability Score (0–100), GO/NO-GO status, and violations.

Note: This is a *Razor-based risk audit*, not an official government compliance standard.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional
import json


@dataclass(frozen=True)
class MissionProfile:
    mission: str

    # Compression Gates
    enforced_lineage: bool = False                 # lineage/provenance enforced end-to-end
    canonical_schemas: bool = False                # standardized schemas/ontologies enforced
    domain_boundaries_enforced: bool = True        # cross-domain mixing controlled

    # Memory Integrity
    refresh_cycle_days: int = 365                  # model refresh cadence (days)
    reproducible_logs: bool = False                # versioned reasoning logs
    provenance_tags: bool = False                  # citations / sources / provenance metadata

    # Recursion Throttles
    autonomy_scale: float = 1.0                    # 1.0–10.0 (higher = more autonomous behavior)
    tool_call_budgets: bool = False                # explicit tool/call budgets
    stop_conditions: bool = False                  # hard stop rules for loops / runaway behavior
    rollback_rules: bool = False                   # safe rollback procedures


@dataclass(frozen=True)
class AuditConfig:
    # Thresholds tuned to the publicly stated goal of fast deployment
    # while preventing runaway recursion and memory rot.
    high_autonomy_threshold: float = 7.0

    # The DoW AI strategy memo directs enabling deployment of latest models
    # within 30 days of public release. This config flags that cadence as
    # high-risk unless memory integrity controls exist.
    high_risk_refresh_days: int = 30

    # Penalty weights (sum can exceed 100; final score is clamped to 0–100)
    penalty_missing_lineage: int = 30
    penalty_missing_schema: int = 15
    penalty_domain_boundary_off: int = 15

    penalty_fast_refresh_without_memory_controls: int = 25
    penalty_missing_repro_logs: int = 10
    penalty_missing_provenance_tags: int = 10

    penalty_high_autonomy_without_throttles: int = 35
    penalty_missing_tool_budgets: int = 10
    penalty_missing_stop_conditions: int = 10
    penalty_missing_rollback_rules: int = 10

    go_threshold: int = 80


class RazorStabilityAuditor:
    """
    Audits a MissionProfile against Razor non-negotiables.
    Produces a deterministic score + violations list.
    """

    def __init__(self, config: Optional[AuditConfig] = None):
        self.cfg = config or AuditConfig()

    def evaluate(self, profile: MissionProfile) -> Dict[str, Any]:
        score = 100
        violations: List[str] = []

        # 1) Compression Gates
        if not profile.enforced_lineage:
            score -= self.cfg.penalty_missing_lineage
            violations.append("CRITICAL: Missing Compression Gate — enforced lineage/provenance (Failure Point 1)")

        if not profile.canonical_schemas:
            score -= self.cfg.penalty_missing_schema
            violations.append("HIGH RISK: Missing Compression Gate — canonical schemas/ontology alignment (Failure Point 1)")

        if not profile.domain_boundaries_enforced:
            score -= self.cfg.penalty_domain_boundary_off
            violations.append("HIGH RISK: Domain boundary controls off — authority hallucination risk (Failure Point 4)")

        # 2) Memory Integrity
        if profile.refresh_cycle_days <= self.cfg.high_risk_refresh_days:
            # Only penalize heavily if the org is refreshing fast *without* memory controls.
            memory_controls = profile.reproducible_logs and profile.provenance_tags
            if not memory_controls:
                score -= self.cfg.penalty_fast_refresh_without_memory_controls
                violations.append(
                    "HIGH RISK: Fast model refresh cadence without memory controls — institutional amnesia risk (Failure Point 2)"
                )

        if not profile.reproducible_logs:
            score -= self.cfg.penalty_missing_repro_logs
            violations.append("MEDIUM RISK: Reproducible reasoning logs not enforced (Failure Point 2)")

        if not profile.provenance_tags:
            score -= self.cfg.penalty_missing_provenance_tags
            violations.append("MEDIUM RISK: Provenance/citation tags not enforced (Failure Point 4)")

        # 3) Recursion Throttles
        if profile.autonomy_scale >= self.cfg.high_autonomy_threshold:
            throttles_present = profile.tool_call_budgets and profile.stop_conditions and profile.rollback_rules
            if not throttles_present:
                score -= self.cfg.penalty_high_autonomy_without_throttles
                violations.append("CRITICAL: High autonomy without recursion throttles — runaway recursion risk (Failure Point 3)")

        if not profile.tool_call_budgets:
            score -= self.cfg.penalty_missing_tool_budgets
            violations.append("MEDIUM RISK: Tool/call budgets not enforced (Failure Point 3)")

        if not profile.stop_conditions:
            score -= self.cfg.penalty_missing_stop_conditions
            violations.append("MEDIUM RISK: Stop conditions not enforced (Failure Point 3)")

        if not profile.rollback_rules:
            score -= self.cfg.penalty_missing_rollback_rules
            violations.append("MEDIUM RISK: Rollback rules not enforced (Failure Point 2/3)")

        final_score = max(0, min(100, score))
        status = "GO" if final_score >= self.cfg.go_threshold else "NO-GO"

        return {
            "mission": profile.mission,
            "stability_score": final_score,
            "status": status,
            "violations": violations,
            "profile": asdict(profile),
            "config": asdict(self.cfg),
        }


def _demo() -> None:
    # Example mission profile reflecting an "AI-first" push:
    # - fast refresh
    # - high autonomy
    # - weak memory + throttle controls
    profile = MissionProfile(
        mission="AI-First Pilot — Rapid Refresh / High Autonomy",
        enforced_lineage=False,
        canonical_schemas=False,
        domain_boundaries_enforced=False,
        refresh_cycle_days=30,
        reproducible_logs=False,
        provenance_tags=False,
        autonomy_scale=9.0,
        tool_call_budgets=False,
        stop_conditions=False,
        rollback_rules=False,
    )

    auditor = RazorStabilityAuditor()
    report = auditor.evaluate(profile)

    print(f"Audit Report: {report['mission']}")
    print(f"Final Score: {report['stability_score']}/100 | Status: {report['status']}")
    for v in report["violations"]:
        print(f" - {v}")

    # Optional: emit JSON for pipelines
    print("\nJSON:")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    _demo()
