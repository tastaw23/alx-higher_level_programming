#!/usr/bin/python3

def magic_string():
    """
    Returns a string "BestSchool" n times the number of the iteration.

    Format: see example
    """
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return "BestSchool" + ", BestSchool" * magic_string.count
###
