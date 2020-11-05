""" This program does something

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-11-18
"""
import quadratic_sorts as qs
import list_generator as lg


def get_length():
    while True:
        try:
            length = int(input("Please enter the length of input lists: "))
            break
        except ValueError:
            print("That is not a valid input. Please try again.")
    return length


def sort_tester(sort_name, sort_type, a_list, b_list, c_list):
    print("Using %s sort:" % sort_name)
    print("%32s %s %s" % ("# of outer loops", "# of inner loops", "# of swaps"))
    print("Best-case\t\t%-16i %-16i %i" % sort_type(a_list))
    print("Worst-case\t\t%-16i %-16i %i" % sort_type(b_list))
    print("Randomized-case\t%-16i %-16i %i" % sort_type(c_list))
    print()


def main():
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
