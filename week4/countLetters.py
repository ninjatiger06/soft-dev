"""
    Description: This program goes through a phrase entered by the user, one
    character at a time, and counts up how many of a chosen letter are in the phrase.
    Author: Mr. Bloom
    Date: Fall 2019
"""

#------------------------------------------------------------------------------#
def printResults(count, letter):
    """ print out the results with correct grammar """
    if count == 1:
        print("There is 1 %s in that phrase." % letter)
    else:
        print("There are %i %s's in that phrase." % (count, letter))

#------------------------------------------------------------------------------#
def count(char, text):
    """ count up how many of letter are in text """
    letterCount = 0
    for ch in text:             # where ch is the current letter in the phrase
        if ch == char:          # where char is the letter we're counting (looking for)
            letterCount += 1
    return letterCount

#------------------------------------------------------------------------------#
def main():
    phrase = str(input("phrase: "))
    letter = str(input("letter: "))
    n = count(letter, phrase)
    printResults(n, letter)


main()
