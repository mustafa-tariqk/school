""" This program contains a function that uses binary search
    to find the first occurrence of a character in a string.

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-12-2
"""


def find_first_b(string, low, high, character):
    """ This function finds the first occurrence
        of a character in a string.
    """
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or character > string[mid - 1]) and string[mid] == character:
            return mid  # Only returns if its the first occurrence.
        elif character > string[mid]:  # Looks for element in right side of string.
            return find_first_b(string, mid + 1, high, character)
        else:  # Looks for element in left side of string.
            return find_first_b(string, low, mid - 1, character)

    return None  # If element not in string.


if __name__ == "__main__":
    # Test for multiple "b"s.
    print(find_first_b("aaaabbb", 0, len("aaaabbb") - 1, "b"))

    # Test for no "b".
    print(find_first_b("aaaaaaaa", 0, len("aaaaaaaa") - 1, "b"))

    # Test for all "bs".
    print(find_first_b("bbb", 0, len("bbb") - 1, "b"))

    # Test for single "b".
    print(find_first_b("aaaaaab", 0, len("aaaaaab") - 1, "b"))
