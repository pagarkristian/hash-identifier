import os
import json

def show_stats():
    log_file = "logs/hash_identifier.log"

    if not os.path.exists(log_file):
        print("No logs found.")
        return

    stats = {}

    with open(log_file, "r") as file:
        for line in file:
            if "TYPE=" not in line:
                continue

            hash_type = line.split("TYPE=")[1].strip()

            stats[hash_type] = stats.get(hash_type, 0) + 1

    total = sum(stats.values())

    print("\nStatistics")
    print("=" * 50)
    print(f"Total Hashes Scanned : {total}")
    print()

    for hash_type, count in stats.items():
        percentage = (count / total) * 100

        print(
            f"{hash_type:<10} : {count} ({percentage:.2f}%)"
        )
