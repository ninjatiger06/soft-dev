"""
Description: This program has a function named getChoice that asks a user to
             enter either "rock", "paper", or "scissors" and then returns the
             string value entered by the user but only if it's valid.
Author: Jonas Pfefferman '24
Date: 11/3/20
"""

#------------------------------------------------------------------------------#
"""
Purpose: Validates user-input
Parameters: Takes user-input (string) to see whether or not it is acceptable
            input.
Returns: Returns the validated user-input (string)
"""

def getChoice():

    while True: # Loop to continue to ask for user-input
        userInput = str(input("Pick one of rock, paper, or scissors: "))

        # Breaks loop if user-input matches one of the terms
        if userInput == "rock" or userInput == "paper" or userInput == "scissors":
            move = userInput
            return move

        else: # Tells the user that their choice isn't valid
            print("Whoops! %s isn't a valid choice. Try again." % (userInput))


#------------------------------------------------------------------------------#
def main():
    move = getChoice()
    print("getChoice returned %s" % (move)) # Displays what getChoice returned



main()
