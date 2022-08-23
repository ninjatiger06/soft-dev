"""
    Description: This program decides if people can get into a party or not.
    Author: Jonas Pfefferman '24
    Date: 10/8/20
"""

def main():

    # Using input to see who is asking to get in
    guest = str(input("What's your name? "))

    # List of those who are allowed
    guestList = ["Mr. Bloom", "Jonas Pfefferman", "Kenan Begovic", "Sopo Guan",
                "Millan Kumar", "Carlton Schell", "Cesar Tadeo",
                "Andrew Welsbie", "Nathan Xiong"]

    # If statement for whether or not they're on the "yes" List
    if guest in guestList:
        print("You're on the list... welcome to the party.")

    else:
        print("Sorry, you're not on the list.")



main()
