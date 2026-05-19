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

        elif 1 <= choice <= len(topics):

            selected_topic = topics[choice - 1]

            print("\nTopic:", selected_topic)

            # FILTER BY TOPIC
            topic_questions = filter_by_topic(
                questions,
                selected_topic
            )

            # DIFFICULTY SELECTION
            print("\nSelect Difficulty")
            print("[1] Easy")
            print("[2] Medium")
            print("[3] Hard")
            print("[4] Mixed")

            difficulty_choice = input("\nChoice: ")

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

            # FILTER BY DIFFICULTY
            topic_questions = filter_by_difficulty(
                topic_questions,
                selected_difficulty
            )

            available_questions = len(topic_questions)

            print(
                f"\nQuestions available: {available_questions}"
            )

            # QUESTION COUNT
            question_count = input(
                "How many questions do you want? "
            )

            try:
                question_count = int(question_count)

                if question_count <= 0:
                    print("Enter a positive number")
                    continue

                if question_count > available_questions:
                    print("Not enough questions available")
                    continue

            except ValueError:
                print("Invalid number")
                continue

            # RANDOM QUESTION SELECTION
            selected_questions = select_random_questions(
                topic_questions,
                question_count
            )

            # START QUIZ
            run_quiz(selected_questions)

        elif choice == len(topics) + 1:
            print("Leaderboard not ready yet")

        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid number")
        