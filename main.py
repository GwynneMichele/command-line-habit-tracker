from display import (
    show_menu,
    show_habits,
    show_today_progress,
    show_streaks,
    get_habit_choice,
    get_new_habit_name,
)
from storage import load_data, save_data
from tracker import (
    add_habit,
    delete_habit,
    mark_habit_complete,
    get_today_progress,
    get_streaks,
)


def main():
    """Run the habit tracker program."""
    data = load_data()

    while True:
        choice = show_menu()

        if choice == "1":
            show_habits(data["habits"])

        elif choice == "2":
            show_habits(data["habits"])
            habit_index = get_habit_choice("Select a habit to mark as done: ")
            message = mark_habit_complete(data, habit_index)
            print(message)
            save_data(data)

        elif choice == "3":
            today, completed_today = get_today_progress(data)
            show_today_progress(today, completed_today)

        elif choice == "4":
            new_habit = get_new_habit_name()
            message = add_habit(data, new_habit)
            print(message)
            save_data(data)

        elif choice == "5":
            show_habits(data["habits"])
            habit_index = get_habit_choice("Select a habit to delete: ")
            message = delete_habit(data, habit_index)
            print(message)
            save_data(data)

        elif choice == "6":
            streak_data = get_streaks(data)
            show_streaks(streak_data)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()