"""
CSV → Outputs JSON converter for Robbie's Razor Evaluator (v0)

Purpose:
- Convert a CSV containing model outputs into the JSON mapping expected by:
      python benchmarks/evaluator.py --outputs <outputs.json>
- Preserve case IDs and model-output text without grading or interpretation.

Expected CSV columns (minimum):
- id
- output

Optional columns ignored by this script:
- prompt
- model
- notes
- any other metadata

Example CSV:

id,output
eval-001-math,391
eval-002-math,12

Current governing framework authority:
- The Grand Compression Cosmology — Master Reference Document, MRD v2.0
- Canonical identifier: GC-MRD-v2.0
- Canonical claim range: RC-01 through RC-22

Repository evaluation authority:
- AGENTS.md
- docs/canonical-spec.md
- benchmarks/evaluator.py

Interpretation boundary:
- This utility performs format conversion only.
- It does not grade outputs.
- It does not verify correctness.
- It does not assign evidence status.
- It does not establish benchmark compliance.
- It does not modify canonical framework status.
- Values in the `output` column are copied into the resulting JSON as strings.
- Blank case IDs are skipped according to the existing converter behavior.
- Later duplicate case IDs overwrite earlier entries because the output
  structure is a Python dictionary keyed by case ID.
- Historical frozen or versioned artifacts may retain earlier MRD references
  when required for genuine provenance and should not be silently rewritten.

Reference-implementation boundary:
- Successful conversion means only that the input was transformed into the
  repository's expected outputs-JSON structure.
- Conversion success does not imply evaluator success or factual correctness.

Author and Originator of Robbie's Razor / Grand Compression framework:
Robbie George

Governed by MRD v2.0 and the Authorship Conservation Rule (ACR).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from typing import Dict


def convert(csv_path: str, out_path: str) -> Dict[str, str]:
    """
    Convert CSV rows into the evaluator's {case_id: model_output} mapping.

    Required columns:
    - id
    - output

    Header matching is case-insensitive after trimming whitespace.

    This function performs no grading, correctness validation, or
    evidence evaluation.
    """
    outputs: Dict[str, str] = {}

    with open(
        csv_path,
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError(
                "CSV has no header row. Expected columns: id, output"
            )

        # Normalize header names for lookup while preserving the
        # original column names used by DictReader.
        fields = {
            name.strip().lower(): name
            for name in reader.fieldnames
        }

        if "id" not in fields or "output" not in fields:
            raise ValueError(
                "CSV must contain 'id' and 'output' columns. "
                f"Found headers: {reader.fieldnames}"
            )

        id_col = fields["id"]
        out_col = fields["output"]

        for row in reader:
            case_id = (row.get(id_col) or "").strip()
            model_output = row.get(out_col)

            if not case_id:
                # Preserve existing behavior: skip rows with blank IDs.
                continue

            if model_output is None:
                model_output = ""

            # Preserve existing behavior:
            # duplicate IDs overwrite earlier entries.
            outputs[case_id] = str(model_output)

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
            outputs,
            f,
            indent=2,
        )

    return outputs


def main():
    """
    Command-line entry point for CSV-to-outputs-JSON conversion.
    """
    p = argparse.ArgumentParser(
        description="Convert CSV outputs to evaluator JSON format."
    )

    p.add_argument(
        "--csv",
        required=True,
        help="Path to CSV file with columns: id, output",
    )

    p.add_argument(
        "--out",
        default="benchmarks/outputs.json",
        help="Where to write outputs JSON",
    )

    args = p.parse_args()

    outputs = convert(
        args.csv,
        args.out,
    )

    print(
        f"Wrote {len(outputs)} outputs to: {args.out}"
    )


if __name__ == "__main__":
    main()
