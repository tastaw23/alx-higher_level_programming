#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Function to check if the object is an instance of, or if it is an instance of
    a class that inherited from, the specified class.

    Args:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)

# Example usage
if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))

