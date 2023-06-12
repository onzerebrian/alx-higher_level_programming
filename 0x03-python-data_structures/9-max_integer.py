#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_va = my_list[0]
    for i in my_list:
        if max_va < i:
            max_va = i
    return max_va
