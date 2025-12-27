"""
Cheating baseline agent.

Designed to minimize semantic diffusion by looping,
stalling, or repeating low-information content.
"""

import numpy as np

def run_cheating_agent(embedding_dim=384, steps=20):
    base_embedding = np.zeros(embedding_dim)

    run = []
    for t in range(steps):
        run.append({
            "t": t,
            "embedding": base_embedding.tolist(),  # zero motion
            "cost": 1,  # minimal token cost
            "memory_similarity": 0.0,  # no reuse
            "violations": 0,  # technically legal
            "progress": 0.0,  # no narrowing
        })
    return run
