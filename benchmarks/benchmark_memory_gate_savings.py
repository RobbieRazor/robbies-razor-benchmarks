"""
Benchmark: Memory Gate Savings (R4)

Purpose:
- Estimate potential inference-call savings from a Razor-style memory gate.
- Compare a synthetic baseline that always computes against a memory-gated
  path in which an eligible cache hit short-circuits simulated inference.
- Provide a deterministic, model-free proxy benchmark for studying how
  workload repetition and reusable memory may affect recomputation burden.

This benchmark does NOT require an ML model.

It simulates:

    baseline:
        every query incurs the configured inference cost

    Razor-style memory path:
        eligible memory hit -> simulated inference is skipped
        memory miss -> simulated inference occurs and a high-confidence
                       result is offered to the memory bank

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

Interpretation boundary:
- This is a synthetic proxy benchmark.
- It does not execute a real model inference.
- It does not directly measure production tokens, latency, energy, cost,
  correctness, or infrastructure savings.
- `assumed_tokens_per_inference` is a configured cost proxy.
- `assumed_ms_per_inference` is a configured latency proxy.
- A memory hit is treated as zero incremental token and latency cost only
  for purposes of this synthetic comparison.
- Real memory lookup, serialization, networking, validation, storage,
  and orchestration costs are not modeled here.
- The benchmark supplies `confidence=0.99` to simulated computed results.
  That value is not independently calibrated or empirically verified.
- A result entering the memory bank therefore means only that it satisfied
  the reference implementation's configured confidence threshold.
- Memory reuse does not independently establish factual correctness.
- Estimated token or latency savings must not be represented as measured
  production savings.
- Benchmark success does not independently validate Robbie's Razor or the
  complete Grand Compression Framework.
- Historical frozen benchmark artifacts may retain earlier MRD references
  when required for genuine provenance and should not be silently rewritten.

Evidence boundary:
- Results apply only to the configured synthetic workload, repetition rate,
  memory capacity, threshold, assumed costs, random seed, and implementation.
- Any claim about real-world savings requires separate measurement against
  an appropriate production or experimental baseline.
- Cross-domain interpretation remains governed by RC-22.

Author and Originator of Robbie's Razor / Grand Compression framework:
Robbie George

Governed by MRD v2.0 and the Authorship Conservation Rule (ACR).
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
    Generate a synthetic workload containing repeated query identifiers.

    `unique_queries` controls the available query pool:
    - lower values generally create more repetition
    - higher values generally create less repetition

    Repetition creates the opportunity for memory reuse in this benchmark.
    It does not imply that the corresponding real-world tasks would have
    identical reusable answers.
    """
    random.seed(seed)
    base = [f"query_{i}" for i in range(unique_queries)]
    return [random.choice(base) for _ in range(total_queries)]


