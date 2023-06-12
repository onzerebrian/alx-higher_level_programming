#!/usr/bin/python3
def no_c(my_string):
#convert the string to list
    lt = []
    for m in my_string:
        lt.append(m)
#remove the occurace of c or C in the list
    x = 0
    for i in lt:
        if (i == 'c') or (i == 'C'):
            lt.remove(i)
    x += 1
#convert the list to string
    my_string = ""
    x = 0
    for i in lt:
        my_string = my_string + i
    

#return the resultant list
    return my_string
