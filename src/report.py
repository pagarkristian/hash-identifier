import os
import json
import csv
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

def view_report():

    txt_path = "reports/report.txt"
    json_path = "reports/report.json"

    if not os.path.exists(txt_path):
        print("No report found.")
        return

    print("\nLatest Report")
    print("=" * 50)

    with open(txt_path, "r") as f:
        print(f.read())

    print("=" * 50)
    print(f"JSON Report : {json_path}")

def save_csv(hash_value, result):

    csv_path = "reports/report.csv"
    file_exists = os.path.exists(csv_path)

    with open(csv_path, "a", newline="") as csv_file:

        fieldnames = [
            "timestamp",
            "hash_value",
            "hash_length",
            "hash_type",
            "confidence"
        ]

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hash_value" : hash_value,
            "hash_length" : len(hash_value),
            "hash_type" : result["name"],
            "confidence" : result["confidence"]
        })
