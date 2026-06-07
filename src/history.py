import os

def view_history():

    log_file = "logs/hash_identifier.log"

    if not os.path.exists(log_file):
        print("No history found.")
        return

    print("\nScan History")
    print("=" * 50)

    with open(log_file, "r") as file:

        lines = file.readlines()

        if not lines:
            print("History is empty.")
            return

        for line in lines[-20:]:
            print(line.strip())

def clear_history():

    log_file = "logs/hash_identifier.log"

    if not os.path.exists(log_file):
        print("No history found.")
        return

    with open(log_file, "w") as file:
        file.write("")

    print("History cleared.")
