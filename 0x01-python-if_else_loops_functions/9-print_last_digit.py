#!/usr/bin/python3
def print_last_digit(number):
#    num = abs(number) % 10
    num = number % 10
    if number < 0:
        num = (number * -1) % 10

    print("{}".format(num), end="")
    return num
