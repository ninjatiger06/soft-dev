"""Description: This program adds an inputted character between the letters of
                an inputted string
    Author: Jonas Pfefferman '24
    Date: 9/15/20
"""

def main():

    # Getting the string and characters and assigning them to variables
    stringvar = str(input("enter a string: "))
    charvar = str(input("enter a char:"))

    # For loop to add the selected character between each letter of the string
    newPhrase = charvar + ""
    for char in stringvar:
        newPhrase = newPhrase + char + charvar

    # Displaying results to the user
    print(newPhrase)


main()