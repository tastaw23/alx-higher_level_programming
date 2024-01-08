#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class representing the base geometry.
    """

    def area(self):
        """
        Public instance method to calculate the area.
        Raises:
        - Exception: with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

# Example usage
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

