# oop basics
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.eye_color = "blue"    

    # setter method 
    def set_first_name(self, first_name):
        self.first_name = first_name; 
    
    def __str__(self):
        return f"<< {self.first_name} {self.last_name} >> " 

# __str__ , __init__ are called magic method or dunder method

eric = Person("Eric", "Bronson")
eric.set_first_name("Eric Joshua")
print(eric)

# Inheritance
# all user define class in python extends object class

class Vehicle:
    def __init__(self, type, number_of_wheels):
        self.type = type
        self.number_of_wheels = number_of_wheels
        self.color = "red"
        pass

    def set_color(self, color):
        self.color = color
    
    def __str__(self):
        return f" TYPE: {self.type} COLOR: {self.color} NUMBER OF WHEELS: {self.number_of_wheels}"
    
    
class FourWheel(Vehicle):
    def __init__(self, type, number_of_wheels, hood, trunk):
        super().__init__(type, number_of_wheels)
        self.hood = hood
        self.trunk = trunk

    def __str__(self):
        return f"TYPE: {self.type} COLOR: {self.color} NUMBER OF WHEELS: {self.number_of_wheels} HOOD: {self.hood} TRUNK:{self.trunk}"

class TwoWheel(Vehicle):
    def __init__(self, type, number_of_wheels, handle_bar, chassis):
       super().__init__(type, number_of_wheels) 
       self.handle_bar = handle_bar
       self.chassis = chassis

    def __str__(self):
        return f"TYPE: {self.type} COLOR: {self.color} NUMBER OF WHEELS: {self.number_of_wheels} Handler Bars: {self.handle_bar} Chassis:{self.chassis}"
    
    
car = FourWheel("Car", 4, True, False)
car.set_color("Blue")
print(car)

motorcylce = TwoWheel("MotorCycle", 2, "Ape", "Underbone")
print(motorcylce)


print(issubclass(Vehicle, object))
print(issubclass(FourWheel, Vehicle))

print(Vehicle.__base__)   # base class is object class
print(FourWheel.__base__) # base class is Vehicle class


