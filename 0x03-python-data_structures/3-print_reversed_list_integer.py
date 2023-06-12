#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        list_copy = my_list
        list_copy.reverse()
        for i in list_copy:
            print("{:d}".format(i))
