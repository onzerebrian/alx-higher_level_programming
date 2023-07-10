#!/usr/bin/python3
"""
This module contains one class MyInt
"""


class MyInt(int):
    """ class MyInt """

    def __eq__(self, other):
        """ returns true if equal """
        return super().__int__() != other

    def __ne__(self, other):
        """ returns true if not equal """
        return super().__int__() == other
