def checkIfGameOver(board):
	"""
	check if someone has won, or a draw.
	return “x” if X wins, “o” if O wins, “d” if draw, and None if game not over
	"""
	return None


def computerTurn(board):
	""" find best spot and play it """
	board[5] = "o"
	return


def main():
	""" run one game of tic-tac-toe """

	# print rules of game??
	board = [" "] * 9
	display(board)

	while True:
		userTurn(board)
		display(board)
		result = checkIfGameOver(board)
		if result != None:
			break
		computerTurn(board)
		display(board)
		result = checkIfGameOver(board)
		if result != None:
			break

	# game is over, print results
	if result == "x":
		print("X wins!")
	elif result == "o":
		print("O wins!")
	else:
		print("it’s a draw. . . .")



main()
