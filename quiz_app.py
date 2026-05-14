import json

with open("questions.json", "r") as file:
    questions = json.load(file)

print("Questions loaded successfully!")
print("Total questions:", len(questions))


