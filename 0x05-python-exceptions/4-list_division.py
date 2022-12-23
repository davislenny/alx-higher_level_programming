#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        div = 0
        try:
            div = my_list[i] / my_list_2[i]
        except (ValueError, TypeError):
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = None
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            new_list.append(div)
        i += 1
    return new_list
