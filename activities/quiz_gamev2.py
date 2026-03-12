import os
exams = [
    {
        "question": "What 2 + 2?",
        "choices": [
            {"text": "3", "correct": False},
            {"text": "555", "correct": False},
            {"text": "2", "correct": False},
            {"text": "4", "correct": True},
        ]
    }, {
        "question": "What is the capital of France?",
        "choices": [
            {"text": "London", "correct": False},
            {"text": "Berlin", "correct": False},
            {"text": "Madrid", "correct": False},
            {"text": "Paris", "correct": True},
    ]
    }
]
def clear_screen():
    os.system("clear")

while True:
    clear_screen()
    correct_answer_count = 0
    for i, exam in enumerate(exams, start=1):
        correct_answer = ""
        print(f"\n--- Question: {i} / {len(exams)} ---\n")
        print(f'{i}. {exam["question"]}\n')

        for choice in exam["choices"]:
            print(choice["text"])
            if choice["correct"]:
                correct_answer = choice["text"]

        answer = input("\nanswer : ")
        clear_screen()
    
        if correct_answer.lower() == answer.lower():
            correct_answer_count+=1
        if answer.lower() == "quit": 
            exit()
        if i == len(exams):
            print("Thank you! Your score is:") 
            print(f"({correct_answer_count} / {i}) correct\n")
            exit()

# TODO
# Convert this to objects so mypy will not give a warning
# Add choice, user input (a, b, c, d) not the value itself