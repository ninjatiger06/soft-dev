"""
    Description: This program asks the user if they would like to play Global
                 Thermonuclear War and prints a response based off of their
                 answer
    Author: Jonas Pfefferman '24
    Date: 10/1/20
"""

def main():

    yesAnswers = ["yes", "y", "sure", "Yes", "Y", "Sure", "YES", "SURE"]
    noAnswers = ["no", "nope", "n", "No", "Nope", "N", "NO", "NOPE"]
    answer = input("Would you like to Play Global Thermonuclear War? ")

    if answer in yesAnswers:
        print("\n<large explosion>.........you LOSE!")

    elif answer in noAnswers:
        print("\nThe only winning move is not to play. \n \t \t \t--JOSHUA")

    else:
        print("\nHow about a nice game of chess?")



main()
