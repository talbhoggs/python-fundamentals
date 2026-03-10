

from typing import Any, TypeVar, NewType
from dataclasses import dataclass
import random
# Solution 3
# Data class

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

@dataclass
class UserDataClass():
    first_name: str
    last_name: str
    email: str
    age: int | None = None
    fav_color: RGB | None = None


def create_employee(first_name:str, 
                       last_name:str, 
                       age:int | None = None,
                       fav_color: RGB | None = None) -> UserDataClass:
    
    email = f"{first_name}-{last_name}@company.com"

  # str_age = str(age) # age type change to str

    return UserDataClass (
        first_name= first_name,
        last_name=last_name,
        age=age, 
      # "age": str_age, # mypy now able to detect for mismach types
               # mypy now able to detect for mismach types 
        email=email,
        fav_color=fav_color
    )

# Generics
def random_choice(items:list[UserDataClass]) -> UserDataClass:
    return random.choice(items)

user1 = create_employee("charles", "austria", 44, fav_color=RGB((23,23,32)))
user2 = create_employee("joy", "austria", 44, fav_color=RGB((23,23,32)))

users = [user1, user2]

random_user = random_choice(users)

emails = [user.email for user in users]
random_email = random_choice(emails) # mypy detects invalid input type (Input is UserDataClass not emails)
print(random_email)


# Solution 1: Using Any
def random_choice_ver2(items:list[Any]) -> Any:
    return random.choice(items)

random_user = random_choice_ver2(users)
random_email = random_choice_ver2(emails) # No mypy issue. Downside: python no able to determine what type of object (no autocomplete)
print(random_email)

# Solution 2: Using TypeVar
T = TypeVar("T")
def random_choice_ver4(items:list[T]) -> T:
    return random.choice(items)

emails_4 = [user.email for user in users]
print(emails_4)
random_email_4 = random_choice_ver4(emails_4) # No issue, python is able to detect the correct classs.
print(random_email_4)


# Solution 3: 
# python 3.12 no need to define TypeVar is example below 
#
# def random_choice_ver4[T](items:list[T]) -> T:
#    return random.choice(items)

# Usig type hints with 3rd party library
# most of the cases don't add typehint you need to install stubs to enable type hints

# Best practices
# Input must be more generic (allow multiple inputs)
# Output be more specific (allow specific output)