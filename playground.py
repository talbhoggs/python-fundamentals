# data type
# number
my_num = 12
# float
my_num_flt = 123.3
# boolean
my_bool = True
# string
my_str = "this is my string"
my_str_interpolation = f"The float value {my_num_flt}"

# list
my_list = ["Charles","Amper"]
my_list.append("Austria")

for name in my_list:
    print(f"Name -> {name}")

my_tup = ("Joy","Amper")

my_set = {"Charles","Joy","Joy"}
for set_name in my_set:
    print(f"Set name: {set_name}")

# tuple
# set
# dic

# error handling
# comprehention



# class

class Vehicle():

    def __init__(self, type:str, manufacturer:str, no_of_wheels:int):
        self.type = type
        self.manufacturer = manufacturer
        self.no_of_wheels = no_of_wheels

    def __str__(self):
        return f"Type: {self.type} Manu: {self.manufacturer} #wheels: {self.no_of_wheels}"

class MortorCycle(Vehicle):
    def __init__(self, type:str, manufacturer:str, no_of_wheels:int = 2):
        super().__init__(type, manufacturer, no_of_wheels)

class Car(Vehicle):
    def __init__(self, type:str, manufacturer:str, no_of_wheels:int = 4):
        super().__init__(type, manufacturer, no_of_wheels)


rusi = MortorCycle("Regular", "Rusi")
print(rusi)

raze = Car("Raze", "Toyota")
print(raze)

# oop







# data type
my_int = 23
my_dec = 12.3
my_string = f"string"



# number,
# float
# boolean
# string
# list
# tuple
# set
# dic
# error handling
# comprehention
# class
# oop