def display_question(question):
    """Displays a single quiz question."""

    print("\n" + "-" * 40)

    print("Topic:", question["topic"])
    print("Difficulty:", question["difficulty"])

    print("\n" + question["question"])

    for key, value in question["options"].items():
        print(f"{key}. {value}")

    print("-" * 40)

def get_player_answer():
    """Gets and validates player answer."""

    valid_answers = ["A", "B", "C", "D"]

    while True:
        answer = input("\nYour answer: ").upper()

        if answer in valid_answers:
            return answer

        print("Invalid input. Enter A, B, C, or D.")

def check_answer(question, player_answer):
    """Checks if answer is correct."""

    correct_answer = question["answer"]

    return player_answer == correct_answer        