questions = {
    "1 + 1 ":"2",
    "What is the capital of China":"Bejing",
    "What is the capital of Japan":"Tokyo"
}


number_of_items = len(questions)
correct_items = 0

for question, answer in questions.items():
    item = input(f"{question} : ")
    if(item == answer):
        correct_items += 1
    if item.lower() == "quit":
        break

print(f"{correct_items} / {number_of_items} correct") 
