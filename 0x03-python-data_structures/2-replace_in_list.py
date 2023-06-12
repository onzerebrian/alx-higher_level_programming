#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    i = 0
    for m in my_list:
        if i == idx:
            my_list.insert(i, element)
            my_list.remove(i + 1)
            return my_list
        i += 1
