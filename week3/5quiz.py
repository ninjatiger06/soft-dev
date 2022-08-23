"""
    Description: Asks the user 5 yes or no questions
    Author: Jonas Pfefferman '24
    Date: 11/20/20
"""

def main():
    questions = ["Star Wars timeline uses BBC and ABC, or before or after the Battle of Couruscant",
                    "The Clone Wars began in 22 BBY and Ended in 19 ABY",
                    "The Battle of Yavin techincally takes place in the year 0 ABY",
                    "The Empire surrendered as of 4 ABY following the Battle of Endor",
                    "The New Republic's capital rotates planets"]
    answers = ["n", "y", "n", "n", "y"]

    userScore = 0
    for i in range(len(questions)):
        userAnswer = str(input(questions[:i] + "....... [y/n] "))
        if userAnswer == answers[:i]:
            print("CORRECT!")
            userScore += 1
        else:
            print("INCORRECT")

    print("You got %i out of %i correct!")
    if userScore >= 4:
        print("Awesome!")
    elif userScore >= 2 and userScore < 4:
        print("Nice try.")
    else:
        print("Maybe you'll do better next time...")



main()
