"""
    Description: This program adds dashes between each character from a string
                entered by the user.
    Author: Jonas Pfefferman '24
    Date: 9/21/20
"""

def main():

    # Getting the string and assgining to a variable
    text = str(input("Enter text: "))

    # For loop to add dashes between the characters
    dashText = "-" + ""
    for char in text:
        dashText += char + "-"

    # Displaying results to the user
    print(dashText)



main()