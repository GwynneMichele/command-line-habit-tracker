from utils import get_today


def add_habit(data, new_habit):
    """Add a new habit if it does not already exist."""
    new_habit = new_habit.strip()

    if not new_habit:
        return "Habit name cannot be blank."

    normalized_habits = [habit.lower() for habit in data["habits"]]
    if new_habit.lower() in normalized_habits:
        return f"'{new_habit}' is already being tracked."

    data["habits"].append(new_habit)
    return f"'{new_habit}' has been added."


def mark_habit_complete(data, habit_index):
    """Mark a selected habit as complete for today."""
    if not data["habits"]:
        return "No habits available to mark. Add a habit first."

    if not isinstance(habit_index, int):
        return "Invalid choice. Please enter a number."

    if not 0 <= habit_index < len(data["habits"]):
        return "Invalid choice. Please try again."

    habit = data["habits"][habit_index]
    today = get_today()

    if today not in data["completions"]:
        data["completions"][today] = []

    if habit not in data["completions"][today]:
        data["completions"][today].append(habit)
        return f"{habit} marked as done for {today}."
    else:
        return f"{habit} is already marked as done for {today}."


def delete_habit(data, habit_index):
    """Delete a habit from the tracker and remove it from all completion records."""
    if not data["habits"]:
        return "No habits available to delete."

    if not isinstance(habit_index, int):
        return "Invalid choice. Please enter a number."

    if not 0 <= habit_index < len(data["habits"]):
        return "Invalid choice. Please try again."

    habit = data["habits"][habit_index]
    data["habits"].remove(habit)

    for day in data["completions"]:
        if habit in data["completions"][day]:
            data["completions"][day].remove(habit)

    return f"{habit} has been deleted from tracked habits."


def get_today_progress(data):
    """Return today's date and completed habits."""
    today = get_today()
    completed_today = data["completions"].get(today, [])
    return today, completed_today