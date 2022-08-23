"""Description: This program takes a word and removes a diffrent letter each
                time until there are no more to remove
    Author: Jonas Pfefferman '24
    Date: 9/17/20
"""

def main():

    #Getting word variable
    wordvar = str(input("Input WORD: "))

    #printing Description
    print("Here's that word with all possible single-letter deletions:")

    #for loop for printing
    for i in range(len(wordvar)):
        print("%i: %s%s" % (i, wordvar[:i], wordvar[i+1:]))

main()