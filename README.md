****What This Application Is Expected To Do****
 
At a high level, the application:

1.	Loads quiz questions from a JSON file 
2.	Displays quiz topics dynamically 
3.	Lets users configure a quiz 
4.	Runs the quiz interactively 
5.	Validates answers 
6.	Calculates scores 
7.	Shows results and explanations 
8.	Saves high scores to a leaderboard file 

This is not *“just a quiz app.”*

It is a complete small software system.

I am building:
1.	A data loader 
2.	A filtering engine 
3.	A scoring engine 
4.	A user interaction loop 
5.	A persistence system 
6.	A reporting system

**Core Programming Concepts Involved**

This project heavily tests these Python concepts:

*Core Fundamentals*
1.	Variables 
2.	Loops 
3.	Conditionals 
4.	Functions 
5.	Lists 
6.	Dictionaries 
7.	Strings 

*Intermediate Concepts*

1.	JSON handling 
2.	File reading/writing 
3.	Error handling with try/except 
4.	Modular programming 
5.	Randomization 
6.	Time tracking 
7.	Input validation 

*Software Engineering Concepts*

1.	Separation of concerns 
2.	Reusability 
3.	Scalability 
4.	Clean architecture 
5.	State management 
6.	Data persistence

**Relationship Between Features**

Every feature depends on another feature.

*Example flow:*

questions.json
↓

load_questions()
↓

extract_topics()
↓

display_menu()
↓

filter_questions()
↓

run_quiz()
↓

calculate_score()
↓

display_results()
↓

save_leaderboard()

**Project Structure**


```text
quiz_project/
│
├── modules/
│   ├── file_handler.py
│   ├── leaderboard.py
│   ├── menu.py
│   └── quiz.py
│
├── questions.json
├── leaderboard.json
├── session_history.json
│
├── quiz_app.py
├── README.md
├── Road map.md
├── functions.md
└── what_the_app_does.md
```

this structure because:

1.	Easier debugging 
2.	Easier scaling 
3.	Cleaner code 
4.	Better separation of concerns

**Program Flow**

Think of the app like stages.

Stage 1:
Load data

Stage 2:
Display menu

Stage 3:
Get quiz configuration

Stage 4:
Prepare questions

Stage 5:
Run quiz loop

Stage 6:
Calculate results

Stage 7:
Save leaderboard

Stage 8:
Return to menu

