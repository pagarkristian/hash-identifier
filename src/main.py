from src.banner import show_banner
from src.detector import identify_hash
from src.report import save_report


def main():
	show_banner()
	user_hash = input("\nEnter Hash:")

	result =  identify_hash(user_hash)
	report_path = save_report(user_hash, result)

	print("\nAnalysis Result")
	print("=" * 50 )
	print(f"Hash Length: {len(user_hash)}")
	print(f"Hash Type: {result['name']}")
	print(f"Description: {result['description']}")
	print(f"Confidence: {result['confidence']}")
	print(f"Report File : {report_path}")

if __name__ == "__main__":
    main()
