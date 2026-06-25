****Functions****

1. load_questions()
2. display_menu()
3. get_topics()
4. filter_questions()
5. shuffle_questions()
6. display_question()
7. get_player_answer()
8. validate_answer()
9. calculate_score()
10. show_feedback()
11. show_results()
12. save_leaderboard()
13. load_leaderboard()
14. review_wrong_answers()
15. clear_screen()

**Each function does one thing only.**

*Program Flow*

START PROGRAM

load questions

WHILE app running:

    display menu

    get topic selection

    IF exit:
        stop app

    configure quiz

    filter questions

    run quiz

    show results

    save leaderboard

*Loading And Validating JSON*

I will use:

import json

*Example:*

with open("questions.json", "r") as file:

    questions = json.load(file)

*Possible errors:*

1.	File missing 
2.	Invalid JSON 
3.	Empty file 

*Handle using:*

try:

except:

*never assumes files work perfectly.*

Random Question Selection 

I'm using:

import random

*Example:*

random.sample(question_pool, count)

Why this is good:

1.	No duplicates 
2.	Clean implementation 
3.	Built into Python 

*Input Validation**

*Example:*

while True:
    answer = input("Answer: ").upper()

    if answer in ["A", "B", "C", "D"]:
        return answer

    print("Invalid input")

*Never trust users.*

*No hardcoding repeatedly.*

POINTS = {

    "Easy": 10,

    "Medium": 20,

    "Hard": 30

}

Why?

1.	Easier maintenance 
2.	Cleaner code 
3.	Scalable 

Leaderboard Persistence 

building persistence.

**Important backend concept**

Process:

1.	Read existing leaderboard 
2.	Add new score 
3.	Sort scores 
4.	Keep top 10 
5.	Save back to file 

(This teaches real-world data management.)

*Python Concepts I plan to Revise*

Before starting:

1.	Functions 
2.	Lists and dictionaries 
3.	Loops 
4.	Conditionals 
5.	JSON handling 
6.	File reading/writing 
7.	try/except 
8.	random module 
9.	datetime module 

Later:

1.	classes 
2.	decorators 
3.	threading 
4.	async timers 

