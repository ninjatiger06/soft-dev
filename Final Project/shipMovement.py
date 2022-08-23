"""
    Description: Figures out how to move the ship usign WSAD so that it can be
                 later converted into C#
    Author: Jonas Pfefferman '24
    Date: 3/30/21
"""

from graphics import *

def main():

    gw = GraphWin("SHIP MOVEMENT TEST", 1080, 720)

    gw.setBackground("lightblue")

    p1 = Point(540, 370)
    p2 = Point(560, 350)
    ship = Rectangle(p1, p2)
    ship.setFill("red")
    ship.setOutline("black")
    ship.draw(gw)

    while True:
        userInput = str(input("Direction: "))
        userInput = userInput.lower()

        if userInput == "w":
            ship.move(0, -10)

        elif userInput == "s":
            ship.move(0, 10)

        elif userInput == "a":
            ship.move(-10, 0)

        elif userInput == "d":
            ship.move(10, 0)

        elif userInput == "exit":
            gw.close()
            break

        else:
            print("Invalid Input")


main()
