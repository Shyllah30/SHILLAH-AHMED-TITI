quiz = [
    {
        "question": "How many bits are in a byte?",
        "options": ["a. 10", "b. 8", "c.6", "d. 4"],
        "anwer": "b"
    },
    {
        "question": "which of the following is a brain of the computer?",
        "options":["a. RAM", "b. ROM", "c.processor", "d.chip"],
        "answer":"c"    
    },
    {    "question": "How month are in a year?",
        "options":["a. 2", "b. 10","c. 13","d. 12"],
        "answer":"d"    

    },
    {   "question": "how many days are in aweek?",
        "options": ["a. 10" , "b. 7" , "c.6","d. 4"],
        "anwer": "b"
    },

    {   "question": "whats my name?",
        "options": ["a. 1isa" , "b. shillah" , "c.mary","d. ice"],
        "anwer": "b"
    },

]
score = 0
for question in quiz:
    print(question["question"])
    
    for option in question["options"]:
        print(option)


    Answer = input("Select option: ")
    if Answer == question["Answer"]:
        print("correct")
        score += 5
    else:
        print("wrong")
print(score)