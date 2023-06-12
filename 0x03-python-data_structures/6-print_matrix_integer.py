#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for idx, i in enumerate(r):
            print("{:d}".format(i), end="")
            if (idx < len(r) - 1):
                print("{}".format(" "), end="")
        print()
