import re

from src.patterns import HASH_PATTERNS

def identify_hash(hash_string):
    hash_string =   hash_string.strip()

    for pattern in HASH_PATTERNS :

        if len(hash_string) != pattern["length"]:
            continue

        if re.fullmatch(pattern["regex"], hash_string):

            return {
                "name" : pattern["name"],
                "description" : pattern["description"],
                "confidence" : "Medium"
                }

    return {
        "name" : "Unknown",
        "description" : "hash type not idetified",
                "confidence" : "Low"
    }
