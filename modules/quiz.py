import random

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
def calculate_points(difficulty):
    """Returns points based on difficulty."""

    points_map = {
        "Easy": 10,
        "Medium": 20,
        "Hard": 30
    }

    return points_map.get(difficulty, 0)     
def run_quiz(questions):
    """Runs the quiz session."""

    score = 0

    for question in questions:

        display_question(question)

        player_answer = get_player_answer()

        is_correct = check_answer(question, player_answer)

        if is_correct:
            points = calculate_points(question["difficulty"])

            score += points

            print(f"\nCorrect! +{points} points")

        else:
            print("\nWrong!")

            print("Correct answer:", question["answer"])

        print("Current Score:", score)

def select_random_questions(questions, count):
    """Selects random questions without repetition."""

    return random.sample(questions, count)        

    print("\nQuiz Complete")
    print("Final Score:", score)