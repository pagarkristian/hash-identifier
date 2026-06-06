import os
import json
from datetime import datetime

def save_report(hash_value, result):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("reports/report.txt", "w") as report:

        report.write("HASH IDENTIFIER REPORT\n")
        report.write("=" * 50 + "\n")
        report.write(f"Timestamp  : {timestamp}\n")
        report.write(f"Hash Value : {hash_value}\n")
        report.write(f"Hash Length: {len(hash_value)}\n")
        report.write(f"Hash Type  : {result['name']}\n")
        report.write(f"Description: {result['description']}\n")
        report.write(f"Confidence : {result['confidence']}\n")

    json_data = {
        "timestamp" : timestamp,
        "hash_value" : hash_value,
        "hash_length" : len(hash_value),
        "hash_type" : result["name"],
        "description" : result["description"],
        "confidence" : result["confidence"]
    }

    with open("reports/report.json", "w") as json_report:
        json.dump(json_data, json_report, indent=4)

    return "reports/report.txt"
