from src.history import view_history, clear_history
from src.report import save_report, view_report, save_csv
from src.banner import show_banner
from src.detector import identify_hash
from src.logger import write_log
from src.batch_scan import scan_file
from src.stats import show_stats

GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
RESET  = "\033[0m"

def main():
    show_banner()

    print("\n1. Single Hash Scan")
    print("2. Batch Scan From File")
    print("3. View Statistics")
    print("4. View Latest Report")
    print("5. View Scan History")
    print("6. Clear History")

    choice = input("\nChoose: ").strip()

    if choice == "1":

        user_hash = input("\nEnter Hash: ").strip()

        if not user_hash:
            print("Error: Hash cannot be empty.")
            return

        result = identify_hash(user_hash)

        if result["name"] == "Unknown":
            print("\nAnalysis Result")
            print("=" * 50)
            print("Hash Type   : Unknown")
            print("Description : Hash type not identified")
            print("Confidence  : Low")
            return

        write_log(
            user_hash,
            result["name"]
        )


        report_path = save_report(
            user_hash,
            result
        )

        save_csv(
            user_hash,
            result
        )

        print("\nAnalysis Result")
        print("=" * 50)
        print(f"Hash Length: {len(user_hash)}")
        print(f"Hash Type : {result['name']}")
        print(f"Description: {result['description']}")

        if result["confidence"] == "High":
            print(f"Confidence : {GREEN}{result['confidence']}{RESET}")

        elif result["confidence"] == "Medium":
            print(f"Confidence : {YELLOW}{result['confidence']}{RESET}")

        else:
            print(f"Confidence : {RED}{result['confidence']}{RESET}")

        print(f"Report File : {report_path}")

    elif choice == "2":

        file_path = input(
            "\nEnter File Path: "
        ).strip()

        scan_file(file_path)


    elif choice == "3":

        show_stats()


    elif choice == "4":

        view_report()


    elif choice == "5":

        view_history()


    elif choice == "6":

        clear_history()

    else:

        print("Invalid Choice")


if __name__ == "__main__":
    main()
