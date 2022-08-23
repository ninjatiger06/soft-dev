"""
    Description: This program takes a number of stones as input and returns True
                 if the game is over (number of stones is 0). Based on 21 stones
    Author: Jonas Pfefferman '24
    Date: 11/18/20
"""

#------------------------------------------------------------------------------#
def isGameOver(stones):
    """
    Purpose: checks a inputted number of stones to see if the game is over
    Parameters: stones, the current number of stones in the pile (int)
    Return Val: True if 0 stones remain; false if stones remain
    """
    if stones == 0:
        return True
    else:
        return False


#------------------------------------------------------------------------------#
def main():
    stones = 3
    gameOver = isGameOver(stones)
    print("isGameOver(%i)? %s" % (stones, gameOver))
    stones = 0
    gameOver = isGameOver(stones)
    print("isGameOver(%i)? %s" % (stones, gameOver))
    stones = 9
    gameOver = isGameOver(stones)
    print("isGameOver(%i)? %s" % (stones, gameOver))



main()
#------------------------------------------------------------------------------#
