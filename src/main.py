from src.banner import show_banner
from src.detector import identify_hash

def main():
	show_banner()
	user_hash = input("\nEnter Hash:")

	result =  identify_hash(user_hash)

	print("\nAnalysis Result")
	print("=" * 50 )
	print(f"Hash Length: {len(user_hash)}")
	print(f"Hash Type: {result['name']}")
	print(f"Description: {result['description']}")
	print(f"Confidence: {result['confidence']}")

if __name__ == "__main__":
    main()
