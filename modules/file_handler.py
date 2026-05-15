import json


def load_questions():
    """Loads questions from the JSON file.""" #docstring

    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)

        return questions

    except FileNotFoundError:
        print("Error: questions.json file not found.")
        return []

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []