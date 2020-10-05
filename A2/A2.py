""" This program gets inputs, validates inputs
and calculates outputs using fun_math.py.

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-10-14
"""

import fun_math

def valid_input(task):
    """ Common for all functions to check input.
    Use of ValueError as exception type.
    """
    while True: #  Keeps asking for input until valid.
        try:
            task()
            break
        except ValueError:
            print("That is not a valid input, try again.\n")

def task1():
    """ Input and output for task 1.
    """
    base = int(input("Please enter a positive integer: "))
    if base <= 0: #  Checks if integer is positive
        raise ValueError
    print(fun_math.cal_factorial(base), "\n")

def task2():
    """ Input and output for task 2.
    """
    number, length = map(int, input("Please enter a non-negative number and a length spaced: ").split())
    if number < 0 or length <= 0: #  Checks if non-negative and positive.
        raise ValueError
    print(fun_math.list_multiples(number, length), "\n")

def task3():
    """ Input and output for task 3.
    """
    a_list = list(map(int,\
             input("Please enter a list of spaced integers: ")\
             .split())) #  Converts one line of spaced integers into a list.
    print(fun_math.find_max(a_list), "\n")

def main():
    """ Function for exceution of program.
    """
    while True: #  Keeps asking for input until valid.
        task = input("Please choose your task:\n"\
                    "1 – calculate factorial\n"\
                    "2 - generate a list of multiples\n"\
                    "3 – find max number in a list\n"\
                    "4 - exit the program\n")

        #  Excecutes task based on input.
        if task == "1":
            valid_input(task1)
        elif task == "2":
            valid_input(task2)
        elif task == "3":
            valid_input(task3)
        elif task == "4":
            break
        else:
            print("That is not a valid option, try again.\n")

main()