#!/usr/bin/python3
"""
Module for writing an Object to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved to the file.
        filename (str): The name of the file to save JSON representation to.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
