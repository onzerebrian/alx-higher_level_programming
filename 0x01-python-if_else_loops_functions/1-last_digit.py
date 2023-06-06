#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
g = "and is greater than 5"
z = "and is 0"
ll = "and is less than 6 and not 0"
print("Last digit of", end=" ")
if (number % 10 > 5):
    print("{} is {} {}".format(number, number % 10, g))
elif (number % 10 == 0):
    print("{} is {} {}".format(number, number % 10, z))
elif (number < 0):
    print("{} is -{} {}".format(number, (number * -1) % 10, ll))
else:
    print("{} is {} {}".format(number, number % 10, ll))
