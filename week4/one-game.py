"""
Description: This program has a function named getChoice that asks a user to
             enter either "rock", "paper", or "scissors" and then returns the
             string value entered by the user but only if it's valid. It will
             also calculate the winner of the game
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

            return userInput

        else: # Tells the user that their choice isn't valid
            print("Whoops! %s isn't a valid choice. Try again." % (userInput))


#------------------------------------------------------------------------------#
"""
Purpose: Takes the moves of players 1 and 2 and checks who won.
Parameters: Takes player 1's move (string) and player 2's move (string)
Returns: Returns a value that describes who won (integer)
"""

def calculateWinner(player1, player2):
    if player1 == player2: # Players 1 and 2 both have the same move (a tie)
      playerWin = 0

    elif player1 == "scissors" and player2 == "paper": # Player 1 wins
        palyerWin = 1

    elif player1 == "paper" and player2 == "rock": # Player 1 wins
        playerWin = 1

    elif player1 == "rock" and player2 == "paper": # Player 1 wins
        palyerWin = 1

    # Because all tie and player 1 win options are all listed, the only
    # thing left is player 2 winning
    else:
        playerWin = 2

    return playerWin


#------------------------------------------------------------------------------#
def main():
    print("Player 1:")
    player1 = getChoice() # Takes and validates player 1's move
    print("Player 2:")
    player2 = getChoice() # Takes and validates player 2's move

    winner = calculateWinner(player1, player2) # Calls function to see who won

    # Displays who picked what
    print("Player 1 picked %s and Player 2 picked %s" % (player1, player2))
    print("calculateWinner returned %i" % (winner)) # Displays numerical results

    # Adds to just the numerical results
    if winner == 0:
      print("A Tie.")

    elif winner == 1:
      print("Player 1 wins!")

    elif winner == 2:
      print("Player 2 wins!")




main()
