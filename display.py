from utils import get_today


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