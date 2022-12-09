#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    a = sum([num[0] * num[1] for num in my_list])
    b = sum([num[1] for num in my_list])
    return a/b
