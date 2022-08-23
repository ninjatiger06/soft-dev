"""
    Description: This program is a simple example of a while loop.
    Author: Mr. Bloom
    Date: Fall 2019
"""

import random

def insults():
    """
    Purpose: randomly generate an insult because the user seemingly can't read
    Parameters: none
    Returns: none
    """
    insultList = ["NO, please type u or d!", "You can read...right?",
                  "You seem to be quite unintellectual.", "Try again, dummy"]
    insult = random.choice(insultList)
    print(insult)


def main():
    level = 10                                     # player starts at level 10
    print("........... (%d)" % level)

    while level > 0:
        choice = str(input("char (u/d): "))
        if choice == "u":                       # user selected UP so level up
            level = level + 1
            print("........... (%d) level UP" % level)
        elif choice == "d":                     # user selected DOWN so level down
            level = level - 1
            print("........... (%d) level down" % level)
        else:
            insults()

    print("G A M E  O V E R")


main()
