# Dictionary
# key value pairs
# B0001


person ={"name":"Charles", "age": 28, "city": "Talisay"}

# retriving
age = person["age"]
name = person.get("name")

print(person)

# modify
person["age"] = 44
person.pop("city")
# person.popitem() pop the last item
del person["age"]
# person.clear()
print(person)

# iterating
person ={"name":"Charles", "age": 28, "city": "Talisay"}

for key in person:
    print(f"key -> {key}")

for value in person.values():
    print(f"value -> {value}")

for key, value in person.items():
    print(f"key => {key} :: value => {value}")

# nested dictionary
company_employees = {
    "ceo": {"name":"Charles", "age": 43},
    "gm": {"name":"Joy", "age": 37}
}

for position, person in company_employees.items():
    print(f"position: {position} \nname: {person.get("name")}")
    
# dictionary with list inside
students = {
    "Charles": ["Math", "English"],
    "Joy": ["Filipino", "Math"]
}

for student, subjects in students.items():
    print(student)
    for subject in subjects:
        print(f"- {subject}") 

