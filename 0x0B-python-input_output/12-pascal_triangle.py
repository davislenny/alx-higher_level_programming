#!/usr/bin/python3
"""
The '12-pascal_triangle' module
Returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """function definition"""
    if n <= 0:
        return []
    Triangle = [[1]]
    for rows in range(n - 1):
        List = [1]
        for i in range(rows):
            List.append(Triangle[-1][i] + Triangle[-1][i+1])
        List.append(1)
        Triangle.append(List)
    return Triangle
