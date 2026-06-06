import os
import json

def show_stats():
    log_file = "logs/hash_identifier.log"

    if not os.path.exists(log_file):
        print("No logs found.")
        return

    stats = {}
    confidence_stats = {
        "High" : 0,
        "Medium" : 0,
        "Low" : 0
    }

    with open(log_file, "r") as file:
        for line in file:
            if "TYPE=" not in line:
                continue

            hash_type = line.split("TYPE=")[1].strip()

            stats[hash_type] = stats.get(hash_type, 0) + 1

            if hash_type == "Unknown":
                confidence_stats["Low"] += 1
            elif hash_type in ["SHA256", "SHA3-256", "SHA224", "SHA3-224",
                                "SHA384", "SHA3-384", "SHA512", "SHA3-512"]:
                confidence_stats["Medium"] += 1
            else:
                confidence_stats["High"] += 1

    total = sum(stats.values())

    if total == 0:
        print("No scan history found.")
        return

    most_common = max(stats, key=stats.get)
    unknown = stats.get("Unknown", 0)
    detected = total - unknown
    detection_rate = (detected / total) * 100

    print("\nStatistics")
    print("=" * 50)
    print(f"Total Hashes Scanned : {total}")
    print(f"Detected             : {detected}")
    print(f"Unknown              : {unknown}")
    print(f"Detection Rate       : {detection_rate:.2f}%")
    print(f"Most Common Hash     : {most_common}")
    print()
    print("Hash Type Breakdown")
    print("=" * 50)

    for hash_type, count in stats.items():
        percentage = (count / total) * 100
        print(
            f"{hash_type:<12} : {count} ({percentage:.2f}%)"
        )

    print()
    print("Confidence Breakdown")
    print("=" * 50)
    print(f"High   : {confidence_stats['High']}")
    print(f"Medium : {confidence_stats['Medium']}")
    print(f"Low    : {confidence_stats['Low']}")
