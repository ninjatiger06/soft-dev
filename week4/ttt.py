"""
    Description: This program allows the user to play multiple rounds of
    tic-tac-toe against the computer (has NOT been fully implemented yet)
    Author: Mr. Bloom/Jonas Pfefferman '24
    Date: 10/20/20
"""

def draw(board):
    """  Displays a simple 3x3 board to the screen  """
    print(" %s | %s | %s" % (board[0], board[1], board[2]))
    print("-----------")
    print(" %s | %s | %s" % (board[3], board[4], board[5]))
    print("-----------")
    print(" %s | %s | %s" % (board[6], board[7], board[8]))


def main():
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    draw(board)

    location = int(input("  0-8: "))
    board[location] = "x"
    draw(board)

    location = int(input("  0-8: "))
    board[location] = "o"
    draw(board)


main()
