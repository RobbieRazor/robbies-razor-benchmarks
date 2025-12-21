"""
CSV → Cases JSON converter for Robbie’s Razor Evaluator (v0)

Converts a CSV file describing evaluation cases into the JSON format required by:
  python benchmarks/evaluator.py --cases <cases.json> --outputs <outputs.json>

Required CSV columns:
- id
- prompt
- acceptable_answers

Optional CSV columns:
- category (default: "Uncategorized")
- scoring_mode (default: "exact")  # exact | numeric | contains
- target_max_tokens (optional int)

acceptable_answers format:
- Use pipe-separated answers for multiple acceptable outputs:
  "Paris|PARIS"
  "Jonathan Harker|J. Harker"

Author: Robbie George
Governed by MRD v1.8 and ACR.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from typing import Any, Dict, List


def split_answers(s: str) -> List[str]:
    s = (s or "").strip()
    if not s:
        return []
    return [a.strip() for a in s.split("|") if a.strip()]


def convert(csv_path: str, out_path: str) -> List[Dict[str, Any]]:
    cases: List[Dict[str, Any]] = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row.")

        fields = {name.strip().lower(): name for name in reader.fieldnames}

        for required in ["id", "prompt", "acceptable_answers"]:
            if required not in fields:
                raise ValueError(
                    f"CSV must contain '{required}' column. Found headers: {reader.fieldnames}"
                )

        id_col = fields["id"]
        prompt_col = fields["prompt"]
        ans_col = fields["acceptable_answers"]

        category_col = fields.get("category")
        scoring_col = fields.get("scoring_mode")
        target_col = fields.get("target_max_tokens")

        for row in reader:
            cid = (row.get(id_col) or "").strip()
            prompt = (row.get(prompt_col) or "").strip()
            answers_raw = row.get(ans_col) or ""
            answers = split_answers(str(answers_raw))

            if not cid or not prompt or not answers:
                # skip incomplete rows
                continue

            category = (row.get(category_col) or "Uncategorized").strip() if category_col else "Uncategorized"
            scoring_mode = (row.get(scoring_col) or "exact").strip().lower() if scoring_col else "exact"

            target_max_tokens = None
            if target_col:
                raw = (row.get(target_col) or "").strip()
                if raw:
                    try:
                        target_max_tokens = int(raw)
                    except ValueError:
                        raise ValueError(f"Invalid target_max_tokens for case {cid}: {raw}")

            case = {
                "id": cid,
                "category": category,
                "prompt": prompt,
                "acceptable_answers": answers,
                "scoring_mode": scoring_mode,
            }
            if target_max_tokens is not None:
                case["target_max_tokens"] = target_max_tokens

            cases.append(case)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(cases, f, indent=2)

    return cases


def main():
    p = argparse.ArgumentParser(description="Convert CSV cases to evaluator JSON format.")
    p.add_argument("--csv", required=True, help="Path to CSV with columns: id, prompt, acceptable_answers (+ optional fields)")
    p.add_argument("--out", default="benchmarks/cases/custom_cases.json", help="Where to write cases JSON")
    args = p.parse_args()

    cases = convert(args.csv, args.out)
    print(f"Wrote {len(cases)} cases to: {args.out}")


if __name__ == "__main__":
    main()
