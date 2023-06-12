#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    space=" "
    for i in matrix:
        for j in i:
            print("{:d}".format(j),end="")
            if (j != i[-1]):
                print("{}".format(space),end="")
        print()
