import os
import datetime

def create_journal_entry():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    entry = input("Write your journal entry for today: ")

    if not os.path.exists("data/journal_entries"):
        os.makedirs("data/journal_entries")

    with open(f"data/journal_entries/{date}.txt", "w") as file:
        file.write(entry)

    print("Your journal entry has been saved successfully!")

def view_journal_entry(date):
    try:
        with open(f"data/journal_entries/{date}.txt", "r") as file:
            entry = file.read()
            print(f"Journal entry for {date}:\n")
            print(entry)
    except FileNotFoundError:
        print("No journal entry found for this date. Please try another date")

def search_journal_entries(keyword):
    entries_found = False

    for filename in os.listdir("data/journal_entries"):
        if filename.endswith(".txt"):
            with open(os.path.join("data/journal_entries", filename), "r") as file:
                entry = file.read()
                if keyword in entry:
                    date = filename.split(".")[0]
                    print(f"Found in the entry for {date}:\n")
                    print(entry)
                    entries_found = True

    if not entries_found:
        print("No entries found with the specified keyword.")

if __name__ == "__main__":
    print("Welcome to the Daily Journal App!")

    while True:
        print("\nOptions:")
        print("1. Create Journal Entry")
        print("2. View Journal Entry")
        print("3. Search Journal Entries")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_journal_entry()
        elif choice == "2":
            date = input("Please enter the date (YYYY-MM-DD): ")
            view_journal_entry(date)
        elif choice == "3":
            keyword = input("Please enter a keyword to search for: ")
            search_journal_entries(keyword)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 4.")