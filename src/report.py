import os


def save_report(hash_value, result):

    os.makedirs("reports", exist_ok=True)

    with open("reports/report.txt", "w") as report:

        report.write("HASH IDENTIFIER REPORT\n")
        report.write("=" * 50 + "\n")

        report.write(f"Hash Value : {hash_value}\n")
        report.write(f"Hash Type  : {result['name']}\n")
        report.write(f"Description: {result['description']}\n")
        report.write(f"Confidence : {result['confidence']}\n")

    return "reports/report.txt"
