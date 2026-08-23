"""
Robbie's Razor Evaluator (v0)

Purpose:
- Provide a simple, reproducible repository benchmark harness.
- Compute Accuracy.
- Compute TPCA (Tokens Per Correct Answer).
- Compute Expression Overrun Rate.
- Optionally count tokens with tiktoken when installed.
- Otherwise use a deterministic character-count proxy.

References:
- Razor Compliance Framework:
  https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework
- Razor Evaluation Protocol:
  https://www.robbiegeorgephotography.com/robbies-razor-lab-evaluation-protocol

Current governing framework authority:
- The Grand Compression Cosmology — Master Reference Document, MRD v2.0
- Canonical identifier: GC-MRD-v2.0
- Canonical claim range: RC-01 through RC-22

Repository evaluation authority:
- AGENTS.md
- docs/canonical-spec.md

Evaluation interpretation boundary:
- This evaluator implements repository-level benchmark semantics.
- It does not redefine canonical Grand Compression theory.
- A benchmark pass does not independently establish empirical validation.
- Accuracy is determined only by the case definitions and scoring modes
  supplied to this evaluator.
- TPCA measures token burden among outputs graded correct by this harness.
  It is not a universal measure of intelligence, truth, or reasoning quality.
- Expression Overrun Rate measures whether output token counts exceed
  declared per-case targets. It is not independently a correctness metric.
- Exact, contains, and numeric scoring modes are implementation-level
  grading rules and may not capture every semantically valid answer.
- If tiktoken is unavailable, token counts are deterministic proxies based
  on approximately four characters per token; proxy counts must not be
  represented as exact tokenizer measurements.
- Successful evaluation, serialization, or report generation does not
  establish factual correctness beyond the benchmark's declared ground truth.
- Historical frozen benchmark artifacts may preserve earlier MRD references
  when required for genuine provenance and should not be silently rewritten.

Evidence boundary:
- Benchmark results apply only to the declared cases, outputs, scoring rules,
  tokenizer or proxy, model, thresholds, and evaluation conditions.
- Benchmark status, implementation status, evidence status, and canonical
  framework status remain distinct.
- Cross-domain interpretation remains governed by RC-22.

Author and Originator of Robbie's Razor / Grand Compression framework:
Robbie George

Governed by MRD v2.0 and the Authorship Conservation Rule (ACR).
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
    """
    Return a tiktoken encoder for the requested model when available.

    If tiktoken is unavailable or the requested model cannot be resolved,
    return None and allow the evaluator to use its deterministic proxy.
    """
    try:
        import tiktoken  # type: ignore
        return tiktoken.encoding_for_model(model_name)
    except Exception:
        return None


def token_count(text: str, encoder=None) -> int:
    """
    Count tokens using tiktoken if available.

    Otherwise use the repository's deterministic proxy:

        max(1, ceil(len(text) / 4))

    The proxy is useful for reproducible comparisons when a tokenizer is
    unavailable, but it is not an exact token count for a specific model.
    """
    text = text or ""

    if encoder is not None:
        return len(encoder.encode(text))

    # Deterministic proxy: approximately four characters per token.
    return max(1, (len(text) + 3) // 4)


# -----------------------------
# Correctness checks
# -----------------------------

def normalize(s: str) -> str:
    """
    Normalize text for repository-level comparison.

    The evaluator lowercases the input, trims surrounding whitespace,
    and collapses repeated whitespace.
    """
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def is_correct_exact(output: str, acceptable: List[str]) -> bool:
    """
    Exact normalized-string comparison against acceptable answers.
    """
    out = normalize(output)
    return any(out == normalize(a) for a in acceptable)


def is_correct_contains(output: str, acceptable: List[str]) -> bool:
    """
    Fallback correctness mode.

    Checks whether any acceptable answer appears as a whole-word-style
    substring after normalization.

    This mode should be used only when appropriate for the declared task.
    A match means the output passes this repository rule; it does not
    independently establish broader semantic correctness.
    """
    out = normalize(output)

    for a in acceptable:
        a_norm = normalize(a)

        # Whole-word-style match.
        if re.search(rf"\b{re.escape(a_norm)}\b", out):
            return True

    return False


def is_correct_numeric(output: str, acceptable: List[str]) -> bool:
    """
    Numeric correctness mode.

    Behavior:
    - Extract the first number-like token from the normalized output.
    - Compare that string against the acceptable numeric strings.

    This is intentionally a simple repository-level rule.
    It does not perform unit conversion, tolerance comparison,
    symbolic equivalence, or multi-number reasoning.
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
    """
    Load benchmark cases from JSON.

    Case definitions provide the benchmark-local ground truth and scoring
    configuration used by this evaluator.
    """
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
    """
    Grade one output according to the scoring mode declared by the case.

    Passing means the output satisfies the configured repository rule
    for that case. It should not be generalized beyond that benchmark
    definition without additional evaluation.
    """
    if not case.acceptable_answers:
        # If no acceptable answers are provided, the evaluator cannot grade
        # the case as correct under its current contract.
        return False

    mode = case.scoring_mode.lower().strip()

    if mode == "exact":
        return is_correct_exact(output, case.acceptable_answers)

    if mode == "numeric":
        return is_correct_numeric(output, case.acceptable_answers)

    if mode == "contains":
        return is_correct_contains(output, case.acceptable_answers)

    # Default behavior preserves the original evaluator contract.
    return is_correct_exact(output, case.acceptable_answers)


