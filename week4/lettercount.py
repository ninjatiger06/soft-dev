"""
    Description: This program counts the number of a certain letter in an
                 inputted string.
    Author: Jonas Pfefferman '24
    Date: 10/5/20
"""

def main():

    phrase = str(input("phrase: "))
    letter = str(input("letter: "))

    letterCount = 0
    for char in phrase:
        if char == letter:
            letterCount += 1

    if letterCount == 1:
        print("There is %i %s in %s." % (letterCount, letter, phrase))

    else:
        print("There are %i %s's in %s." % (letterCount, letter, phrase))



main()
