# integer
my_int: int = 32
# float
my_float: float = 3.2
# boolean
my_bool: bool = True
# string
my_str: str = "string"
print(type(my_str))
# 4 + 2j
# list
my_list = [1,2,3,4,5]
print(type(my_list))
# tuple
my_tuple = (1,23,1)
print(type(my_tuple))
# set
my_set= {1,2,3,5}
print(type(my_set))
# dic
my_dic = {"key1": 3,"key2":5}
print(type(my_dic))
# type
my_none = None
print(type(my_none))

#
def my_funct() -> None:
    print("Hello!")

my_funct()

def my_func(age:int, name:str) -> None:
    print(f"""{name} {age}""")

my_func(name="Charles",age=44)
my_func(age=44,name="Joy")


# importing
import arthimetic
print(f''' result: {arthimetic.add(3,4)}''')

from mypackage import square
print(f''' square {square(5)}''')


# list
my_list_str = ["charles","Joy","Lexie"]
for name in my_list_str:
    print(f"---> {name}")
print(my_list_str)
my_list_str.append("Will")
print(my_list_str)
my_list_str.pop(1) # remove by index
print(my_list_str)
my_list_str.remove("charles")
print(my_list_str)
my_list_str.clear()
print("clear ==> ", my_list_str)

# range
list_numbers = [value for value in range(11, 20)]
print(list_numbers)

# tuple
my_tuple_str = ("Daddy","Mommy","Grandma","Daddy")
print(len(my_tuple_str))
print(my_tuple_str.count("Daddy"))

# set

# dictionary

person ={"name":"Charles", "age": 28, "city": "Talisay"}
print(person)
# add
person["address"] = "Serenis"
print(person)
# remove
del person["age"]
print(person)
# iterate

# iterate by keys
for key in person:
    print(key)

# iterate by values
for item in person.values():

    print(item)
# iterate by items (key and value)
for key, value in person.items():
    print(f"{key} = {value}")

class Vehicle:
    def __init__(self, brand:str, type:str, no_of_wheels:int, vehicle_drive:str):
        self.brand = brand 
        self.type = type
        self.no_of_wheels = no_of_wheels
        self.vehicle_drive = vehicle_drive
    
    def __str__(self):
        return f"<<<< {self.brand} {self.no_of_wheels} {self.type} {self.vehicle_drive} >>>>"

click = Vehicle("Honda", "Motorcycle", 2, "rwd" )
print(click)
mini_van = Vehicle("Suzuki","Minivan", 4, "rwd")
print(mini_van)