#!/usr/bin/python3
"""
This module contains one function
"""


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename) as f:
        c = 0
        for line in f:
            c += 1
    return c
