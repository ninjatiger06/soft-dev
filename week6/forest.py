"""
    Description: Draws a forest with randomly-generated trees
    Author: Jonas Pfefferman '24
    Date: 12/15/20
"""

from graphics import *

def main():

    #make window
    windowWidth = 600
    windowHeight = 400
    gw = GraphWin("Beautiful Forest", windowWidth, windowHeight)

    #draw sky
    gw.setBackground("lightblue")

    #draw grass
    grassHeight = windowHeight * .75
    grassTopLeft = Point(0, grassHeight)
    grassBottomRight = Point(windowWidth, windowHeight)
    grass = Rectangle(grassTopLeft, grassBottomRight)
    grass.setFill("darkgreen")
    grass.setOutline("darkgreen")
    grass.draw(gw)

    #draw sun
    sun = Circle(Point(windowWidth * .85, windowHeight * .1), windowWidth * .05)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(gw)

    #wait for user input to end program
    click = gw.getMouse()
    gw.close()

main()
