#!/usr/bin/python3
"""
Module for defining a Student class.
"""


class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list):list strings containing attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return
        {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
