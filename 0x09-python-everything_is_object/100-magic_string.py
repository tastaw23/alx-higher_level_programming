#!/usr/bin/python3

def magic_string():
    """
    Returns a string "BestSchool" n times the number of the iteration.

    Format: see example
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
###
