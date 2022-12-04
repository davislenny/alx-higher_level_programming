#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    cpy = my_list.copy()
    cpy.sort()
    return cpy[-1]

# def max_integer(my_list=[]):
    # mx = my_list[0]
    # for i in range(1, len(my_list)):
        # if my_list[i] > mx:
            # mx = my_list[i]
    # return mx
