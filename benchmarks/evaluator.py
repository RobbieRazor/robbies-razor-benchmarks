"""
Robbie’s Razor Evaluator (v0)

Purpose:
- Provide a simple, reproducible benchmark harness for labs.
- Compute: Accuracy, TPCA (Tokens Per Correct Answer), Overrun Rate.
- Optional: token counting via tiktoken if installed; otherwise uses a deterministic proxy.

References:
- Razor Compliance Framework:
  https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework
- Razor Evaluation Protocol:
  https://www.robbiegeorgephotography.com/robbies-razor-lab-evaluation-protocol

Governed by MRD v1.8 and the Authorship Conservation Rule (ACR).
Author: Robbie George
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


# -----------------------------
# Token counting (tiktoken optional)
# -----------------------------

def try_get_tiktoken_encoder(model_name: str):
    try:
        import tiktoken  # type: ignore
        return tiktoken.encoding_for_model(model_name)
    except Exception:
        return None


def token_count(text: str, encoder=None) -> int:
    """
    Count tokens using tiktoken if available, otherwise fall back to a deterministic proxy.
    Proxy rule: tokens ~= max(1, ceil(len(text)/4)).
    """
    text = text or ""
    if encoder is not None:
        return len(encoder.encode(text))
    # Deterministic proxy: ~4 chars per token
    return max(1, (len(text) + 3) // 4)


# -----------------------------
# Correctness checks
# -----------------------------

def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def is_correct_exact(output: str, acceptable: List[str]) -> bool:
    out = normalize(output)
    return any(out == normalize(a) for a in acceptable)


def is_correct_contains(output: str, acceptable: List[str]) -> bool:
    """
    Fallback correctness mode: checks if any acceptable answer appears as a whole-word substring.
    Use sparingly (only for certain extraction tasks).
    """
    out = normalize(output)
    for a in acceptable:
        a_norm = normalize(a)
        # whole-word-ish match
        if re.search(rf"\b{re.escape(a_norm)}\b", out):
            return True
    return False


def is_correct_numeric(output: str, acceptable: List[str]) -> bool:
    """
    Numeric correctness mode:
    - extracts first number-like token from output
    - compares against acceptable numeric strings
    """
    out = normalize(output)
    m = re.search(r"[-+]?\d+(\.\d+)?", out)
    if not m:
        return False
    found = m.group(0)
    return any(found == normalize(a) for a in acceptable)


# -----------------------------
# Data model
# -----------------------------

@dataclass
class Case:
    id: str
    category: str
    prompt: str
    acceptable_answers: List[str]
    scoring_mode: str = "exact"          # exact | contains | numeric
    target_max_tokens: Optional[int] = None


def load_cases(path: str) -> List[Case]:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    cases: List[Case] = []
    for item in raw:
        cases.append(
            Case(
                id=item["id"],
                category=item.get("category", "Uncategorized"),
                prompt=item["prompt"],
                acceptable_answers=item.get("acceptable_answers", []),
                scoring_mode=item.get("scoring_mode", "exact"),
                target_max_tokens=item.get("target_max_tokens"),
            )
        )
    return cases


def grade_case(case: Case, output: str) -> bool:
    if not case.acceptable_answers:
        # If no answers provided, cannot grade
        return False

    mode = case.scoring_mode.lower().strip()
    if mode == "exact":
        return is_correct_exact(output, case.acceptable_answers)
    if mode == "numeric":
        return is_correct_numeric(output, case.acceptable_answers)
    if mode == "contains":
        return is_correct_contains(output, case.acceptable_answers)

    # default
    return is_correct_exact(output, case.acceptable_answers)


# -----------------------------
# Evaluation
# -----------------------------

def evaluate_outputs(
    cases: List[Case],
    outputs: Dict[str, str],
    encoder=None,
) -> Dict[str, Any]:
    results: List[Dict[str, Any]] = []
    correct_count = 0
    total_tokens = 0
    correct_tokens = 0
    overruns = 0
    overrun_den = 0

    for case in cases:
        out = outputs.get(case.id, "")
        tokens = token_count(out, encoder=encoder)
        ok = grade_case(case, out)

        total_tokens += tokens
        if ok:
            correct_count += 1
            correct_tokens += tokens

        if case.target_max_tokens is not None:
            overrun_den += 1
            if tokens > case.target_max_tokens:
                overruns += 1

        results.append(
            {
                "id": case.id,
                "category": case.category,
                "tokens": tokens,
                "correct": ok,
                "target_max_tokens": case.target_max_tokens,
                "scoring_mode": case.scoring_mode,
            }
        )

    n = len(cases)
    accuracy = (correct_count / n) if n else 0.0
    tpca = (correct_tokens / correct_count) if correct_count else None  # tokens per correct answer
    eor = (overruns / overrun_den) if overrun_den else None  # expression overrun rate

    summary = {
        "num_cases": n,
        "num_correct": correct_count,
        "accuracy": accuracy,
        "tpca": tpca,
        "expression_overrun_rate": eor,
        "total_tokens": total_tokens,
    }

    return {"summary": summary, "results": results}


def write_report(report: Dict[str, Any], out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)


def print_summary(summary: Dict[str, Any]) -> None:
    print("\n=== Robbie’s Razor Evaluator Report (v0) ===\n")
    print(f"Cases:                  {summary['num_cases']}")
    print(f"Correct:                {summary['num_correct']}")
    print(f"Accuracy:               {summary['accuracy']:.2%}")
    if summary["tpca"] is not None:
        print(f"TPCA (tokens/correct):  {summary['tpca']:.2f}")
    else:
        print("TPCA (tokens/correct):  N/A (no correct answers)")
    if summary["expression_overrun_rate"] is not None:
        print(f"Expression overrun rate:{summary['expression_overrun_rate']:.2%}")
    else:
        print("Expression overrun rate:N/A (no token targets set)")
    print(f"Total tokens (all):     {summary['total_tokens']}\n")


def main():
    p = argparse.ArgumentParser(description="Robbie’s Razor Evaluator (v0).")
    p.add_argument("--cases", default="benchmarks/cases/razor_eval_v0.json", help="Path to JSON cases file.")
    p.add_argument("--outputs", required=True, help="Path to JSON outputs mapping {case_id: model_output}.")
    p.add_argument("--model", default="gpt-4", help="Tokenizer model name (tiktoken) if available.")
    p.add_argument("--report-out", default="benchmarks/reports/latest.json", help="Where to write the JSON report.")
    args = p.parse_args()

    cases = load_cases(args.cases)
    with open(args.outputs, "r", encoding="utf-8") as f:
        outputs = json.load(f)

    encoder = try_get_tiktoken_encoder(args.model)
    report = evaluate_outputs(cases, outputs, encoder=encoder)
    write_report(report, args.report_out)
    print_summary(report["summary"])
    print(f"Report written to: {args.report_out}\n")
    if encoder is None:
        print("Note: tiktoken not available; using deterministic token proxy (len(text)/4).\n")


if __name__ == "__main__":
    main()
