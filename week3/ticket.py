"""
    Description: This program will asses whether or not someone is going over
                 the speed limit and give them a ticket whose amount is based
                 off of how much over the speed limit they were going.
    Author: Jonas Pfefferman '24
    Date: 10/7/20
"""

def main():

    # Defining variables from user input
    speedLimit = int(input("What is the speed limit in mph? "))
    speed = int(input("How fast were you going in mph? "))

    # If statement for whether or not the you were speeding
    speedDiff = speed - speedLimit
    if speedDiff >= 5:
        ticketCost = 2 * speedDiff
        # For if the speed limit is greater than or equal to 65
        if speedLimit >= 65:
            ticketCost += 33
            print("\nYou were speeding and your fine is $%i" % (ticketCost))
        else:
            ticketCost =+ 25
            print("\nYou were speeding and your fine is $%i" % (ticketCost))

    # For if they were not going more than 5mph above the speed limit
    else:
        print("\nYou were not speeding. Safe driving FTW!")



main()
