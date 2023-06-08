#!/usr/bin/python3
from sys import argv
def arguments():
    arg_string = "arguments"
    a = "."
    length = len(argv) - 1
    if (length == 1):
        arg_string = "argument"
    if (length - 1 >= 0):
        a = ":"

    print("{} {}{}".format(length, arg_string, c_or_d,))

    for index, arg in enumerate(argv):
        if (index > 0):
            print("{}: {}".format(index, arg))

if __name__ == "__main__":
    arguments()
