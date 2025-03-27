#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program checks if the user guesses the random number correctly
number = int(input("Enter an integer: "))

if number > 0:
    print(f"{number} is a positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is just zero!")
