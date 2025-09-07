from datetime import datetime, date, timedelta
from random import random, randrange, choice

# date class
now = datetime.now()
plus_10_days = timedelta(days=10)

print(now + plus_10_days)
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
print(date.today())

# random
print(random())
print(randrange(1, 4))

fruits = ["apple", "orange", "mange"]
fruit = fruits[randrange(0, len(fruits))]
print(fruit)

chosen_fruit = choice(fruits)
print(chosen_fruit)


# Path
# Reading files
# Writing files
from pathlib import Path

# read
file = Path("read.txt")
text = file.read_text()
print(text)

# write
file.write_text("Charles is good\nLexie \n")
text = file.read_text()
print(text)

# using with in reading and writing files
with Path.open("read.txt", "r") as read_txt:
    print(f"---> {read_txt.read()}")

with Path.open("read.txt", "w") as write_txt:
    content = write_txt.write("Yes Yes Yes")