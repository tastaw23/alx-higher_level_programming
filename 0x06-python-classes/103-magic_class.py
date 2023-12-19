#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * 3.141592653589793

    def circumference(self):
        return 2 * 3.141592653589793 * self.__radius
###
