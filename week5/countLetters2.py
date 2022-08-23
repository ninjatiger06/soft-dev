"""
Description: Counts letters from a word inputted by a user but through a
             separate count function.
Author: Jonas Pfefferman '24
Date: 11/12/20
"""
#------------------------------------------------------------------------------#

def count(word, letter):
    letterCount = 0
    for char in word:
        if char == letter:
            letterCount += 1

    return letterCount




#------------------------------------------------------------------------------#
def main():
    word = str(input("Enter word: "))
    letter = str(input("Enter letter: "))
    letterCount = count(word, letter)

    if letterCount == 1:
        print("There is 1 %s in that phrase." % (letter))
    else:
        print("There are %d %s's in that phrase." % (letterCount, letter))



main()
