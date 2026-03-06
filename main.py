import json
from datetime import date

HABITS = ["Meditate", "Exercise", "Read", "Write", "Code", "Clean"]
SAVE_FILE = "habits.json"

def load_data():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_data(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_menu():
    print("\nHabit Tracker")
    print("1. Add Habit")
    print("2. Mark Habit as Done")
    print("3. View Progress")
    print("4. Exit")
    print()
    return input("Choose an option: ").strip()

def show_habits():
    print("\nAvailable Habits:")
    for idx, habit in enumerate(HABITS, 1):
        print(f"{idx}. {habit}")
    print()

def mark_habit_complete(data):
    show_habits()
    choice = input("Select a habit to mark as done: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(HABITS):
        habit = HABITS[int(choice) - 1]
        today = str(date.today())
        if today not in data:
            data[today] = []
        if habit not in data[today]:
            data[today].append(habit)
            print(f"{habit} marked as done for {today}.")
        else:
            print(f"{habit} is already marked as done for {today}.")
    else:
        print("Invalid choice. Please try again.")

def view_today_progress(data):
    today = str(date.today())
    if today in data:
        print(f"\nHabits completed today ({today}):")
        for habit in data[today]:
            print(f"- {habit}")
    else:
        print(f"\nNo habits marked as done for today ({today}).")

def main():
    data = load_data()
    while True:
        choice = show_menu()
        if choice == "1":
            show_habits()
        elif choice == "2":
            mark_habit_complete(data)
            save_data(data)
        elif choice == "3":
            view_today_progress(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

