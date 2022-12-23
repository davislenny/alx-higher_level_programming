#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            div = None
            print("wrong type")
        except ZeroDivisionError:
            div = None
            print("division by 0")
        except IndexError:
            div = None
            print("out of range")
        finally:
            new_list.append(div)
            i += 1
    return new_list
