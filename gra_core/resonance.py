"""
Resonance frequency ω_res of the meta-observer.
ω_res = Σ Γ_crit(i) · R(i)
where R(i) is the mean distance of bubble i to all others.
"""

import numpy as np
from .multiverse import MultiverseFoam

def compute_omega_res(foam: MultiverseFoam) -> float:
    """
    Compute the total resonance frequency of the foam.
    Only considers alive bubbles.
    """
    total = 0.0
    alive = [b for b in foam.bubbles if b.alive]
    if not alive:
        return 0.0
    for b in alive:
        gamma = foam.gamma_crit(b)
        # R = average distance to other alive bubbles
        dists = [b.distance(other) for other in alive if other != b]
        if dists:
            R = np.mean(dists)
            total += gamma * R
    return total
