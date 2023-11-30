#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    plural_s = 's' if argc != 1 else ''

    print('{} argument{}{}{}'.format(argc, plural_s, '.' if argc == 0 else ':', ''))

    for i in range(argc):
        print('{}: {}'.format(i + 1, argv[i + 1]))
