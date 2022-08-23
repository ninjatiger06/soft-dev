"""
    Description: This is a game where a user tries to get their level down to 0.
                 If they input something that isn't allowed, they will get a
                 random insult thrown their way.
    Author: Jonas Pfefferman '24
    Date: 10/22/20
"""

import random

def main():

    level = 10
    upAnswers = ["u", "U"]
    downAnswers = ["d", "D"]
    insults = ["u or d. Not that hard.", "You can read... right?", "Yeah... no",
               "You sure you made it past second grade?",
               "You should try to hit your head less.",
               "Definitely an intellectual here.",
               "Did you need help turning on the computer?",
               "Okay so I want you to hit Alt and F4 at the same time.",
               "Have you tried Control Alt Delete?"]

    print(". . . . . . . . . . . (%i)" % (level))
    answer = str(input("char (u/d): "))

    while level > 0:
        if answer in upAnswers:
            level += 1
            print(". . . . . . . . . . . (%i) level UP" % (level))
            answer = str(input("char (u/d): "))

        elif answer in downAnswers:
            level += -1
            print(". . . . . . . . . . . (%i) level down" % (level))
            answer = str(input("char (u/d): "))

        elif answer == "End Program":
            level = 0

        else:
            print(random.choice(insults))
            answer = str(input("char (u/d): "))

    if level == 0:
        print("G A M E  O V E R")



main()
