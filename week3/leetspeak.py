"""
    Description: Leet speak is a program that will take a string and use Leet
                 Speak (modifying text by replacing some letters with
                 symbols/numbers) to convert it.
    Author: Jonas Pfefferman '24
    Date: 10/9/20
"""

def main():

    # Getting the string from user input
    phrase = str(input("Enter a string: "))

    leetPhrase = ""
    for char in phrase:
        if char == "e" or char == "E":
            leetPhrase += "3"

        elif char == "l" or char == "L":
            leetPhrase += "1"

        elif char == "s" or char == "S":
            leetPhrase += "5"

        else:
            leetPhrase += char

    print("Leet version: %s" % (leetPhrase))



main()
