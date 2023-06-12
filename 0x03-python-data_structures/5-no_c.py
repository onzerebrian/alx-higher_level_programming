#!/usr/bin/python3
def no_c(my_string):
    lt = []
    for m in my_string:
        lt.append(m)
    for i in lt:
        if (i == 'c') or (i == 'C'):
            lt.remove(i)
    my_string = ""
    x = 0
    for i in lt:
        my_string = my_string + i
    return my_string
