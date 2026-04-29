"""
Build digital cell twins from scRNA-seq data.
Supports loading from GEO (GEOparse fallback) or local sample CSV.
"""

import pandas as pd
import numpy as np
from typing import Optional, Dict, Any

class CellTwin:
    def __init__(self, cell_id: str, gene_expression: pd.Series, metadata: Optional[Dict[str, Any]] = None):
        self.id = cell_id
        self.expr = gene_expression  # gene names -> expression
        self.metadata = metadata or {}
        # latent state derived from expression (first 20 PCs for demo)
        self.state = self._compute_state()

    def _compute_state(self) -> np.ndarray:
        """Mock state: take first 20 genes as features; in practice use PCA/autoencoder."""
        values = self.expr.values[:20].astype(float)
        if len(values) < 20:
            values = np.pad(values, (0, 20 - len(values)), 'constant')
        return values

    def __repr__(self):
        return f"CellTwin({self.id})"

def load_from_geo(gse_id: str) -> list:
    """
    Load scRNA-seq data from GEO. (Stub using local sample file)
    Real implementation would use GEOparse.
    """
    # Placeholder: load sample_geo.csv
    try:
        df = pd.read_csv("../data/sample_geo.csv", index_col=0)
    except FileNotFoundError:
        # fallback: synthetic data
        genes = [f"GENE_{i}" for i in range(200)]
        df = pd.DataFrame(np.random.poisson(5, size=(100, 200)), columns=genes)
    twins = []
    for idx, row in df.iterrows():
        twin = CellTwin(f"{gse_id}_{idx}", row)
        twins.append(twin)
    return twins

def load_brca_tcga() -> list:
    """Load BRCA TCGA expression (mock)."""
    # In production, use cBioPortal/TCGA data.
    # Here return some twins based on sample data.
    # For simplicity, reuse sample_geo but with BRCA metadata.
    try:
        df = pd.read_csv("../data/sample_geo.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(np.random.poisson(5, size=(50, 200)), columns=[f"GENE_{i}" for i in range(200)])
    twins = []
    for idx, row in df.iterrows():
        twin = CellTwin(f"BRCA_{idx}", row, metadata={"disease": "breast cancer", "subtype": "Luminal A"})
        twins.append(twin)
    return twins
