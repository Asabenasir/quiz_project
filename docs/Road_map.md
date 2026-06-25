****Roadmap:****


**Phase 1. I Build the Skeleton**

*Goal:*

***Application runs without crashing***

*Build:*
1.	Welcome screen 
2.	Main menu 
3.	Exit option 

No adding of quiz logic yet.

**Phase 2. JSON Loading**

Learn:
1.	json.load() 
2.	try/except 
3.	File handling

*Build:*
def load_questions():

Focus:
1.	File exists? 
2.	JSON valid? 
3.	Data structure correct? 

**Phase 3.**

**Dynamic Topics**

Extract unique topics from questions.

*Example:*

topics = set()

*This teaches data extraction.*

**Phase 4. Display Questions**

*Build:*

def display_question(question):

Only display first.

Do not score yet.

**Phase 5. Answer Validation**

*Build:*

def get_valid_answer():

Validate:
1.	A 
2.	B 
3.	C 
4.	D 

Case insensitive.

**Phase 6. Scoring System**

*Build:*


def calculate_score():

Start simple:
1.	Correct = points 
2.	Wrong = 0 

I’m adding bonuses later.

**Phase 7. Quiz Loop**

This is the heart of the app.

*flow:*

*FOR each question:*

    display question
    get answer
    check answer
    update score
    show feedback

**Phase 8. Results Summary**

*Build statistics:*
1.	Correct count 
2.	Wrong count 
3.	Accuracy 
4.	Score percentage 

**Phase 9. Leaderboard**

*Learn:*
1.	Writing JSON 
2.	Reading JSON 
3.	Sorting scores 

**Phase 10. Timers**

Timers come near the end.



