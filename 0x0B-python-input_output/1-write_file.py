#!/usr/bin/python3
"""
Module for writing a string to a text file (UTF8) and returning the number
of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)

