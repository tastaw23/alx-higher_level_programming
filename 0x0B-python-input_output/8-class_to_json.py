#!/usr/bin/python3
"""
Module for returning the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: Dictionary representation of the object.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Convert attributes to dictionary with simple data structures
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[key] = value
        else:
            attributes[key] = str(value)

    return attributes
