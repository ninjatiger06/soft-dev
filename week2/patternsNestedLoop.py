"""
    Description: This program prints a pattern of numbers to a certain number
                that the user defines.
    Author: Jonas Pfefferman '24
    Date: 9/21/20
"""

def main():

    # Assigning the number variable based off of the user's input
    num = int(input("Enter a number to generate a cool pattern: "))

    # For loop to create the overall pattern
    patternCounter = ""
    for i in range(num):

        # Second for loop to create the number pattern for each line
        for j in range(1, num + 1):
            patternCounter += str(j) + " "

        # Adding a new line in after each number set
        patternCounter += "\n"

        # Displaying the results to the user
        print(patternCounter)



main()
