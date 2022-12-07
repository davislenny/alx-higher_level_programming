#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.items())
    for key, item in new:
        print(f"{key}: {item}")
