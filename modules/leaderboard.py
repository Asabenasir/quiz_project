import json
import os
from datetime import datetime


def load_leaderboard():
    """Loads leaderboard data."""

    if not os.path.exists("leaderboard.json"):

        with open("leaderboard.json", "w") as file:
            json.dump([], file)

    try:

        with open("leaderboard.json", "r") as file:
            return json.load(file)

    except json.JSONDecodeError:

        return []


def save_score(
    player_name,
    topic,
    difficulty,
    score,
    accuracy
):
    """Saves score to leaderboard."""

    leaderboard = load_leaderboard()

    new_entry = {
        "player": player_name,
        "topic": topic,
        "difficulty": difficulty,
        "score": score,
        "accuracy": accuracy,
        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    leaderboard.append(new_entry)

    leaderboard.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    leaderboard = leaderboard[:10]

    with open("leaderboard.json", "w") as file:
        json.dump(
            leaderboard,
            file,
            indent=4
        )


def display_leaderboard():
    """Displays leaderboard."""

    leaderboard = load_leaderboard()

    if not leaderboard:

        print("\nNo leaderboard data yet.")

        return

    print("\n" + "=" * 50)

    print("LEADERBOARD")

    print("=" * 50)

    for index, entry in enumerate(
        leaderboard,
        start=1
    ):

        print(
            f"{index}. "
            f"{entry['player']} | "
            f"{entry['topic']} | "
            f"Score: {entry['score']} | "
            f"{entry['accuracy']:.2f}%"
        )