import requests

# Strings
my_number = 1
my_comment = f'''This multi comment is a comment {my_number}'''
my_comment1 = f'This is {my_number} value'

print("Hello")
print(my_comment)
print(my_comment1)

# Numbers
value = 4
value1 = 3

result = 4 / 3
print(result)

# if else, elif, in keyword
if "China" in countries:
    print("Yes it is!")
else:
    print("Nope!")

is_true = True # boolean
if is_true:
    print("Yes it is true")

temperature = 33 
if temperature > 38:
    print("too hot")
elif temperature <= 38 and temperature >= 32:
    print("fair temperature")
else:
    print("too cold")

# Operator

# logical operator
# and, or, not

# inequality
# != == 

# ternary
name = "Charles" 
value = name if name else "No name"
print(value)

# inputs
name = input(f"What is your name?")
age = int(input(f"Please type your age."))
print(f"Your name is {name} your age {age}")

from mypackage import square
print(square())
