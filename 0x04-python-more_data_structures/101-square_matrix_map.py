#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda elem: list(map(lambda num: num**2, elem)), matrix))
