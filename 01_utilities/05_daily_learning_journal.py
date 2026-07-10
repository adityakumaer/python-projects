from datetime import datetime

file_name = "learning_journal.txt"

entry = input("\nWhat did you learn today? ")
rating = input("How would you rate your learning experience today (1-5)? ")

if 1 <= int(rating) <= 5:
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    journal_entry = f"\nDate: {date_time}\n{entry}\n"
    if rating:
        journal_entry += f"Rating: {rating}/5\n"
    journal_entry += "-" * 40 + "\n"

    with open(file_name, "a") as file:
        file.write(journal_entry)

    print(f'\nYour entry has been saved to "{file_name}".')

else:
    raise ValueError("Rating must be between 1 and 5.")
