"""
Description: This program has a function named getChoice that asks a user to
             enter either "rock", "paper", or "scissors" and then returns the
             string value entered by the user but only if it's valid. It will
             also calculate the winner of the game. This also asks the player
             their name and plays to the number of wins they set.
Author: Jonas Pfefferman '24
Date: 11/3/20
"""
import random

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
        playerWin = 1

    elif player1 == "paper" and player2 == "rock": # Player 1 wins
        playerWin = 1

    elif player1 == "rock" and player2 == "paper": # Player 1 wins
        playerWin = 1

    # Because all tie and player 1 win options are all listed, the only
    # thing left is player 2 winning
    else:
        playerWin = 2

    return playerWin


#------------------------------------------------------------------------------#
"""
Purpose: Prints out a scorecard of the wins after each round.
Parameters: Takes the user's wins (integer), computer's wins (integer), and the
            the user's name (string)
Returns: None
"""

def printScores(name, userWins, compWins): #Prints scorecard
    print("-----------------------------------------")
    print("%s: %i\t Computer: %i" % (name, userWins, compWins)) #Displays results
    print("-----------------------------------------")


#------------------------------------------------------------------------------#
def main():
    name = str(input("What is your name? ")) # Asks for name to put on scorecard
    # Asks how many wins
    playTo = int(input("How many wins should we play until? "))
    print("Let's see who can win 2 games first! Good luck.")

    # Accumulators to count what to put on the scorecard and when to end
    totalGames = 0
    userWins = 0
    compWins = 0

    # Both computer and player wins have to be less than the playTo amount
    while userWins < playTo and compWins < playTo:
        print("\nNext round:")
        player1 = getChoice() # Asks for player's move
        possibleMoves = ["rock", "paper", "scissors"]
        player2 = random.choice(possibleMoves) # Randomly selects move

        winner = calculateWinner(player1, player2) # Calls function to see who won

        # Displays who picked what
        print("Player 1 picked %s and Player 2 picked %s" % (player1, player2))

        # Replaces the numerical win results with an easy to understand phrase
        if winner == 0:
          print("... A Tie.")
          totalGames += 1

        elif winner == 1:
          print("... %s wins!" % (name))
          totalGames += 1
          userWins += 1

        elif winner == 2:
          print("... Computer wins!")
          totalGames += 1
          compWins += 1

        printScores(name, userWins, compWins) # Calls function to display scorecard

    # Displays the number of wins for the player out of the number of games
    if userWins > compWins:
        print("%s beat Computer:" % (name))
        print("... won %i games in %i rounds of rock-paper-scissors." % (userWins,
                totalGames))

    # Displays the number of wins for the computer out of the number of games
    else:
        print("Computer beat %s:" % (name))
        print("... won %i games in %i rounds of rock-paper-scissors." % (compWins,
                totalGames))




main()
