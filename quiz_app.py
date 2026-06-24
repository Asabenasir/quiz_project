from modules.file_handler import load_questions

from modules.menu import (
    get_topics,
    show_main_menu,
    filter_by_topic,
    filter_by_difficulty
)

from modules.quiz import (
    run_quiz,
    select_random_questions
)

from modules.leaderboard import (
    display_leaderboard
)


questions = load_questions()

topics = get_topics(questions)


while True:

    show_main_menu(topics)

    choice = input("\nSelect a topic number: ")

    try:

        choice = int(choice)

        if choice == len(topics) + 2:

            print("Goodbye")

            break

        elif choice == len(topics) + 1:

            display_leaderboard()

        elif 1 <= choice <= len(topics):

            selected_topic = topics[choice - 1]

            print("\nTopic:", selected_topic)

            topic_questions = filter_by_topic(
                questions,
                selected_topic
            )

            print("\nSelect Difficulty")
            print("[1] Easy")
            print("[2] Medium")
            print("[3] Hard")
            print("[4] Mixed")

            difficulty_choice = input(
                "\nChoice: "
            )

            difficulty_map = {
                "1": "Easy",
                "2": "Medium",
                "3": "Hard",
                "4": "Mixed"
            }

            selected_difficulty = difficulty_map.get(
                difficulty_choice
            )

            if not selected_difficulty:

                print("Invalid difficulty")

                continue

            topic_questions = (
                filter_by_difficulty(
                    topic_questions,
                    selected_difficulty
                )
            )

            available_questions = len(
                topic_questions
            )

            print(
                f"\nQuestions available: "
                f"{available_questions}"
            )

            question_count = input(
                "How many questions do you want? "
            )

            try:

                question_count = int(
                    question_count
                )

                if question_count <= 0:

                    print(
                        "Enter positive number"
                    )

                    continue

                if (
                    question_count >
                    available_questions
                ):

                    print(
                        "Not enough questions"
                    )

                    continue

            except ValueError:

                print(
                    "Invalid number"
                )

                continue

            print("\nSelect Time Limit")

            print("[1] 15 Seconds")
            print("[2] 30 Seconds")
            print("[3] 60 Seconds")
            print("[4] Unlimited")

            time_choice = input(
                "\nChoice: "
            )

            time_limit_map = {
                "1": 15,
                "2": 30,
                "3": 60,
                "4": None
            }

            if (
                time_choice
                not in time_limit_map
            ):

                print(
                    "Invalid time limit"
                )

                continue

            time_limit = (
                time_limit_map[
                    time_choice
                ]
            )

            selected_questions = (
                select_random_questions(
                    topic_questions,
                    question_count
                )
            )

            player_name = input(
                "\nEnter your name: "
            )

            run_quiz(
                selected_questions,
                player_name,
                time_limit,
                selected_difficulty
            )

        else:

            print("Invalid choice")

    except ValueError:

        print("Enter valid number")