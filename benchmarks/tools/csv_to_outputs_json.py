"""
CSV → Outputs JSON converter for Robbie’s Razor Evaluator (v0)

Converts a CSV file containing model outputs into the JSON format required by:
  python benchmarks/evaluator.py --outputs <outputs.json>

Expected CSV columns (minimum):
- id
- output

Optional columns (ignored by this script):
- prompt
- model
- notes
- any other metadata

Example CSV:

id,output
eval-001-math,391
eval-002-math,12

Author: Robbie George
Governed by MRD v1.8 and ACR.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from typing import Dict


def convert(csv_path: str, out_path: str) -> Dict[str, str]:
    outputs: Dict[str, str] = {}

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row. Expected columns: id, output")

        # Normalize header names
        fields = {name.strip().lower(): name for name in reader.fieldnames}

        if "id" not in fields or "output" not in fields:
            raise ValueError(
                f"CSV must contain 'id' and 'output' columns. Found headers: {reader.fieldnames}"
            )

        id_col = fields["id"]
        out_col = fields["output"]

        for row in reader:
            case_id = (row.get(id_col) or "").strip()
            model_output = row.get(out_col)

            if not case_id:
                continue  # skip blank rows

            if model_output is None:
                model_output = ""

            outputs[case_id] = str(model_output)

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(outputs, f, indent=2)

    return outputs


def main():
    p = argparse.ArgumentParser(description="Convert CSV outputs to evaluator JSON format.")
    p.add_argument("--csv", required=True, help="Path to CSV file with columns: id, output")
    p.add_argument("--out", default="benchmarks/outputs.json", help="Where to write outputs JSON")
    args = p.parse_args()

    outputs = convert(args.csv, args.out)
    print(f"Wrote {len(outputs)} outputs to: {args.out}")


if __name__ == "__main__":
    main()
