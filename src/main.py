from src.banner import show_banner
from src.detector import identify_hash
from src.report import save_report
from src.logger import write_log
from src.batch_scan import scan_file

def main():

    show_banner()

    print("\n1. Single Hash Scan")
    print("2. Batch Scan From File")

    choice = input("\nChoose: ")

    if choice == "1":

        user_hash = input("\nEnter Hash: ")

        result = identify_hash(user_hash)

        write_log(
            user_hash,
            result["name"]
        )

        report_path = save_report(
            user_hash,
            result
        )

        print("\nAnalysis Result")
        print("=" * 50)
        print(f"Hash Length: {len(user_hash)}")
        print(f"Hash Type: {result['name']}")
        print(f"Description: {result['description']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Report File : {report_path}")

    elif choice == "2":

        file_path = input(
            "\nEnter File Path: "
        )

        scan_file(file_path)

    else:

        print("Invalid Choice")

if __name__ == "__main__":
    main()
