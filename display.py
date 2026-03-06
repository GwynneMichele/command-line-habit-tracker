def show_menu():
    """Display the main menu and return the user's choice."""
    print("\nHabit Tracker")
    print("1. View Habits")
    print("2. Mark Habit as Done")
    print("3. View Progress")
    print("4. Add Habit")
    print("5. Delete Habit")
    print("6. View Streaks")
    print("7. Exit")
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


def show_today_progress(today, completed_today):
    """Display habits completed today."""
    if completed_today:
        print(f"\nHabits completed today ({today}):")
        for habit in completed_today:
            print(f"- {habit}")
        print(f"\nTotal completed: {len(completed_today)}")
    else:
        print(f"\nNo habits marked as done for today ({today}).")


def show_streaks(streak_data):
    """Display current and longest streaks for each habit in aligned columns."""
    if not streak_data:
        print("\nNo streak data available.\n")
        return

    print("\nHabit Streaks:")
    print(f"{'Habit':<15}{'Current':<10}{'Longest':<10}")
    print("-" * 35)

    for habit, streaks in streak_data.items():
        print(f"{habit:<15}{streaks['current']:<10}{streaks['longest']:<10}")

    print()


def get_habit_choice(prompt):
    """Prompt the user for a habit number and return a zero-based index."""
    choice = input(prompt).strip()

    if not choice.isdigit():
        return None

    return int(choice) - 1


def get_new_habit_name():
    """Prompt the user for a new habit name."""
    return input("Enter the name of the new habit: ").strip()