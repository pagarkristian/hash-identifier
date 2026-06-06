import os
import json
from src.detector import identify_hash
 
def scan_file(file_path):
    try:
       
        with open(file_path, "r") as file:
            hashes = file.readlines()
 
        total = 0
        detected = 0
        unknown = 0
        hash_stats = {}
 
        print("\nMass Scan Results")
        print("=" * 50)
 
        for index, hash_value in enumerate(hashes, start=1):
            hash_value = hash_value.strip()
 
            if not hash_value:
                continue
 
            total += 1
 
            result = identify_hash(hash_value)
 
            print(
                f"[{index}] "
                f"{result['name']} "
                f"({len(hash_value)} character)"
            )
 
            hash_name = result["name"]
            hash_stats[hash_name] = hash_stats.get(hash_name, 0) + 1
 
            if hash_name == "Unknown":
                unknown += 1
            else:
                detected += 1
 
        print()
        print("=" * 50)
        print("Bulk Scan Summary")
        print("=" * 50)
 
        print(f"Total Hash      : {total}")
        print(f"Detected      : {detected}")
        print(f"Unknown : {unknown}")
 
        if total > 0:
            detection_rate = (detected / total) * 100
        else:
            detection_rate = 0
 
        print(f"Detection Rate : {detection_rate:.2f}%")
 
        if hash_stats:
            most_common = max(hash_stats, key=hash_stats.get)
            print()
            print(f"Most Common Hashes : {most_common}")
        else:
            most_common = "None"
 
       
        os.makedirs("reports", exist_ok=True)
 
        stats_data = {
            "total_hashes": total,
            "detected": detected,
            "unknown": unknown,
            "detection_rate": round(detection_rate, 2),
            "most_common_hash": most_common,
            "hash_types": hash_stats
        }
 
        
        with open("reports/stats.json", "w") as stats_file:
            json.dump(stats_data, stats_file, indent=4)
 
        print()
        print("Statistics successfully exported to:")
        print("reports/stats.json")
 
    except FileNotFoundError:
        print("File Not Found.")
    except PermissionError:
        print("Permission Denied.")
    except Exception as error:
        print(f"Unexpected Error: {error}")
