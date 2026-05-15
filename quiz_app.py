from modules.file_handler import load_questions
from modules.menu import get_topics, show_main_menu, filter_by_topic

questions = load_questions()
topics = get_topics(questions)

while True:
    show_main_menu(topics)

    choice = input("\nSelect a topic number: ")

    try:
        choice = int(choice)

        if choice == 6:
            print("Goodbye")
            break

        elif 1 <= choice <= len(topics):
            selected_topic = topics[choice - 1]
            print("Topic:", selected_topic)

            topic_questions = filter_by_topic(questions, selected_topic)
            print("Questions available:", len(topic_questions))

        elif choice == 5:
            print("Leaderboard not ready yet")

        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid number")
