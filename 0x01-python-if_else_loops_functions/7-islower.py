#!/usr/bin/python3
def islower(c):
    for case in range(ord('a'), ord('z') + 1):
        if ord(c) == case:
            return True

        else:
            return False
