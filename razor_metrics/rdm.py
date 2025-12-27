import numpy as np
from .boundary import boundary_score

def cosine_distance(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return 1.0 - np.dot(a, b) / denom

def compute_rdm(steps):
    deltas = []
    costs = []
    boundaries = []

    for i in range(1, len(steps)):
        delta = cosine_distance(
            steps[i-1]["embedding"],
            steps[i]["embedding"]
        )
        steps[i]["delta_t"] = delta
        deltas.append(delta)
        costs.append(steps[i]["cost"])
        boundaries.append(boundary_score(steps[i]))

    D_T = float(np.sum(deltas))
    C_T = float(np.sum(costs))
    A = float(np.mean(boundaries))

    rdm = D_T / max(C_T, 1e-9)
    rdm_star = rdm * (1 - A)

    return {
        "D_T": D_T,
        "C_T": C_T,
        "A": A,
        "RDM": rdm,
        "RDM_star": rdm_star,
    }
