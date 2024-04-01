#!/usr/bin/python3
def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    if size == 0:
        return None
    elif size == 1:
        return list_of_integers[0]

    left, right = 0, size - 1
    while left < right:
        mid = left + (right - left) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
