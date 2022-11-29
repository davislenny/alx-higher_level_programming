#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 10):
        if i != j and (i != 8 or j != 9):
            print("{}{}, ".format(i, j), end="")

        elif i == 8 and j == 9:
            print(f"{i}{j}")
