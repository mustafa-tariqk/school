""" This program outputs someone's first name in all capital letters.

Author: Mustafa Tariq
Date:2020-09-30
"""

running = True
while running:  # Keeps running file until user choses to exit.
    name = input("Please enter your first name: ")

    if name.isalpha():  # Checks if user input only contains a-z
        print("Your name in all capital letters is %s." %name.upper())

        redo = input("Would you like to do this again: ")
        if redo != "Yes":  # Exits the program if input is not Yes.
            running = False
            
    else:  # Asks user to input properly.
        print("Please try again and enter your name.")