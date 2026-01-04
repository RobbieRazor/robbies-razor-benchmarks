from __future__ import annotations

import json
import time
from dataclasses import dataclass, asdict
from typing import Any, Dict

# Wire to your real engine
from src.razor.memory_bank import MemoryBank


@dataclass
class TraceResult:
    prompt: str
    hit: bool
    confidence: float
    lss_final: float
    rejected: bool
    latency_ms: float
    meta: Dict[str, Any]


def _call_bank(bank: Any, prompt: str) -> Any:
    """
    Try common entrypoints without assuming a specific method name.
    Update this list only if your MemoryBank uses a different API.
    """
    for name in ("query", "retrieve", "lookup", "get"):
        fn = getattr(bank, name, None)
        if callable(fn):
            return fn(prompt)

    # Support MemoryBank being callable
    if callable(bank):
        return bank(prompt)

    raise AttributeError(
        "MemoryBank has no callable entrypoint. Expected one of: "
        "query/retrieve/lookup/get or __call__."
    )


def _as_dict(result: Any) -> Dict[str, Any]:
    """
    Normalize MemoryBank outputs into a dict-like structure.
    Supports dict returns or simple objects with attributes.
    """
    if result is None:
        return {}

    if isinstance(result, dict):
        return result

    out: Dict[str, Any] = {}
    for k in ("confidence", "hit", "value", "key", "id"):
        if hasattr(result, k):
            out[k] = getattr(result, k)
    return out


def confidence_to_lss(conf: float) -> float:
    """
    Conservative placeholder mapping:
    LSS is currently derived from confidence and clamped to [0, 1].

    If/when LSS becomes a distinct substrate stability measure,
    replace this mapping while keeping the output schema stable.
    """
    try:
        x = float(conf)
    except Exception:
        x = 0.0
    return max(0.0, min(1.0, x))


class RazorAdapter:
    def __init__(self):
        # Use the same parameters you advertise in the repo (R4 gating + capacity).
        self.bank = MemoryBank(capacity=1000, r_compliance="R4")

    def trace(self, prompt: str, *, reject_threshold: float = 0.2) -> TraceResult:
        t0 = time.time()
        raw = _call_bank(self.bank, prompt)
        latency_ms = (time.time() - t0) * 1000.0

        d = _as_dict(raw)

        confidence = float(d.get("confidence", 0.5))
        hit = bool(d.get("hit", False))

        lss_final = confidence_to_lss(confidence)
        rejected = confidence < reject_threshold

        return TraceResult(
            prompt=prompt,
            hit=hit,
            confidence=confidence,
            lss_final=lss_final,
            rejected=rejected,
            latency_ms=latency_ms,
            meta={
                "r_compliance": "R4",
                "capacity": 1000,
                "reject_threshold": reject_threshold,
                "raw_keys": sorted(list(d.keys())),
            },
        )


def main() -> None:
    adapter = RazorAdapter()

    # Minimal consistency probes (you can expand later)
    prompts = [
        "The car drives through the wall.",
        "The car stops at the wall.",
    ]

    results = [adapter.trace(p) for p in prompts]

    hit_rate = sum(1 for r in results if r.hit) / max(1, len(results))
    rejection_rate = sum(1 for r in results if r.rejected) / max(1, len(results))
    avg_latency_ms = sum(r.latency_ms for r in results) / max(1, len(results))

    report = {
        "benchmark": "refractive-truth",
        "version": "0.1",
        "interpretation": "Refraction = retrieval/stabilization efficiency vs recomputation (MemoryBank gating).",
        "results": [asdict(r) for r in results],
        "summary": {
            "hit_rate": hit_rate,
            "rejection_rate": rejection_rate,
            "avg_latency_ms": avg_latency_ms,
        },
    }

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
