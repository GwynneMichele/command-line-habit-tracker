import json
from datetime import date

HABITS = ["Meditate", "Exercise", "Read", "Write", "Code", "Clean"]
SAVE_FILE = "habits.json"


def load_data():
    """Load saved data from JSON file, or return default structure."""
    default_data = {
        "habits": HABITS.copy(),
        "completions": {}
    }

    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

            if "habits" not in data or not isinstance(data["habits"], list):
                data["habits"] = HABITS.copy()

            if "completions" not in data or not isinstance(data["completions"], dict):
                data["completions"] = {}

            return data

    except (FileNotFoundError, json.JSONDecodeError):
        return default_data


def save_data(data):
    """Save current data to JSON file."""
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_today():
    """Return today's date as a string."""
    return str(date.today())


def show_menu():
    """Display the main menu and return the user's choice."""
    print("\nHabit Tracker")
    print("1. View Habits")
    print("2. Mark Habit as Done")
    print("3. View Progress")
    print("4. Add Habit")
    print("5. Delete Habit")
    print("6. Exit")
    print()
    return input("Choose an option: ").strip()


def show_habits(habits):
    """Display all tracked habits."""
    if not habits:
        print("\nNo habits are currently being tracked.\n")
        return

    print("\nTracked Habits:")
    for idx, habit in enumerate(habits, 1):
        print(f"{idx}. {habit}")
    print()


def add_habit(data):
    """Add a new habit if it does not already exist."""
    new_habit = input("Enter the name of the new habit: ").strip()

    if not new_habit:
        print("Habit name cannot be blank.")
        return

    normalized_habits = [habit.lower() for habit in data["habits"]]
    if new_habit.lower() in normalized_habits:
        print(f"'{new_habit}' is already being tracked.")
        return

    data["habits"].append(new_habit)
    print(f"'{new_habit}' has been added.")


def mark_habit_complete(data):
    """Mark a selected habit as complete for today."""
    if not data["habits"]:
        print("No habits available to mark. Add a habit first.")
        return

    show_habits(data["habits"])
    choice = input("Select a habit to mark as done: ").strip()

    if not choice.isdigit():
        print("Invalid choice. Please enter a number.")
        return

    choice_num = int(choice)
    if not 1 <= choice_num <= len(data["habits"]):
        print("Invalid choice. Please try again.")
        return

    habit = data["habits"][choice_num - 1]
    today = get_today()

    if today not in data["completions"]:
        data["completions"][today] = []

    if habit not in data["completions"][today]:
        data["completions"][today].append(habit)
        print(f"{habit} marked as done for {today}.")
    else:
        print(f"{habit} is already marked as done for {today}.")


def delete_habit(data):
    """Delete a habit from the tracker and remove it from all completion records."""
    if not data["habits"]:
        print("No habits available to delete.")
        return

    show_habits(data["habits"])
    choice = input("Select a habit to delete: ").strip()

    if not choice.isdigit():
        print("Invalid choice. Please enter a number.")
        return

    choice_num = int(choice)
    if not 1 <= choice_num <= len(data["habits"]):
        print("Invalid choice. Please try again.")
        return

    habit = data["habits"][choice_num - 1]
    data["habits"].remove(habit)

    for day in data["completions"]:
        if habit in data["completions"][day]:
            data["completions"][day].remove(habit)

    print(f"{habit} has been deleted from tracked habits.")


def view_today_progress(data):
    """Display habits completed today."""
    today = get_today()
    completed_today = data["completions"].get(today, [])

    if completed_today:
        print(f"\nHabits completed today ({today}):")
        for habit in completed_today:
            print(f"- {habit}")
        print(f"\nTotal completed: {len(completed_today)}")
    else:
        print(f"\nNo habits marked as done for today ({today}).")


def main():
    """Run the habit tracker program."""
    data = load_data()

    while True:
        choice = show_menu()

        if choice == "1":
            show_habits(data["habits"])

        elif choice == "2":
            mark_habit_complete(data)
            save_data(data)

        elif choice == "3":
            view_today_progress(data)

        elif choice == "4":
            add_habit(data)
            save_data(data)

        elif choice == "5":
            delete_habit(data)
            save_data(data)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()