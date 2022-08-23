"""
	Description: This program demonstrates print formatting with parallel lists.
	Author: Mr. Bloom
	Date: Fall 2019
"""

def main():

	selectedPlayer = input("Whose stats would you like to see? ")

	# parallel lists
    players = ["Vladimir Radmanovic", "Lou Williams", "Lebron James",
				"Kevin Durant", "Kobe Bryant", "Kevin Garnett"]

    ppg = [0, 11.5, 30.3, 28.5, 30.0, 19.2]         # points per game
    games = [2, 13, 23, 20, 12, 20] 		        # games played

    #print("%20s  %4.1f  %2i" % (players[i], ppg[i], games[i]))

	if selectedPlayer = players[1]:
		print("%20s  %4.1f  %2i" % (players[1], ppg[1], games[1]))

	else:
		print("END OF TEST")


main()
