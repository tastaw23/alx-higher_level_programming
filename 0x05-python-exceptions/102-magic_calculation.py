#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise ValueError('Too far')
            result += (a ** b) / i
        except ValueError as ve:
            result += a + b
            break

    return result
###
