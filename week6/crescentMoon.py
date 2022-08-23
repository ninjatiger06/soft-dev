"""
    Description: This program draws a crescent moon and star-filled sky.
    Author: Mr. Bloom, Jonas Pfefferman
    Date: 12/15/20
"""

from graphics import *
from random import *

def main():

    # create graphics window
    winHeight = 400
    winWidth = 600
    gw = GraphWin("Night Sky", winWidth, winHeight)
    # set background to black
    gw.setBackground("black")

    # for loop to create stars
    for i in range(random.randint(50, 150)):
    #    pick random x from 0->width
        starPositionX = random.randint(0, 600)
    #    pick random y from 0->height
        starPositionY = random.randint(0, 400)
    #    pick random radius
        starRadius = random.randint(1, 3)
    #    pick circle point
        starPoint = (starPositionX, starPositionY)
    #    draw circle, color it white
        star = Circle(starPoint, starRadius)

        star.draw(gw)
    #
    # create and draw a white circle
    moonPoint = (350, 250)
    moon = Circle(moonPoint, 100)
    moon.setFill("white")
    # clone circle, draw it, move it a little, color it black
    moonDark = moon.clone()
    moonDark.move(25, 0)
    moonDark.setFill("black")
    moon.draw(gw)
    moonDark.draw(gw)


    # wait for user input before ending program/closing window
    click = gw.getMouse()
    gw.close()


main()
