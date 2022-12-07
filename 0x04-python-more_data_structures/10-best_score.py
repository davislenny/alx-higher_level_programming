#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        new = sorted(a_dictionary.values())
        for key in a_dictionary.keys():
            if a_dictionary[key] == new[-1]:
                return key
