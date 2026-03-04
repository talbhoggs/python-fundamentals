import requests

# variables
var_ma = "Charles"
_var_ma = "test"

# Data types
# Number
# Whole number
w_num1 = 12
w_num2: int = 2 # type anotation
                # we can eplicitly add the type but optional

print("Arthimetics : ##########")
print(f'''{w_num1} + {w_num2} = {w_num1 + w_num2}''')
print(f'''{w_num1} - {w_num2} = {w_num1 - w_num2}''')
print(f'''{w_num1} // {w_num2} = {w_num1 // w_num2}''')
print(f'''{w_num1} * {w_num2} = {w_num1 * w_num2}''')
print(f'''{w_num1} ** {w_num2} = {w_num1 ** w_num2}''')
print(f'''{w_num1} % {w_num2} = {w_num1 % w_num2}''')

# Float
w_num_f = 12.3
print(f'''Float {w_num_f}''')
# complex
var_com = 4 + 3j
print("######## Complex number #########")
print(var_com.real)
print(var_com.imag)
print(var_com)

# Strings
print("########## String ##################")
my_number = 1
my_comment = f'''This multi comment is a comment {my_number}'''
my_comment1 = f'This is {my_number} value'
print("Hello")
print(my_comment)
print(my_comment1)

# if else, elif, in keyword
# immutable list
print("############### if else / elif ###################")
countries = ("China", "India")
print(countries)
if "China" in countries:
    print("Yes it is!")
else:
    print("Nope!")

# boolean
is_true = True
is_false = False
print(10 > 5)
print(3 == 7)
print(8 >= 7)

print(bool(0))
print(bool(5))
print(bool(""))
print(bool("Hi"))

if is_true:
    print("Yes it is true")

temperature = 33 
if temperature > 38:
    print("too hot")
elif temperature <= 38 and temperature >= 32:
    print("fair temperature")
else:
    print("too cold")

# None
# No value
var_none = None
if var_none is None:
    print("Variable has no value")

# Type casting
num = 10
str_num = str(num)
print(type(str_num))

# Operator

# logical operator
# and, or, not

# inequality
# != == 

# ternary
name = "Charles" 
value = name if name else "No name"
print("####### ternary #######")
print("name if name else \"No name\"")
print(value)

# inputs
name = input(f"What is your name?")
age = int(input(f"Please type your age."))
print(f"Your name is {name} your age {age}")


from mypackage.math_utils import square
print("######## importing a package #####")
print(f'''square of 4 = {square()}''')


# *args, **kwargs
# *args accepts list
# *kwargs accepts dictionary
def order_food(item, *args, **kwargs)->None:
    print("Item : ", item)
    print("Extras : ", args)
    print("Details : ", kwargs)

# correct approach
order_food("Pizza","Cheese","Hotdog",delivery=True, tip=10)

item = "Pizza"
extras = ["Olives, Pepper"]
details = {"delivery": False, "tip": 3}
# not correct
order_food(item, extras, details)

# decorator
# a function that takes another function as input and returns a new function with added behavior
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
# assert
# good for debuging
# this will return a Assertion Error if condition is not true
assert_var = 10
assert assert_var < 1, "Variable should be greater"
print("Variable is greater than 1")

