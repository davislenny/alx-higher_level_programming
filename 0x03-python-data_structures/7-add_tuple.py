#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    a1 = tuple_a[0] if a > 0 else 0
    a2 = tuple_a[1] if a > 1 else 0
    b1 = tuple_b[0] if b > 0 else 0
    b2 = tuple_b[1] if b > 1 else 0
    sum = (a1 + b1, a2 + b2)
        
    return sum
