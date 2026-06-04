import os
import json

def save_report(hash_value, result):

    os.makedirs("reports", exist_ok=True)

    with open("reports/report.txt", "w") as report:

        report.write("HASH IDENTIFIER REPORT\n")
        report.write("=" * 50 + "\n")

        report.write(f"Hash Value : {hash_value}\n")
        report.write(f"Hash Type  : {result['name']}\n")
        report.write(f"Description: {result['description']}\n")
        report.write(f"Confidence : {result['confidence']}\n")

    json_data = {
        "hash_value" : hash_value,
        "hash_type" : result["name"],
        "description" : result["description"],
        "confidence" : result["confidence"]
}

    with open("reports/report.json", "w")as json_report:
         json.dump(json_data, json_report, indent=4)

    return "reports/report.txt"
