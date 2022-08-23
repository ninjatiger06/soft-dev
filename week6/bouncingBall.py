"""
    Description: This program animates a ball to make it look like it is
                 bouncing off the walls of the window.
    Author: Mr. Bloom
    Date: Fall 2019
"""

from graphics import *
from time import sleep

def main():

    # set up graphics window
    width = 600
    height = 400
    gw = GraphWin("animation...", width, height)
    gw.setBackground("darkblue")

    # instructions for user
    text = Text(Point(width*.5, 15), "Click to animate...")
    text.setOutline("white")
    text.setSize(18)
    text.draw(gw)

    # ball
    ball = Circle(Point(width*.5, height*.5), width*.08)
    ball.setFill("white")
    ball.setOutline("white")
    ball.draw(gw)

    # wait until user clicks before starting the animation
    click = gw.getMouse()

    # simple animation
    dx = 1
    while True:
        ball.move(dx, 0)          # ball moves 1 pixel to the right
        sleep(0.01)             # halt program for 1/100 of a second, & repeat loop
        if ball.getCenter().getX() > gw.getWidth() - ball.getRadius():
            dx = -1.0 * dx
        if ball.getCenter().getX() < 0 + ball.getRadius():
            dx = 1

        key = gw.getKey()
        if key == 'p':
            dx = 0

        click = gw.checkMouse()
        if click != None:
            break


    # wait for user input (mouse-click) before ending program/closing window
    click = gw.getMouse()
    gw.close()



main()
