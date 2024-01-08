#!/usr/bin/python3

def lookup(obj):
    """
    Function to return the list of available attributes and methods of an object.

    Args:
    - obj: The object to inspect.

    Returns:
    - A list containing the attributes and methods of the object.
    """
    return dir(obj)

# Example usage
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

