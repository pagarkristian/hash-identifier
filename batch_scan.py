import os
import json
from src.detector import identify_hash
 
def scan_file(file_path):
    try:
        # Membaca semua baris hash dari file target
        with open(file_path, "r") as file:
            hashes = file.readlines()
 
        total = 0
        detected = 0
        unknown = 0
        hash_stats = {}
 
        print("\nHasil Pemindaian Massal")
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
                f"({len(hash_value)} karakter)"
            )
 
            hash_name = result["name"]
            hash_stats[hash_name] = hash_stats.get(hash_name, 0) + 1
 
            if hash_name == "Unknown":
                unknown += 1
            else:
                detected += 1
 
        print()
        print("=" * 50)
        print("Ringkasan Pemindaian Massal")
        print("=" * 50)
 
        print(f"Total Hash      : {total}")
        print(f"Terdeteksi      : {detected}")
        print(f"Tidak Diketahui : {unknown}")
 
        if total > 0:
            detection_rate = (detected / total) * 100
        else:
            detection_rate = 0
 
        print(f"Tingkat Deteksi : {detection_rate:.2f}%")
 
        if hash_stats:
            most_common = max(hash_stats, key=hash_stats.get)
            print()
            print(f"Hash Paling Umum : {most_common}")
        else:
            most_common = "None"
 
        # Membuat direktori 'reports' jika belum ada
        os.makedirs("reports", exist_ok=True)
 
        stats_data = {
            "total_hashes": total,
            "detected": detected,
            "unknown": unknown,
            "detection_rate": round(detection_rate, 2),
            "most_common_hash": most_common,
            "hash_types": hash_stats
        }
 
        # Mengekspor statistik ke file JSON
        with open("reports/stats.json", "w") as stats_file:
            json.dump(stats_data, stats_file, indent=4)
 
        print()
        print("Statistik berhasil diekspor ke:")
        print("reports/stats.json")
 
    except FileNotFoundError:
        print("Berkas Tidak Ditemukan.")
    except PermissionError:
        print("Akses Ditolak (Permission Denied).")
    except Exception as error:
        print(f"Kesalahan Tak Terduga: {error}")
