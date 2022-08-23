"""
    Description: This program prints a pattern of numbers to a certain number
                that the user defines.
    Author: Jonas Pfefferman '24
    Date: 9/21/20
"""

def main():

    # assigning the number variable based off of the user's input
    num = int(input("Enter a number to generate a cool pattern: "))

    # for loop to create the pattern
    patternCounter = ""
    for i in range(1, num + 1):
        patternCounter += str(i) + " "

    patternCounter += "\n"
    print (patternCounter * num)

main()
