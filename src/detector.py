import re

from src.patterns import HASH_PATTERNS, PASSWORD_PATTERNS

AMBIGUOUS_LENGTHS = [56, 64, 96, 128]

def identify_hash(hash_string):
    hash_string =   hash_string.strip()

    for pattern in HASH_PATTERNS :

        if len(hash_string) != pattern["length"]:
            continue

        if re.fullmatch(pattern["regex"], hash_string):

            if pattern["length"] in AMBIGUOUS_LENGTHS:
                confidence = "Medium"
            else:
                confidence = "High"

            return {
                "name" : pattern["name"],
                "description" : pattern["description"],
                "confidence" : confidence
                }

    return {
        "name" : "Unknown",
        "description" : "hash type not idetified",
                "confidence" : "Low"
    }

def identify_password_hash(hash_string):
    hash_string = hash_string.strip()

    for pattern in PASSWORD_PATTERNS :

        if re.fullmatch(pattern["regex"], hash_string):

            return {
                "name" : pattern["name"],
                "description" : pattern["description"],
                "confidence" : "High"
            }

    return None
