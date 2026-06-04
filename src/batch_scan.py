from src.detector import identify_hash

def scan_file(file_path):
    try:
        with open(file_path, "r")as file:
            hashes=file.readlines()
        print("\nBatch Scan Result")
        print("=" * 50)

        for index, hash_value in enumerate(hashes, start=1):
            hash_value= hash_value.strip()

            if not hash_value:
                continue

            result = identify_hash(hash_value)

            print( 
                f"[{index}]"
                f"{result['name']}"
                f"({len(hash_value)} chars)"
)

    except FileNotFoundError:

        print("File Not Found.")
