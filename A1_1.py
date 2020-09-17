running = True
while running:
    name = input("Please enter your name: ")

    if name.isalpha():
        print("Your name in all capital letters is", name.upper())

        redo = input("Would you like to do this again: ")
        if redo == "Yes":
            running = True
        elif redo == "No":
            running = False

    else:
        print("Please try again and enter your name.")
    
    