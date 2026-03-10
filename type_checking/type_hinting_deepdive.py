
from typing import NewType, TypedDict, Any, TypeVar
from dataclasses import dataclass
import random

# Working method that don't have type hint at the output
def create_employee(first_name:str, last_name:str, age:int | None) -> dict: 
    email = f"{first_name}-{last_name}@company.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email
    }


# Solution 1: Dictionary with type
# dict[str, str | int | None ] 
# meaning it will return a dictionary with key that has a type of str value of type str or int or None
def create_employee_v1(first_name:str, last_name:str, age:int | None) -> dict[str, str | int | None ]:
    
    email = f"{first_name}-{last_name}@company.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email
    }

print(create_employee_v1("charles", "austria", age=None))
print(create_employee_v1("Lexie", "austria", age=5))
print(create_employee_v1("Will", "austria", age=7))

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

# Solution 2: Using type
# type User = dict[str, str | int | RGB| None ]  type alias 3.12.xx up
User = dict[str, str | int | RGB | None ]; 

def create_employee_v2(first_name:str, 
                       last_name:str, 
                       age:int | None = None,
                       fav_color: RGB | None = None) -> User :
    
    email = f"{first_name}-{last_name}@company.com"

    str_age = str(age) # age type change to str

    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": str_age, # mypy will not able to detect the age type has change (solution use type dictionary Solution 3)
        "email": email,
        "fav_color": fav_color
    }

# Solution 3: Type Dictionary
# type dictionary allows us to specify the types of each individual key
class UserDict(TypedDict):
    first_name: str
    last_name: str
    email: str
    age: int | None
    fav_color: RGB | None

def create_employee_v3(first_name:str, 
                       last_name:str, 
                       age:int | None = None,
                       fav_color: RGB | None = None) -> UserDict :
    
    email = f"{first_name}-{last_name}@company.com"

    str_age = str(age) # age type change to str

    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": str_age, # mypy now able to detect for mismach types (othe approach solution 3)
        "email": email,
        "fav_color": fav_color
    }