#!/usr/bin/python3
""" This module contains one function """


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
