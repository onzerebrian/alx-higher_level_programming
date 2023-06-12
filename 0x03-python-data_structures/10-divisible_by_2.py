#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ar = []
    for i in my_list:
        if (i % 2 == 0):
            ar.append(True)
        else:
            ar.append(False)
    return (ar)
