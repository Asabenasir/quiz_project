def get_topics(questions):
    """Extracts unique quiz topics.""" #docstring

    topics = []

    for question in questions:
        topic = question["topic"]

        if topic not in topics:
            topics.append(topic)

    return topics

def show_main_menu(topics):
    """Displays main menu."""

    print("\nQUIZ APPLICATION\n")

    for index, topic in enumerate(topics, start=1):
        print(f"[{index}] {topic}")

    print("[5] View Leaderboard")
    print("[6] Exit")



def filter_by_topic(questions, topic):
    filtered = []

    for q in questions:
        if q["topic"] == topic:
            filtered.append(q)

    return filtered

