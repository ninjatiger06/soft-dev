"""
    Description: Asks the user for an input string and then counts how many
                 total vowels are present in the given string.
    Author: Jonas Pfefferman '24
    Date: 11/20/20
"""

def main():

    word = str(input("input string: "))
    wordLower = word.lower()
    vowels = ["a", "e", "i", "o", "u"]

    vowelCount = 0
    for char in wordLower:
        if char in vowels:
            vowelCount += 1

    if vowelCount == 1:
        print("There is 1 vowel in that string.")
    else:
        print("There are %i vowels in that string." % (vowelCount))



main()
