""" This program finds all the hopping paths from 0 to n.

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-12-2
"""


def hopping_game(n):
    """This function recursively finds
    all the paths hopping from 0 to n.
    """
    if n == 0:  # Base cases.
        return ['0']
    elif n == 1:
        return ['0-1']
    elif n == 2:
        return ['0-1-2', '0-2']
    else:
        one_square_hops = hopping_game(n - 1)  # Finds all hop paths.
        two_square_hops = hopping_game(n - 2)

        for i in range(len(one_square_hops)):  # Proper formatting.
            one_square_hops[i] += ("-" + str(n))
        for j in range(len(two_square_hops)):
            two_square_hops[j] += ("-" + str(n))

        return one_square_hops + two_square_hops


if __name__ == "__main__":
    # All cases match correct output.
    print(hopping_game(1))
    print(hopping_game(2))
    print(hopping_game(3))
    print(hopping_game(4))

