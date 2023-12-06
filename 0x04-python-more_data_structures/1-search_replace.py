#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element with another in a new list."""
    new_list = [replace if x == search else x for x in my_list]
    return new_list

#####
