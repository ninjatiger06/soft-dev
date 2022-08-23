"""
    Description: This program requests the speed limit and clocked speed of a
                 driver and determines whether the driver should be issued and
                 fined
    Author: Jonas Pfefferman '24
    Date: 10/9/20
"""

def main():

    # Getting the speed limit and driver's speed from user
    speedLimit = int(input("Enter speed limit: "))
    speed = int(input("Enter clocked speed: "))

    # Variable for how much over the speed limit the driver is going
    speedDiff = speed - speedLimit

    if speedDiff>0: # If statement for whether or not the driver's speeding
        print("Driver is speeding! Clocked at %imph over the limit." % (speedDiff))

        # If statement's to give a warning or fines and their amount
        if 1<=speedDiff<=9:
            print("Issue a warning.")

        elif 10<=speedDiff<=19:
            print("Issue a ticket with a $50 fine.")

        elif 20<=speedDiff<=29:
            print("Issue a ticket with a $75 fine.")

        else:
            print("Issue a ticket with a $100 fine.")

    else: # For if the driver is not speeding
        print("Driver's speed is within legal limit.")



main()
