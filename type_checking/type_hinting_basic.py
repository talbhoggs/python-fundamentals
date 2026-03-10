from pydantic import validate_call

# Type hinting 
# - is adding meta data type to your program (str, int, dict, .. etc)
# Type checking 
# - is checking type of you variable (install mypy)
# Validation 
# - is validation the type manually

def create_employee(first_name:str, last_name:str, age:int) -> dict:

    # manual validation
    if not isinstance(first_name, str):
        raise TypeError("first name must be string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be string")
    if not isinstance(age, int):
        raise TypeError("age must be int")
    
    email = f"{first_name}-{last_name}@company.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email
    }

# print(create_employee("charles", "amper", 19))

# this is how type check will do
# it warn us that the input you provide is not a proper type
# this example: "17" type should be int 17
print(create_employee("charles", "amper", "17"))

# Use of pydantic for validation
# pydantic uses type hints for validation

@validate_call
def create_employee_pydantic(first_name:str, last_name:str, age:int) -> dict:
    
    email = f"{first_name}-{last_name}@company.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email
    }

print(create_employee_pydantic("charles", "amper", "17")) # pydantic will automatically convert to int automatically (it will not validate)
print(create_employee_pydantic("charles", "amper", "seventeen"))

# pydantic
# - use it when validating a 3rd party api (not your code)