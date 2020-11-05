""" This program does something

Author: Mustafa Tariq
Student Number: 20212856
Section: 001
Date:2020-11-18
"""
import random


def list_randomized(a_length):
    a_list = []
    for i in range(a_length):
        a_list.append(random.uniform(1, 10))
    return a_list


def list_ascending(a_length):
    a_list = list_randomized(a_length)
    a_list.sort()
    return a_list


def list_descending(a_length):
    a_list = list_randomized(a_length)
    a_list.sort(reverse=True)
    return a_list


if __name__ == "__main__":
    print(list_randomized(10))
    print(list_ascending(10))
    print(list_descending(10))
