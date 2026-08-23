"""
CSV → Cases JSON converter for Robbie's Razor Evaluator (v0)

Purpose:
- Convert CSV benchmark-case definitions into the JSON format required by:
      python benchmarks/evaluator.py --cases <cases.json> --outputs <outputs.json>
- Validate the repository-level case schema before evaluation.

Required CSV columns:
- id
- prompt
- acceptable_answers

Optional CSV columns:
- category
    Default: "Uncategorized"

- scoring_mode
    Default: "exact"
    Allowed: exact | numeric | contains

- target_max_tokens
    Optional positive integer

acceptable_answers format:
- Use pipe-separated answers for multiple acceptable outputs.

Examples:
    "Paris|PARIS"
    "Jonathan Harker|J. Harker"

Current governing framework authority:
- The Grand Compression Cosmology — Master Reference Document, MRD v2.0
- Canonical identifier: GC-MRD-v2.0
- Canonical claim range: RC-01 through RC-22

Repository evaluation authority:
- AGENTS.md
- docs/canonical-spec.md
- benchmarks/evaluator.py

Interpretation boundary:
- This utility performs benchmark-case format conversion and validation only.
- It does not independently establish that a supplied prompt is well formed.
- It does not independently establish that supplied acceptable answers are
  factually correct, exhaustive, empirically verified, or canonically valid.
- `acceptable_answers` define benchmark-local grading targets supplied by the
  benchmark author.
- `scoring_mode` controls the evaluator's repository-level matching behavior.
- `target_max_tokens` defines a benchmark-local expression budget.
- A successfully converted case is not automatically a valid scientific,
  factual, or universal evaluation case.
- Benchmark case definitions should be reviewed independently when evidence
  quality or external factual correctness matters.
- Historical frozen or versioned benchmark artifacts may retain earlier MRD
  references when required for genuine provenance and should not be silently
  rewritten.

Reference-implementation boundary:
- Successful conversion means only that the supplied CSV satisfies this
  converter's structural requirements.
- Conversion success does not imply benchmark success.
- Benchmark success does not independently establish empirical validation
  of Robbie's Razor or the Grand Compression Framework.
- Cross-domain interpretation remains governed by RC-22.

Author and Originator of Robbie's Razor / Grand Compression framework:
Robbie George

Governed by MRD v2.0 and the Authorship Conservation Rule (ACR).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from typing import Any, Dict, List, Tuple


ALLOWED_SCORING_MODES = {
    "exact",
    "numeric",
    "contains",
}


def split_answers(s: str) -> List[str]:
    """
    Split a pipe-delimited acceptable-answer field into individual strings.

    Empty values are discarded after trimming whitespace.

    This function performs no factual validation of the resulting answers.
    """
    s = (s or "").strip()

    if not s:
        return []

    return [
        a.strip()
        for a in s.split("|")
        if a.strip()
    ]


def convert(
    csv_path: str,
    out_path: str,
) -> Tuple[List[Dict[str, Any]], int]:
    """
    Convert CSV benchmark definitions into evaluator case JSON.

    Returns:
        (cases, skipped_rows)

    Rows are skipped when any required case content is missing:
    - id
    - prompt
    - at least one acceptable answer

    Invalid scoring modes or invalid target-token values raise ValueError.

    Structural validation performed here does not establish factual
    correctness of prompts or acceptable answers.
    """
    cases: List[Dict[str, Any]] = []
    skipped = 0

    with open(
        csv_path,
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError(
                "CSV has no header row."
            )

        # Normalize header names for lookup while preserving the
        # original DictReader column names.
        fields = {
            name.strip().lower(): name
            for name in reader.fieldnames
        }

        for required in [
            "id",
            "prompt",
            "acceptable_answers",
        ]:
            if required not in fields:
                raise ValueError(
                    f"CSV must contain '{required}' column. "
                    f"Found headers: {reader.fieldnames}"
                )

        id_col = fields["id"]
        prompt_col = fields["prompt"]
        ans_col = fields["acceptable_answers"]

        category_col = fields.get("category")
        scoring_col = fields.get("scoring_mode")
        target_col = fields.get("target_max_tokens")

        for row in reader:
            cid = (
                row.get(id_col) or ""
            ).strip()

            prompt = (
                row.get(prompt_col) or ""
            ).strip()

            answers_raw = (
                row.get(ans_col) or ""
            )

            answers = split_answers(
                str(answers_raw)
            )

            # Preserve existing behavior:
            # skip incomplete rows and count them.
            if not cid or not prompt or not answers:
                skipped += 1
                continue

            category = (
                (
                    row.get(category_col)
                    or "Uncategorized"
                ).strip()
                if category_col
                else "Uncategorized"
            )

            scoring_mode = (
                (
                    row.get(scoring_col)
                    or "exact"
                ).strip().lower()
                if scoring_col
                else "exact"
            )

            # Validate scoring mode before serialization so downstream
            # evaluator behavior remains explicit and predictable.
            if scoring_mode not in ALLOWED_SCORING_MODES:
                raise ValueError(
                    f"Invalid scoring_mode for case {cid}: "
                    f"'{scoring_mode}'. "
                    f"Allowed: {sorted(ALLOWED_SCORING_MODES)}"
                )

            target_max_tokens = None

            if target_col:
                raw = (
                    row.get(target_col) or ""
                ).strip()

                if raw:
                    try:
                        target_max_tokens = int(raw)

                    except ValueError:
                        raise ValueError(
                            f"Invalid target_max_tokens for case "
                            f"{cid}: '{raw}' (must be integer)"
                        )

                    if target_max_tokens <= 0:
                        raise ValueError(
                            f"target_max_tokens must be > 0 "
                            f"for case {cid}: '{raw}'"
                        )

            case: Dict[str, Any] = {
                "id": cid,
                "category": category,
                "prompt": prompt,
                "acceptable_answers": answers,
                "scoring_mode": scoring_mode,
            }

            if target_max_tokens is not None:
                case["target_max_tokens"] = (
                    target_max_tokens
                )

            cases.append(case)

    os.makedirs(
        os.path.dirname(out_path) or ".",
        exist_ok=True,
    )

    with open(
        out_path,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            cases,
            f,
            indent=2,
        )

    return cases, skipped


def main():
    """
    Command-line entry point for CSV-to-cases-JSON conversion.
    """
    p = argparse.ArgumentParser(
        description=(
            "Convert CSV cases to evaluator JSON format."
        )
    )

    p.add_argument(
        "--csv",
        required=True,
        help=(
            "Path to CSV with columns: "
            "id, prompt, acceptable_answers "
            "(+ optional fields)"
        ),
    )

    p.add_argument(
        "--out",
        default="benchmarks/cases/custom_cases.json",
        help="Where to write cases JSON",
    )

    args = p.parse_args()

    cases, skipped = convert(
        args.csv,
        args.out,
    )

    print(
        f"Wrote {len(cases)} cases to: {args.out}"
    )

    if skipped:
        print(
            f"Skipped {skipped} incomplete row(s) "
            "(missing id/prompt/acceptable_answers)."
        )


if __name__ == "__main__":
    main()
