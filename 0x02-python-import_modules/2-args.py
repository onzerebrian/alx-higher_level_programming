#!/usr/bin/python3
from sys import argv

def arguments():
    if len(argv) == 1:
        print("{} {}".format(len(argv)-1, "arguments."))
        return

    if len(argv) == 2:
        print("{} {}".format(len(argv) - 1, "argument:"))
    elif len(argv) > 2:
        print("{} {}".format(len(argv) - 1, "arguments:"))

    no_of_argv = len(argv) - 1
    i = 1
    while i <= no_of_argv:
        print("{}: {}".format(i,argv[i]))
        i += 1
arguments()
