#!/usr/bin/python3
if __name__ == '__main__':
    
a = 1
b = 2

from add_0 import add as add_0_function

result = add_0_function(a, b)
print("{} + {} = {}".format(a, b, result))

