"""
Generate personalised therapy from cell twin and disease.
Uses knowledge graph: OSKM, senolytics, CRISPR targets.
"""

import random
from gra_core.ethics_box import validate_therapy

def generate_therapy(cell_twins: list, disease: str) -> dict:
    """
    Based on disease, produce a therapy recommendation.
    For breast cancer: OSKM + senolytics + CRISPR targets TP53, MYC.
    """
    if disease.lower() in ["breast cancer", "brca"]:
        therapy = {
            "disease": disease,
            "reprogramming": "OSKM (Oct4, Sox2, Klf4, c-Myc)",
            "senolytics": "Dasatinib + Quercetin",
            "crispr_targets": ["TP53", "MYC", "ERBB2 (HER2) if amplified"],
            "notes": "OSKM partial reprogramming to reverse age; senolytics clear senescent cells; CRISPR correct oncogenes.",
            "description": "Combined OSKM + senolytics + CRISPR editing"
        }
    else:
        therapy = {
            "disease": disease,
            "reprogramming": "OSKM",
            "senolytics": "Navitoclax",
            "crispr_targets": ["generic disease driver"],
            "description": "General reprogramming and senolytic therapy"
        }

    if validate_therapy(therapy):
        return therapy
    else:
        return {"error": "Therapy blocked by ethics filter"}

def simulate_trial(cell_twins, therapy):
    """
    Mock in silico trial: return efficacy score.
    """
    # For demonstration, just random score biased by therapy presence.
    if "blocked" in therapy:
        return 0.0
    return random.uniform(0.7, 0.95)
