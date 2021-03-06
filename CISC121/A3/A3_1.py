""" This program does something

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-11-18
"""


def get_bound():
    """This function gets the lower and upper bounds of the guessed
    number while ensuring formatting is correct.
    """
    while True:
        try:
            lower = int(input("Please enter the lower bound: "))
            upper = int(input("Please enter the upper bound: "))
            if lower > upper:
                raise ValueError
            break
        except ValueError:
            print("That is not a valid input. Please try again.")
    return lower, upper


def main():
    """ This function implements a binary search algorithm to
    find the guessed number.
    """
    lower_bound, upper_bound = get_bound()

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        greater_than = input("Is the number greater than %i (Y/N)? " % mid)
        if greater_than.lower() == "y" or greater_than.lower() == "yes":
            lower_bound = mid + 1
        elif greater_than.lower() == "n" or greater_than.lower() == "no":
            upper_bound = mid - 1
        else:
            print("That is not a valid input, please try again.")

    print("The number you had in mind is %i." % lower_bound)


main()
