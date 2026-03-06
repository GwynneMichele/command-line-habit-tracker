from datetime import datetime, timedelta
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

def get_streaks(data):
    """Return current and longest streaks for each habit."""
    streaks = {}
    today = datetime.strptime(get_today(), "%Y-%m-%d").date()

    for habit in data["habits"]:
        completed_dates = []

        for day, habits_completed in data["completions"].items():
            if habit in habits_completed:
                completed_date = datetime.strptime(day, "%Y-%m-%d").date()
                completed_dates.append(completed_date)

        completed_dates.sort()

        if not completed_dates:
            streaks[habit] = {"current": 0, "longest": 0}
            continue

        # Calculate longest streak
        longest_streak = 1
        current_run = 1

        for i in range(1, len(completed_dates)):
            if completed_dates[i] == completed_dates[i - 1] + timedelta(days=1):
                current_run += 1
            else:
                current_run = 1

            if current_run > longest_streak:
                longest_streak = current_run

        # Calculate current streak
        completed_dates_set = set(completed_dates)
        current_streak = 0
        check_day = today

        while check_day in completed_dates_set:
            current_streak += 1
            check_day -= timedelta(days=1)

        streaks[habit] = {
            "current": current_streak,
            "longest": longest_streak
        }

    return streaks