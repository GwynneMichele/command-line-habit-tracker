from display import show_habits
from utils import get_today


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