from display import show_menu, show_habits, view_today_progress
from storage import load_data, save_data
from tracker import add_habit, delete_habit, mark_habit_complete


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