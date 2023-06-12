#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    m = []
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    for i in my_list:
        m.append(i)
    m.insert(idx, element)
    m.remove(idx + 1)
    return m
