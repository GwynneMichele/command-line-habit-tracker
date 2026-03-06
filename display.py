from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()


def show_title():
    """Display the application title."""
    console.print(
        Panel(
            "[bold magenta]Habit Tracker[/bold magenta]\n[dim]Track habits. Build streaks. Become suspiciously powerful.[/dim]",
            expand=False,
            border_style="bright_blue",
        )
    )


def show_menu():
    """Display the main menu and return the user's choice."""
    menu_text = (
        "[bold cyan]1.[/bold cyan] View Habits\n"
        "[bold cyan]2.[/bold cyan] Mark Habit as Done\n"
        "[bold cyan]3.[/bold cyan] View Progress\n"
        "[bold cyan]4.[/bold cyan] Add Habit\n"
        "[bold cyan]5.[/bold cyan] Delete Habit\n"
        "[bold cyan]6.[/bold cyan] View Streaks\n"
        "[bold cyan]7.[/bold cyan] Exit"
    )

    console.print(Panel(menu_text, title="Menu", border_style="cyan"))
    return Prompt.ask("[bold yellow]Choose an option[/bold yellow]").strip()


def show_habits(habits):
    """Display all tracked habits in a table."""
    if not habits:
        show_message("No habits are currently being tracked.", "warning")
        return

    table = Table(title="Tracked Habits", border_style="green")
    table.add_column("#", style="cyan", justify="right")
    table.add_column("Habit", style="white")

    for idx, habit in enumerate(habits, 1):
        table.add_row(str(idx), habit)

    console.print(table)


def show_today_progress(today, completed_today):
    """Display habits completed today."""
    if completed_today:
        progress_text = "\n".join(f"• {habit}" for habit in completed_today)
        progress_text += f"\n\n[bold]Total completed:[/bold] {len(completed_today)}"
        console.print(
            Panel(
                progress_text,
                title=f"Today's Progress ({today})",
                border_style="bright_green",
            )
        )
    else:
        console.print(
            Panel(
                f"No habits marked as done for today ({today}).",
                title="Today's Progress",
                border_style="yellow",
            )
        )


def show_streaks(streak_data):
    """Display current and longest streaks in a table."""
    if not streak_data:
        show_message("No streak data available.", "warning")
        return

    table = Table(title="Habit Streaks", border_style="magenta")
    table.add_column("Habit", style="white")
    table.add_column("Current", style="cyan", justify="right")
    table.add_column("Longest", style="green", justify="right")

    for habit, streaks in streak_data.items():
        table.add_row(
            habit,
            str(streaks["current"]),
            str(streaks["longest"]),
        )

    console.print(table)


def show_message(message, message_type="info"):
    """Display a styled status message."""
    styles = {
        "success": "bold green",
        "error": "bold red",
        "warning": "bold yellow",
        "info": "bold blue",
    }

    style = styles.get(message_type, "white")
    console.print(f"[{style}]{message}[/{style}]")


def get_habit_choice(prompt):
    """Prompt the user for a habit number and return a zero-based index."""
    choice = Prompt.ask(f"[bold yellow]{prompt}[/bold yellow]").strip()

    if not choice.isdigit():
        return None

    return int(choice) - 1


def get_new_habit_name():
    """Prompt the user for a new habit name."""
    return Prompt.ask("[bold yellow]Enter the name of the new habit[/bold yellow]").strip()