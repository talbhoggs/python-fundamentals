######################
# Names and objects
######################

# create an object and bind it 
# not the same as java
x = 10 

# Python everthing is an object
# objects in python has
# the followng:

s='Hello'
print(type(s)) # type
print(s) # value
print(id(s)) # id

######################
# Mutabiility
######################

# immutable objects
# int, string, float, and tuple

# mutable objects
# list, dic, and set 

x = ["work"]
y=x
y[0] = "leisure"
print(x) # leisure
print(y) # leisure

######################
# Python Containers Store Reference
######################


# int is an immutable object

z = 10
a = z
a += 1
print(f"x {a}") # 11
print(f"y {z}") # 10

# java
# value types (primitive) and reference types

# python
# mutable objects and immutable objects


# If python does not have primitives
# How can python handle large array of numbers
# answer: Use of Numpy (package written in c++) 

######################
# Functions are just another objects
######################

# you can store it into a list
# past it to another function
# return
# assign it to a name

def my_funct(): return 2+2

g = my_funct # assign function to another name

print(g()) # g is another name for the function my_funct
print(my_funct())

# this way decorator works and callbacks works

######################
# Scope and namespaces
######################

# Python resolves name using LEGB (Local Enclosing Global BuiltIn)

# global
global_name = 'Charles'
fname = 'Amper'

def change():
    global global_name
    global_name = "Avon"
    fname = 'Austria'

change()
print(global_name) #Avon
print(fname) #Amper


# nonlocal
nonlocal_name = 'Willy'
def main():

    nonlocal_name = 'Charles'

    def change():
        nonlocal nonlocal_name 
        nonlocal_name = "Avon"

    change()
    print(nonlocal_name) #Avon

main()
print("--> " +nonlocal_name) 

######################
# Iterables and Iterators
######################

# loops in python does not loop
# it ask the object for iterator

greeting = "Hello"

for s in greeting:
    print(s, end=",")

# under the hood
print("\nUnder the hood")
it = iter(greeting)

print(next(it), end=",")
print(next(it), end=",")
print(next(it), end=",")
print(next(it), end=",")
print(next(it), end=",")


# Iterable objects List, string, files, generators, 
# understanding this makes generators, comprehension, lazy evaluation and streaming data
# easy to understand

######################
# Imports are just objects too
######################

import math

# When you import a module, python load the module, creates a module object
# and binds the name math to it.

# Module are just a namespace object, a dictionary of names

print(math.pi)
print(math.sin)

my_dic = {"name": "charles", "age": "34"}
print(my_dic["age"])


# # #

# String
# since string are mutable
# it looks like it follows the 
# primitive concept but it is not
my_str1 = "Charles"
my_str2 = my_str1

my_str2 += "Amper" 
# mutation does not happen coz string is a immutable object
# this will create a new instance. 

print(my_str1)
print(my_str2)


# List
# List is a mutable object
#
my_lst = ["charles"]
my_lst1 = my_lst

my_lst1[0] = "Testing Amper" # mutate
# mutation happen since the data type is a list
# it will now point to the same object

print(my_lst)
print(my_lst1)
