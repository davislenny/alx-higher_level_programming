#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for elem in rows:
            if elem is not rows[len(rows) - 1]:
                print("{:d} ".format(elem), end="")
            else:
                print("{:d}".formar(elem), end="")
        print()
