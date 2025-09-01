# function

def my_func():
    print("Hello")

count = 0
while count < 5:
    my_func()
    count+=1

# default parameter
def my_func_param(name="Charles", age=4):
    print(f"{name} is {age}")

my_func_param()

# parameter arrangement 
my_func_param(age=54, name="charles")

name_1 = "Joy"
age_1 = 33

my_func_param(name=name_1, age=age_1)

my_func_param(age=99)

# function with return
# and Doctring 
def multipy(a, b):
    # docstring
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a * b

# function with list as parameters
def my_family_func(family):
    for person in family:
        print(f"Name : {person}")

my_family = ["Charles", "Joy"]
my_family_func(my_family)

# variable arguments
def addition(*args):
        return sum(args)

print(addition(2,4,4))

def profile(first_name, last_name, **info):
    info["first_name"] = first_name
    info["last_name"] = last_name
    return info
    
print(profile("Charles", "Amper", age=34, sex="everyday"))