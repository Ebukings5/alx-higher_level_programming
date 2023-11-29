#!/usr/bin/python3
def fizzbuzz():
    for chuks in range(1, 101):
        if chuks % 3 == 0 and chuks % 5 == 0:
            print("FizzBuzz", end=" ")
        elif chuks % 3 == 0:
            print("Fizz", end=" ")
        elif chuks % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(chuks, end=" ")
