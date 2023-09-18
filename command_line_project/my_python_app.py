import os
import datetime

def create_journal_entry():
    date = datetime.datetime.now().strftime("YYYY-MM-DD")
    entry = input("Write your journal entry for today: ")

    if not os.path.exists("data/journal_entries"):
        os.makedirs("data/journal_entries")

    with open(f"data/journal_entries/{date}.txt", "w") as file:
        file.write(entry)

    print("Journal entry saved successfully!")

def view_journal_entry(date):
    try:
        with open(f"data/journal_entries/{date}.txt", "r") as file:
            entry = file.read()
            print(f"Journal entry for {date}:\n")
            print(entry)
    except FileNotFoundError:
        print("No journal entry found for this date.")

