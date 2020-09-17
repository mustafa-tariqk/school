name = input("Please enter your name: ")
if name.isascii():
    print(name.isalpha())
else:
    print("Try again. ")