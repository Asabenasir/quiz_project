from modules.leaderboard import save_score

import random


def display_question(question):
    """Displays a quiz question."""

    print("-" * 40)

    print("Difficulty:", question["difficulty"])

    print("\n" + question["question"])

    for key, value in question["options"].items():

        print(f"{key}. {value}")

    print("-" * 40)


def get_player_answer():
    """Gets and validates player answer."""

    valid_answers = ["A", "B", "C", "D"]

    while True:

        answer = input(
            "\nYour answer: "
        ).upper()

        if answer in valid_answers:

            return answer

        print(
            "Invalid input. Enter A, B, C, or D."
        )


def check_answer(question, player_answer):
    """Checks if answer is correct."""

    correct_answer = question["answer"]

    return player_answer == correct_answer


def calculate_points(difficulty):
    """Returns points based on difficulty."""

    points_map = {
        "Easy": 10,
        "Medium": 20,
        "Hard": 30
    }

    return points_map.get(
        difficulty,
        0
    )


def select_random_questions(
    questions,
    count
):
    """Selects random questions."""

    return random.sample(
        questions,
        count
    )


def run_quiz(
    questions,
    player_name
):
    """Runs the quiz session."""

    score = 0

    correct_count = 0

    wrong_count = 0

    wrong_answers = []

    total_questions = len(questions)

    for index, question in enumerate(
        questions,
        start=1
    ):

        print(
            f"\nQuestion {index} "
            f"of {total_questions}"
        )

        display_question(question)

        player_answer = get_player_answer()

        is_correct = check_answer(
            question,
            player_answer
        )

        if is_correct:

            points = calculate_points(
                question["difficulty"]
            )

            score += points

            correct_count += 1

            print(
                f"\nCorrect! +{points} points"
            )

        else:

            wrong_count += 1

            wrong_answers.append({
                "question": question,
                "player_answer": player_answer
            })

            print("\nWrong!")

            print(
                "Correct answer:",
                question["answer"]
            )

            print(
                "Explanation:",
                question["explanation"]
            )

        print(
            "Current Score:",
            score
        )

    accuracy = (
        correct_count / total_questions
    ) * 100

    show_results_summary(
        total_questions,
        correct_count,
        wrong_count,
        score,
        accuracy
    )

    review_wrong_answers(
        wrong_answers
    )

    save_score(
        player_name,
        questions[0]["topic"],
        "Mixed",
        score,
        accuracy
    )


def show_results_summary(
    total_questions,
    correct_count,
    wrong_count,
    score,
    accuracy
):
    """Displays final results."""

    print("\n" + "=" * 40)

    print("QUIZ COMPLETE")

    print("=" * 40)

    print(
        f"Questions Attempted: "
        f"{total_questions}"
    )

    print(
        f"Correct Answers: "
        f"{correct_count}"
    )

    print(
        f"Wrong Answers: "
        f"{wrong_count}"
    )

    print(
        f"Accuracy: "
        f"{accuracy:.2f}%"
    )

    print(
        f"Final Score: {score}"
    )

    print(
        "Performance:",
        get_performance_rating(
            accuracy
        )
    )


def get_performance_rating(
    accuracy
):
    """Returns performance rating."""

    if accuracy >= 90:

        return "Excellent"

    elif accuracy >= 75:

        return "Good"

    elif accuracy >= 60:

        return "Fair"

    elif accuracy >= 40:

        return "Needs Work"

    return "Keep Practising"


def review_wrong_answers(
    wrong_answers
):
    """Reviews incorrect answers."""

    if not wrong_answers:

        print(
            "\nPerfect score. "
            "No wrong answers."
        )

        return

    choice = input(
        "\nReview wrong answers? (Y/N): "
    ).upper()

    if choice != "Y":

        return

    for item in wrong_answers:

        question = item["question"]

        player_answer = item[
            "player_answer"
        ]

        print("\n" + "-" * 40)

        print(question["question"])

        for key, value in question[
            "options"
        ].items():

            print(f"{key}. {value}")

        print(
            "\nYour Answer:",
            player_answer
        )

        print(
            "Correct Answer:",
            question["answer"]
        )

        print(
            "Explanation:",
            question["explanation"]
        )