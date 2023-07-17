#!/usr/bin/python3
"""
This module contains one function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r') as f:
        text = ""
        l = -1
        while l != 0:
            line = f.readline()
            l = len(line)
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as f:
        f.write(text)