# -----------------------------
# Evaluation
# -----------------------------

def evaluate_outputs(
    cases: List[Case],
    outputs: Dict[str, str],
    encoder=None,
) -> Dict[str, Any]:
    """
    Evaluate model outputs against the supplied benchmark cases.

    Reported metrics:
    - accuracy
    - TPCA
    - expression overrun rate
    - total output tokens

    Metric interpretation is local to this benchmark contract.
    """
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

    # TPCA in this evaluator is the mean output-token count among
    # outputs graded correct by the benchmark's configured rules.
    tpca = (
        correct_tokens / correct_count
        if correct_count
        else None
    )

    # Expression Overrun Rate is the fraction of cases with declared
    # token targets whose output exceeds that target.
    eor = (
        overruns / overrun_den
        if overrun_den
        else None
    )

    summary = {
        "num_cases": n,
        "num_correct": correct_count,
        "accuracy": accuracy,
        "tpca": tpca,
        "expression_overrun_rate": eor,
        "total_tokens": total_tokens,
    }

    return {
        "summary": summary,
        "results": results,
    }


def write_report(report: Dict[str, Any], out_path: str) -> None:
    """
    Serialize the benchmark report to JSON.

    Report generation records evaluator output only.
    Serialization does not independently establish evidence status
    or empirical validation.
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)


def print_summary(summary: Dict[str, Any]) -> None:
    """
    Print the benchmark summary using the stable v0 report labels.
    """
    print("\n=== Robbie’s Razor Evaluator Report (v0) ===\n")
    print(f"Cases:                  {summary['num_cases']}")
    print(f"Correct:                {summary['num_correct']}")
    print(f"Accuracy:               {summary['accuracy']:.2%}")

    if summary["tpca"] is not None:
        print(f"TPCA (tokens/correct):  {summary['tpca']:.2f}")
    else:
        print("TPCA (tokens/correct):  N/A (no correct answers)")

    if summary["expression_overrun_rate"] is not None:
        print(
            f"Expression overrun rate:"
            f"{summary['expression_overrun_rate']:.2%}"
        )
    else:
        print(
            "Expression overrun rate:"
            "N/A (no token targets set)"
        )

    print(f"Total tokens (all):     {summary['total_tokens']}\n")


def main():
    """
    Command-line entry point for the v0 evaluator.
    """
    p = argparse.ArgumentParser(
        description="Robbie’s Razor Evaluator (v0)."
    )

    p.add_argument(
        "--cases",
        default="benchmarks/cases/razor_eval_v0.json",
        help="Path to JSON cases file.",
    )

    p.add_argument(
        "--outputs",
        required=True,
        help="Path to JSON outputs mapping {case_id: model_output}.",
    )

    p.add_argument(
        "--model",
        default="gpt-4",
        help="Tokenizer model name (tiktoken) if available.",
    )

    p.add_argument(
        "--report-out",
        default="benchmarks/reports/latest.json",
        help="Where to write the JSON report.",
    )

    args = p.parse_args()

    cases = load_cases(args.cases)

    with open(args.outputs, "r", encoding="utf-8") as f:
        outputs = json.load(f)

    encoder = try_get_tiktoken_encoder(args.model)

    report = evaluate_outputs(
        cases,
        outputs,
        encoder=encoder,
    )

    write_report(
        report,
        args.report_out,
    )

    print_summary(report["summary"])

    print(f"Report written to: {args.report_out}\n")

    if encoder is None:
        print(
            "Note: tiktoken not available; using deterministic "
            "token proxy (len(text)/4).\n"
        )


if __name__ == "__main__":
    main()
