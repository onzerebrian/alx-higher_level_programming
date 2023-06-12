#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list[0] == None:
        return None
    max_va = my_list[0]
    for i in my_list:
        if max_va < i:
            max_va = i
    return max_va
