#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number % 10 > 5:
    print(f"Lst digit of {number} is {number % 10} and is greater than 5\n")
elif number % 10 == 0:
    print(f"Lst digit of {number} is {number % 10} and is 0\n")
else:
    print(f"Lst digit of {number} is {number % 10} and is less than 6 and not 0\n")
