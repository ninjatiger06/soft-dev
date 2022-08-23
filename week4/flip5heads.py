"""
    Description: This program simulates a coin flip over and over until 5
    'heads' are flipped in a row.
    Author: Mr. Bloom
    Date: Fall 2019
"""

import random

def main():
    coin = ["heads", "tails"]

    countFlips = 0                  # count total number of flips
    numInARow = 0                   # count times heads is flipped consecutively
    while numInARow < 5:
        coinFlip = random.choice(coin)              # flip coin
        countFlips = countFlips + 1                 # update countFlips
        print("%d. %s" % (countFlips, coinFlip))    # print results of flip

        if coinFlip == "heads":                     # keep track of how many in row
            numInARow = numInARow + 1               # update numInARow
        else:
            numInARow = 0                           # tails was flipped! reset

    print("Nice, we got 5-in-a-row!")


main()
