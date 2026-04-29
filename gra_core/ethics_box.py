"""
Ethics filter for therapies.
Blocks any therapy that violates the "do no harm" principle.
"""

ETHICAL_BLACKLIST = {
    "gene drive in wild population": "permanent ecosystem alteration",
    "crispr germline editing (human)": "heritable changes without consent",
    "lethal dosage": "intentional harm",
}

def validate_therapy(therapy: dict) -> bool:
    """
    Check a therapy dict against the blacklist.
    therapy: {'description': ...}
    Returns True if allowed, False if blocked.
    """
    desc = therapy.get('description', '').lower()
    for banned, reason in ETHICAL_BLACKLIST.items():
        if banned in desc:
            print(f"ETHICS BLOCK: {banned} ({reason})")
            return False
    return True
