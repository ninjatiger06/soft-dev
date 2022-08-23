"""
    Description: This program helps users practice their multiplication tables.
    It starts by asking the user to enter a starting factor (from 2-12) and then
    it randomly generates multiplication problems until the user answers 3 in a
    row correctly. When this happens, the program displays a score report and
    (encouraging) message for the user to let them know how they did.
    Author: Mr. Bloom/Jonas Pfefferman '24
    Date: 10/26/20
"""

import random

def getChoice(low, high):

    factor1 = int(input("What factor would you like to work on? "))
    while factor1 < low or factor1 > high:
        factor1 = int(input("What factor would you like to work on? "))

    return factor1



"""
Purpose:  Creates a multiplication problem and asks the user to answer it.
Parameters:  Takes a factor (integer) to be used in the multiplication problem.
Return Val:  Returns a string indicating whether their answer was correct or not.
"""


def question(factor1):

    factor2 = random.randrange(1, 13)
    print("----------------------------------")
    problem = "%i x %i? " % (factor1, factor2)
    userAnswer = int(input(problem))
    answer = factor1 * factor2
    if userAnswer == answer:
        print("....Correct!")
        return "correct"

    else:
        print("....Nope. %d x %d = %d" % (factor1, factor2, answer))
        return "incorrect"



def allResults(correctAnswers, totalAnswers):
    totals = "You got %i out of %i correct. " % (correctAnswers, totalAnswers)
    score = float(correctAnswers / totalAnswers)
    print(score)
    if score == 1:
        totals += "Perfect!"

    elif score <= 0.9:
        totals += "Excellent!"

    elif 0.8 <= score <= 0.89:
        totals += "Good Work!"
        return totals

    elif 0.7 <= score <= 0.79:
        totals += "You're Getting There..."

    elif 0.6 <= score <= 0.69:
        totals += "You Need Some More Practice..."

    else:
        totals += "You Need A Lot More Work..."


    print(totals)



def main():
    print("Welcome to MathQuiz v0.1!\n")    # display introductory message

    factor1 = getChoice(1, 12)               # starting factor to practice with
    correctAnswers = 0
    totalAnswers = 0
    correctStreak = 0
    factor = getChoice
    while correctStreak < 3:
        result = question(factor1)     # creates and asks a question

        if result == "correct":
            correctAnswers += 1
            totalAnswers += 1
            correctStreak += 1

        else:
            totalAnswers += 1
            correctStreak = 0

    allResults(correctAnswers, totalAnswers)



main()
