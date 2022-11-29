#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
if number > 0:
    num = number % 10
else:
    num = (number % -10)
if num > 5:
    print(f"{str} {number:d} is {num:d} and is greater than 5")
elif num == 0:
    print(f"{str} {number:d} is {num:d} and is 0")
elif num < 6 and num != 0:
    print(f"{str} {number:d} is {num:d} and is less than 6 and not 0")