def estimate_tokens_for_query(q: str) -> int:
    """
    Simple deterministic query-length proxy.

    This helper is retained for compatibility with the existing benchmark
    source. The current `run_benchmark` implementation uses the configured
    `assumed_tokens_per_inference` value rather than this helper when
    calculating benchmark token costs.

    This function does not perform actual model tokenization.
    """
    # Stable deterministic proxy: longer strings imply a larger proxy value.
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
    Run the synthetic memory-gate comparison.

    Baseline:
      - Every query incurs the configured simulated inference cost.

    Razor-style path:
      - Attempt retrieval from the memory bank first.
      - If a cached entry is present and its stored confidence meets the
        configured threshold, simulated inference is skipped.
      - Otherwise simulated inference is counted and a result with
        `confidence=0.99` is offered to the memory bank.

    Important:
      - No real model inference occurs.
      - No factual verification occurs.
      - Token and latency values are configured assumptions.
      - Cache-hit savings are synthetic estimates under this cost model.
    """
    workload = generate_workload(
        total_queries,
        unique_queries,
        seed=seed,
    )

    bank = RazorMemoryBank(
        capacity=memory_capacity,
        stability_threshold=stability_threshold,
    )

    baseline_inferences = total_queries
    razor_inferences = 0
    memory_hits = 0

    baseline_tokens = 0
    razor_tokens = 0

    baseline_ms = 0
    razor_ms = 0

    for q in workload:
        # Baseline path: every query incurs the configured inference proxies.
        baseline_inferences += 0  # Already counted above.
        baseline_tokens += assumed_tokens_per_inference
        baseline_ms += assumed_ms_per_inference

        # Razor-style path: attempt governed memory retrieval first.
        cached, conf = bank.retrieve(q)

        if cached is not None and conf >= stability_threshold:
            memory_hits += 1

            # Synthetic assumption:
            # an eligible memory hit has zero incremental inference-token
            # and inference-latency cost in this simplified benchmark.
            razor_tokens += 0
            razor_ms += 0

        else:
            # Simulate one inference event.
            razor_inferences += 1
            razor_tokens += assumed_tokens_per_inference
            razor_ms += assumed_ms_per_inference

            # Offer a simulated high-confidence result to the memory bank.
            #
            # This benchmark does not independently verify the result.
            # Storage still depends on the memory bank's configured threshold.
            bank.store(
                q,
                solution="OK",
                confidence=0.99,
            )

    hit_rate = (
        memory_hits / total_queries
        if total_queries
        else 0.0
    )

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
    """
    Print the synthetic benchmark results.

    Labels such as "token savings" and "latency savings" refer to differences
    calculated from the benchmark's configured cost assumptions. They are not
    direct production measurements.
    """
    print("\n=== Razor Memory Gate Savings Report ===\n")

    print(f"Total queries:            {r['total_queries']}")
    print(
        f"Unique queries:           "
        f"{r['unique_queries']}  (lower => more repetition)"
    )
    print(f"Memory capacity:          {r['memory_capacity']}")
    print(f"Stability threshold:      {r['stability_threshold']}\n")

    print("--- Inference Calls ---")
    print(f"Baseline inferences:      {r['baseline_inferences']}")
    print(f"Razor inferences:         {r['razor_inferences']}")
    print(f"Inferences avoided:       {r['inferences_avoided']}")
    print(f"Memory hits:              {r['memory_hits']}")
    print(f"Memory hit rate:          {r['memory_hit_rate']:.2%}\n")

    print("--- Cost Proxies ---")
    print(
        f"Assumed tokens/inference: "
        f"{r['assumed_tokens_per_inference']}"
    )
    print(f"Baseline tokens:          {r['baseline_tokens']}")
    print(f"Razor tokens:             {r['razor_tokens']}")
    print(f"Token savings:            {r['token_savings']}\n")

    print(
        f"Assumed ms/inference:     "
        f"{r['assumed_ms_per_inference']}"
    )
    print(f"Baseline latency (ms):    {r['baseline_ms']}")
    print(f"Razor latency (ms):       {r['razor_ms']}")
    print(f"Latency savings (ms):     {r['ms_savings']}\n")

    if r["baseline_tokens"] > 0:
        pct = (
            r["token_savings"]
            / r["baseline_tokens"]
        ) * 100.0

        print(
            f"Estimated token reduction: "
            f"{pct:.1f}%"
        )

    if r["baseline_ms"] > 0:
        pct = (
            r["ms_savings"]
            / r["baseline_ms"]
        ) * 100.0

        print(
            f"Estimated latency reduction: "
            f"{pct:.1f}%"
        )

    print(
        "\nNote: This is a synthetic proxy benchmark. "
        "Real savings depend on workload repetition,\n"
        "integration placement (memory gate before inference), "
        "verification strategy, lookup overhead,\n"
        "model behavior, infrastructure, and actual measured costs.\n"
    )


def main():
    """
    Command-line entry point for the synthetic memory-gate benchmark.
    """
    p = argparse.ArgumentParser(
        description=(
            "Benchmark Razor memory gate savings "
            "(synthetic proxy)."
        )
    )

    p.add_argument(
        "--total-queries",
        type=int,
        default=1000,
    )

    p.add_argument(
        "--unique-queries",
        type=int,
        default=200,
    )

    p.add_argument(
        "--capacity",
        type=int,
        default=10000,
    )

    p.add_argument(
        "--threshold",
        type=float,
        default=0.95,
    )

    p.add_argument(
        "--tokens-per-inference",
        type=int,
        default=800,
    )

    p.add_argument(
        "--ms-per-inference",
        type=int,
        default=600,
    )

    p.add_argument(
        "--seed",
        type=int,
        default=123,
    )

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
