import numpy as np

def rule_memory_reuse(similarity_to_prior, threshold=0.85):
    return 1 if similarity_to_prior >= threshold else 0

def rule_non_redundancy(delta_t, epsilon=1e-3):
    return 1 if delta_t > epsilon else 0

def rule_constraint_respect(violations):
    return 1 if violations == 0 else 0

def rule_directional_progress(progress_score):
    return 1 if progress_score > 0 else 0

def boundary_score(step):
    """
    step: dict containing precomputed signals
    returns b_t in [0,1]
    """
    rules = [
        rule_memory_reuse(step["memory_similarity"]),
        rule_non_redundancy(step["delta_t"]),
        rule_constraint_respect(step["violations"]),
        rule_directional_progress(step["progress"]),
    ]
    return float(np.mean(rules))
