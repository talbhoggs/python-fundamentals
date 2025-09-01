# This activity allows you to enter student name
# and provide notes to it. Once your done it will
# list all the student you enter and equivalent notes
# you have written

students = {}

print("Enter student details or enter quit to exit")
while True:
    name = input("Name: ")
    if name.lower() == "quit":
        break
    note = input(f"Note: ") 
    students[name] = note if note else "None"
    
print("\n----- Student List -----") 
for name, note in students.items():
    print(f"{name} -{note}")