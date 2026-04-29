"""
Multiverse Foam and GRA Zeroing
Based on GRA-Multiverse-Final (qqewq)
"""

import numpy as np
from typing import List, Tuple, Optional

class Bubble:
    """A single bubble in the multiverse foam."""
    def __init__(self, state_vector: np.ndarray, rna_counts: Optional[np.ndarray] = None):
        self.state = state_vector  # latent representation of cell state
        self.rna = rna_counts if rna_counts is not None else np.random.randn(100)
        self.alive = True

    def distance(self, other: 'Bubble') -> float:
        """Spatial correlation distance R between two bubbles."""
        return np.linalg.norm(self.state - other.state)

class MultiverseFoam:
    """
    A collection of bubbles that can be zeroed via GRA.
    T_c : critical temperature (threshold) parameter.
    """
    def __init__(self, bubbles: List[Bubble], T_c: float = 1.0):
        self.bubbles = bubbles
        self.T_c = T_c
        self.history = []  # record zeroed bubbles

    @property
    def density(self) -> float:
        """Foam density (number of alive bubbles)."""
        return sum(1 for b in self.bubbles if b.alive)

    def gamma_crit(self, bubble: Bubble) -> float:
        """Critical foam threshold for a bubble."""
        # Local density: number of neighbours within T_c radius
        neighbours = sum(1 for other in self.bubbles if other.alive and bubble.distance(other) < self.T_c)
        local_density = neighbours / max(1, self.density)
        return min(local_density, self.T_c)

    def step_zero(self):
        """
        One step of GRA zeroing: remove bubbles whose resonance is out of band.
        Resonance of a bubble = gamma_crit * average_R (where R is distance to others)
        We remove if resonance < threshold (bottom threshold) or > threshold (top). 
        Here we use median of all resonances as band centre, with width band_width.
        """
        if self.density == 0:
            return
        resonances = []
        for b in self.bubbles:
            if not b.alive:
                continue
            avg_R = np.mean([b.distance(other) for other in self.bubbles if other.alive and other != b])
            resonances.append(self.gamma_crit(b) * avg_R)
        if not resonances:
            return
        median_res = np.median(resonances)
        band_half = 0.2 * median_res  # adaptive band
        for i, b in enumerate(self.bubbles):
            if b.alive:
                if abs(resonances[i] - median_res) > band_half:
                    b.alive = False
                    self.history.append(("zeroed", resonances[i], b.state.tolist()))

    def run_until_stable(self, max_steps: int = 100) -> int:
        """Run zeroing steps until no bubbles are removed."""
        for step in range(max_steps):
            before = self.density
            self.step_zero()
            if self.density == before:
                return step
        return max_steps
