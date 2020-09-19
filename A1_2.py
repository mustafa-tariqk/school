""" This program reads a file and finds how many friends each person has.

Author: Mustafa Tariq
Date:2020-09-30
"""

friendships = [line.strip().split() for line in open("friendship.txt")]
# Converts data in file into a 2D list

friendships_dict = {}  # Creating a dictionary for all friendships in the list.
for friends in friendships:

    if friends[1] in friendships_dict:  # Appends values to dictionary.
        friendships_dict[friends[1]].append(friends[0])

        if friends[0] in friendships_dict:
            friendships_dict[friends[0]].append(friends[1])
        else:  # If a key is not in the dictionary it adds it.
            friendships_dict[friends[0]] = [friends[1]]

    else:  # If a key is not in the dictionary it adds it.
        friendships_dict[friends[1]] = [friends[0]]

        if friends[0] in friendships_dict:
            friendships_dict[friends[0]].append(friends[1])
        else:
            friendships_dict[friends[0]] = [friends[1]]


for name in friendships_dict:  # Looks at name and all of their friends.
    print(name, "has", len(friendships_dict[name]), "friend", end="")

    if len(friendships_dict[name]) != 1:
        print("s", end="")
    print(".") # Above lines make sure grammar is correct.