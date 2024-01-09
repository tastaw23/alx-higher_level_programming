#!/usr/bin/python3
"""
Module for creating an Object from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of file containing the JSON representation.

    Returns:
        object: The Python data structure represented by the JSON in the file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
