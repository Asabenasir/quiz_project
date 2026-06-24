from modules.leaderboard import save_score

import random
import time


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

    return (
        player_answer ==
        question["answer"]
    )


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


def get_timed_answer():
    """Gets answer and tracks elapsed time."""

    start_time = time.time()

    answer = get_player_answer()

    end_time = time.time()

    elapsed_time = (
        end_time - start_time
    )

    return answer, elapsed_time


def calculate_time_bonus(
    difficulty,
    remaining_time
):
    """Calculates time bonus."""

    multiplier_map = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    multiplier = multiplier_map.get(
        difficulty,
        0
    )

    return int(
        remaining_time * multiplier
    )


def select_random_questions(
    questions,
    count
):
    """Selects random questions without repetition."""

    return random.sample(
        questions,
        count
    )


def run_quiz(
    questions,
    player_name,
    time_limit,
    selected_difficulty
):
    """Runs the quiz session."""

    session_start = time.time()

    score = 0
    total_bonus = 0

    correct_count = 0
    wrong_count = 0
    timed_out_count = 0

    wrong_answers = []

    question_history = []

    total_questions = len(
        questions
    )

    for index, question in enumerate(
        questions,
        start=1
    ):

        print(
            f"\nQuestion {index} "
            f"of {total_questions}"
        )

        display_question(question)

        if time_limit is None:

            player_answer = (
                get_player_answer()
            )

            elapsed_time = 0

        else:

            (
                player_answer,
                elapsed_time
            ) = get_timed_answer()

            if (
                elapsed_time >
                time_limit
            ):

                print(
                    "\nTime expired!"
                )

                timed_out_count += 1
                wrong_count += 1

                question_history.append(
           {
                "question":
                question["question"],
                "result":
                "Timed Out"
            }
        )

                continue

        is_correct = check_answer(
            question,
            player_answer
        )

        if is_correct:

            points = (
                calculate_points(
                    question["difficulty"]
                )
            )

            score += points

            correct_count += 1

            question_history.append(
               {
                    "question":
                    question["question"],
                    "result":
                    "Correct"
                }
            ) 

            print(
                f"\nCorrect! "
                f"+{points} points"
            )

            if (
                time_limit
                is not None
            ):

                remaining_time = max(
                    0,
                    time_limit -
                    elapsed_time
                )

                bonus = (
                    calculate_time_bonus(
                        question["difficulty"],
                        remaining_time
                    )
                )

                total_bonus += bonus

                score += bonus

                print(
                    f"Time Used: "
                    f"{elapsed_time:.2f}s"
                )

                print(
                    f"Time Remaining: "
                    f"{remaining_time:.2f}s"
                )

                print(
                    f"Time Bonus: "
                    f"+{bonus}"
                )

        else:

            wrong_count += 1

            question_history.append(
                {
                "question":
                question["question"],
                "result":
                "Wrong"
          }
    )

            wrong_answers.append(
                {
                    "question": question,
                    "player_answer":
                    player_answer
                }
            )

            print("\nWrong!")

            print(
                "Correct Answer:",
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

    session_end = time.time()

    total_time = (
        session_end -
        session_start
    )

    accuracy = (
        correct_count /
        total_questions
    ) * 100

    average_time = (
        total_time /
        total_questions
    )

    show_results_summary(
        total_questions,
        correct_count,
        wrong_count,
        timed_out_count,
        score,
        total_bonus,
        accuracy,
        total_time,
        average_time,
        question_history
    )
    
    

    review_wrong_answers(
        wrong_answers
    )

    save_score(
        player_name,
        questions[0]["topic"],
        "mixed",
        score,
        accuracy,
        correct_count,
        wrong_count,
        timed_out_count,
        total_questions  
    )

def show_question_breakdown(question_history):
    """Displays per-question results."""

    print("\n" + "=" * 50)

    print("QUESTION BREAKDOWN")

    print("=" * 50)

    for index, item in enumerate(
        question_history,
        start=1
    ):

        print(
            f"{index}. "
            f"{item['result']} | "
            f"{item['question']}"
        )

def show_results_summary(
    total_questions,
    correct_count,
    wrong_count,
    timed_out_count,
    score,
    total_bonus,
    accuracy,
    total_time,
    average_time,
    question_history
):
    """Displays final results."""

    print("\n" + "=" * 50)

    print("QUIZ COMPLETE")

    print("=" * 50)

    print(
        f"Questions Attempted : "
        f"{total_questions}"
    )

    print(
        f"Correct Answers     : "
        f"{correct_count}"
    )

    print(
        f"Wrong Answers       : "
        f"{wrong_count}"
    )

    print(
        f"Timed Out           : "
        f"{timed_out_count}"
    )

    print(
        f"Accuracy            : "
        f"{accuracy:.2f}%"
    )

    print(
        f"Total Time          : "
        f"{total_time:.2f}s"
    )

    print(
        f"Average Time/Q      : "
        f"{average_time:.2f}s"
    )

    print(
        f"Time Bonus Earned   : "
        f"{total_bonus}"
    )

    print(
        f"Final Score         : "
        f"{score}"
    )

    print(
        f"Performance         : "
        f"{get_performance_rating(accuracy)}"
    )

    print("=" * 50)

    show_question_breakdown(
        question_history
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

        print(
            question["question"]
        )

        for key, value in question[
            "options"
        ].items():

            print(
                f"{key}. {value}"
            )

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