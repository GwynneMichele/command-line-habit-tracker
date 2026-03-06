import json

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