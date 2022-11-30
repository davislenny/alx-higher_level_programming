#!/usr/bin/python3
def islower(c):
    for case in range(ord('a'), ord('z')):
        if ord(c) == case:
            return True

        else:
            return False


def uppercase(str):
    for c in str:
        if islower(c):
            print("{:c}".format(ord(c) - 32), end="")

        else:
            print("")
