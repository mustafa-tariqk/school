""" This program measures the components of sorting algorithms
based on 3 lists, a best-case, worst-case and randomized case.

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-11-18
"""
import quadratic_sorts as qs
import list_generator as lg


def get_length():
    """ This function gets the input of the length of the list from
    the user and ensures the input is correct.
    """
    while True:
        try:
            length = int(input("Please enter the length of input lists: "))
            break
        except ValueError:
            print("That is not a valid input. Please try again.")
    return length


def sort_tester(sort_name, sort_type, a_list, b_list, c_list):
    """ This function outputs the score of the sorting algorithms in
    a formatted manner.
    """
    print("Using %s sort:" % sort_name)
    print("%33s |%s |%s" % ("|# of outer loops", "# of inner loops", "# of swaps"))
    print("Best-case\t\t|%-16i |%-16i |%i" % sort_type(a_list))
    print("Worst-case\t\t|%-16i |%-16i |%i" % sort_type(b_list))
    print("Randomized-case\t|%-16i |%-16i |%i" % sort_type(c_list))
    print()


def main():
    """ This function outputs the measurements of each sorting
    algorithms. As well as the lists being used for the measurements.
    """
    length = get_length()
    print()

    best = lg.list_ascending(length)
    worst = lg.list_descending(length)
    rand = lg.list_randomized(length)

    print("Best-case example:", best)
    print("Worse-case example:", worst)
    print("Randomized example:", rand)
    print()

    sort_tester("insertion", qs.insertion, best, worst, rand)
    sort_tester("selection", qs.selection, best, worst, rand)
    sort_tester("bubble", qs.bubble, best, worst, rand)


main()
