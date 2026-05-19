def get_topics(questions):
    """Extracts unique quiz topics."""

    topics = set()

    for question in questions:
        topics.add(question["topic"])

    return sorted(topics)


def show_main_menu(topics):
    """Displays main menu."""

    print("\nQUIZ APPLICATION\n")

    for index, topic in enumerate(topics, start=1):
        print(f"[{index}] {topic}")

    print(f"[{len(topics) + 1}] View Leaderboard")
    print(f"[{len(topics) + 2}] Exit")


def filter_by_topic(questions, topic):
    filtered = []

    for q in questions:
        if q["topic"] == topic:
            filtered.append(q)

    return filtered

def filter_by_difficulty(questions, difficulty):
    """Filters questions by difficulty."""

    if difficulty == "Mixed":
        return questions

    filtered = []

    for question in questions:
        if question["difficulty"] == difficulty:
            filtered.append(question)

    return filtered