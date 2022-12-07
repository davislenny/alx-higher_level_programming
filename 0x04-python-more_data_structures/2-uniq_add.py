#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    a = sorted(set(my_list))
    for i in range(len(a)):
        sum += a[i]
    return sum
