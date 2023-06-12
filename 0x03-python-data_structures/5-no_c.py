#!/usr/bin/python3
def no_c(my_string):
    my_string2 = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            my_string2 = my_string2 + i
    return my_string2
