""" This program contains function that checks if
a number appears an equal amount of times in two lists.

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-10-21
"""


def equal_occurence(list_a, list_b, target):
    """ Checks if an element is repeated the 
        same number of times in 2 lists.
    """
    if not list_a or not list_b:  # Checks if lists are empty.
        return False
    elif list_a.count(target) == list_b.count(target):
        return True
    else:
        return False


if __name__ == "__main__":
    #  Tests if it will see a float and int as the same.
    print(equal_occurence([1, 2, 3], [1.0, 2.0, 3.0], 3))
    print(equal_occurence([1, 2, 3], [1.0, 2.0, 3.0], 3.0))

    #  Tests if null lists are accepted.
    print(equal_occurence([], [1.0, 2.0, 3.0], 3.0))
    print(equal_occurence([1, 2, 3], [], 3.0))

    #  Tests if target not in lists.
    print(equal_occurence([1, 2, 3], [1.0, 2.0, 3.0], 4))

    #  Tests if taget does not show up equal times.
    print(equal_occurence([1, 2, 3, 3], [1.0, 2.0, 3.0], 3))
