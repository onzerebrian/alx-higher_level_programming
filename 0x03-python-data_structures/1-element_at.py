#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    i = 0
    for m in my_list:
        if i == idx:
            return m
        i += 1
