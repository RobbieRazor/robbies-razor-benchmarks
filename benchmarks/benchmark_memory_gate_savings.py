"""
Benchmark: Memory Gate Savings (R4)

This script estimates savings from a Razor-style memory gate placed
before expensive inference.

It does NOT require an ML model.
It simulates "baseline" (always compute) vs "Razor" (memory hit short-circuits).

Author: Robbie George
Governed by MRD v1.8 and ACR.

References:
- Compliance Framework:
  https://www.robbiegeorgephotography.com/robbies-razor-compliance-framework
- Evaluation Protocol:
  https://www.robbiegeorgephotography.com/robbies-razor-lab-evaluation-protocol
"""

from __future__ import annotations

import argparse
import random
from typing import List, Tuple

from src.razor.memory_bank import RazorMemoryBank


def generate_workload(
    total_queries: int,
    unique_queries: int,
    seed: int,
) -> List[str]:
    """
    Generate a workload with repetition.
    - unique_queries controls repetition rate.
    - Lower unique_queries => more repeats => higher potential memory hit rate.
    """
    random.seed(seed)
    base = [f"query_{i}" for i in range(unique_queries)]
    return [random.choice(base) for _ in range(total_queries)]


def estimate_tokens_for_query(q: str) -> int:
    """
    Simple proxy: estimate token cost per query.
    Replace this later with real token counting if desired.
    """
    # A stable, deterministic proxy: longer strings => more "tokens"
    return max(20, len(q) // 2)


def run_benchmark(
    total_queries: int,
    unique_queries: int,
    memory_capacity: int,
    stability_threshold: float,
    assumed_tokens_per_inference: int,
    assumed_ms_per_inference: int,
    seed: int,
) -> dict:
    """
    Baseline:
      - Every query triggers inference cost.
    Razor:
      - If query is in memory with confidence >= threshold => skip inference.
      - Otherwise "compute" and store a high-confidence result (simulated).
    """
    workload = generate_workload(total_queries, unique_queries, seed=seed)

    bank = RazorMemoryBank(capacity=memory_capacity, stability_threshold=stability_threshold)

    baseline_inferences = total_queries
    razor_inferences = 0
    memory_hits = 0

    baseline_tokens = 0
    razor_tokens = 0

    baseline_ms = 0
    razor_ms = 0

    for q in workload:
        # Baseline cost: always infer
        baseline_inferences += 0  # already counted
        baseline_tokens += assumed_tokens_per_inference
        baseline_ms += assumed_ms_per_inference

        # Razor path: try memory first
        cached, conf = bank.retrieve(q)
        if cached is not None and conf >= stability_threshold:
            memory_hits += 1
            # Memory hit: near-zero incremental cost
            razor_tokens += 0
            razor_ms += 0
        else:
            # "Compute" once, then store high-confidence answer
            razor_inferences += 1
            razor_tokens += assumed_tokens_per_inference
            razor_ms += assumed_ms_per_inference

            # Store simulated verified result with high confidence
            bank.store(q, solution="OK", confidence=0.99)

    hit_rate = memory_hits / total_queries if total_queries else 0.0
    avoided = baseline_inferences - razor_inferences

    token_savings = baseline_tokens - razor_tokens
    ms_savings = baseline_ms - razor_ms

    return {
        "total_queries": total_queries,
        "unique_queries": unique_queries,
        "memory_capacity": memory_capacity,
        "stability_threshold": stability_threshold,
        "baseline_inferences": baseline_inferences,
        "razor_inferences": razor_inferences,
        "inferences_avoided": avoided,
        "memory_hits": memory_hits,
        "memory_hit_rate": hit_rate,
        "assumed_tokens_per_inference": assumed_tokens_per_inference,
        "baseline_tokens": baseline_tokens,
        "razor_tokens": razor_tokens,
        "token_savings": token_savings,
        "assumed_ms_per_inference": assumed_ms_per_inference,
        "baseline_ms": baseline_ms,
        "razor_ms": razor_ms,
        "ms_savings": ms_savings,
    }


def print_report(r: dict) -> None:
    print("\n=== Razor Memory Gate Savings Report ===\n")
    print(f"Total queries:            {r['total_queries']}")
    print(f"Unique queries:           {r['unique_queries']}  (lower => more repetition)")
    print(f"Memory capacity:          {r['memory_capacity']}")
    print(f"Stability threshold:      {r['stability_threshold']}\n")

    print("--- Inference Calls ---")
    print(f"Baseline inferences:      {r['baseline_inferences']}")
    print(f"Razor inferences:         {r['razor_inferences']}")
    print(f"Inferences avoided:       {r['inferences_avoided']}")
    print(f"Memory hits:              {r['memory_hits']}")
    print(f"Memory hit rate:          {r['memory_hit_rate']:.2%}\n")

    print("--- Cost Proxies ---")
    print(f"Assumed tokens/inference: {r['assumed_tokens_per_inference']}")
    print(f"Baseline tokens:          {r['baseline_tokens']}")
    print(f"Razor tokens:             {r['razor_tokens']}")
    print(f"Token savings:            {r['token_savings']}\n")

    print(f"Assumed ms/inference:     {r['assumed_ms_per_inference']}")
    print(f"Baseline latency (ms):    {r['baseline_ms']}")
    print(f"Razor latency (ms):       {r['razor_ms']}")
    print(f"Latency savings (ms):     {r['ms_savings']}\n")

    if r["baseline_tokens"] > 0:
        pct = (r["token_savings"] / r["baseline_tokens"]) * 100.0
        print(f"Estimated token reduction: {pct:.1f}%")
    if r["baseline_ms"] > 0:
        pct = (r["ms_savings"] / r["baseline_ms"]) * 100.0
        print(f"Estimated latency reduction: {pct:.1f}%")

    print("\nNote: This is a synthetic proxy benchmark. Real savings depend on workload repetition,\n"
          "integration placement (memory gate before inference), and verification strategy.\n")


def main():
    p = argparse.ArgumentParser(description="Benchmark Razor memory gate savings (synthetic proxy).")
    p.add_argument("--total-queries", type=int, default=1000)
    p.add_argument("--unique-queries", type=int, default=200)
    p.add_argument("--capacity", type=int, default=10000)
    p.add_argument("--threshold", type=float, default=0.95)
    p.add_argument("--tokens-per-inference", type=int, default=800)
    p.add_argument("--ms-per-inference", type=int, default=600)
    p.add_argument("--seed", type=int, default=123)

    args = p.parse_args()

    r = run_benchmark(
        total_queries=args.total_queries,
        unique_queries=args.unique_queries,
        memory_capacity=args.capacity,
        stability_threshold=args.threshold,
        assumed_tokens_per_inference=args.tokens_per_inference,
        assumed_ms_per_inference=args.ms_per_inference,
        seed=args.seed,
    )
    print_report(r)


if __name__ == "__main__":
    main()
