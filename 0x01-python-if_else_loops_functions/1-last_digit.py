#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number % -10
elif number >= 0:
    num = number % 10
if num > 5:
    print(f"Last digit of {num} is greater than {number:d} and is greater than 5")
elif num == 0:
    print(f"Last digit of {num} is {number:d} and is 0")
else:
    print(f"Last digit of {num} is less than {number:d} and is less than 6 not 0")
