# List

# Tuples

# immutable list
countries = ("China", "India")
print(countries)

# mutable list
animals = ["pig", "cat", "dog"]

# Adding removing values in a list
animals.append("horse")
print(animals)

animals.remove("cat") # remove using value
print(animals)

animals.pop()  # remove the last object
print(animals)

animals.pop(0) # remove using index
print(animals)

# sorting list and calling len
fruits = ["banana", "apple", "durian"]

fruits.sort()
print(f"sort {fruits}")

fruits.reverse()
print(f"reverse {fruits}")

length = len(fruits)
print(length)

# iterating a list 
for fruit in fruits:
    print(f"I love {fruit}")

# range
list_numbers = []
for value in range(1, 10):
    list_numbers.append(value)
print(list_numbers)

# max, min, sum
print(f"max {max(list_numbers)}")
print(f"min {min(list_numbers)}")
print(f"sum {sum(list_numbers)}")

# List comprehension
list_numbers = [value for value in range(11, 20)]
print(list_numbers)