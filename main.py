name = input("Please enter your name: ")
if name.isascii():
    print(name.upper())
else:
    print("Try again. ")