"""
    Description: This program allows the user to draw a forest in a graphics window.
    Author: Mr. Bloom, Jonas Pfefferman '24
    Date: 12/5/20
"""


from graphics import *
import random

def drawTree(grassHeight, window):
    x = window.getWidth()    # get width of window
    # pick random x from 0->width
    P1 = Point(random.randint(0, x), grassHeight)
    P2 = Point(random.randint(x, window.getHeight() * .75), window.getHeight()*.5)
    # draw tree trunk
    treeTrunk = Rectangle(P1, P2)
    trunkR = random.randrange(35, 204, 37)
    trunkG = random.randrange(18, 153, 75)
    trunkB
    = random.randrange(8, 102, 10)
    treeTrunk.setFill(color_rgb(trunkR, trunkG, trunkB))
    treeTrunk.setOutline(color_rgb(trunkR, trunkG, trunkB))
    treeTrunk.draw(gw)

    leafPoint = Point((P1 + P2) / 2,P1 + 4.5)
    leafRadius = random.randrange(10, 20)
    leaf = Circle(leafPoint, leafRadius)
    leafR = random.randrange(3, 61, 3)
    leafG = random.randrange(13, 254, 12.5)
    leafB = random.randrange(2, 34, 2)
    leaf.setFill(color_rgb(leafR, leafB, leafG))
    leaf.setOutline(color_rgb(leafR, leafB, leafG))
    leaf.draw(gw)
    # create a Point object at x, grassHeight
    # make other Point objects for the trunk (a Rectangle)
    # and the tree top (a Circle?)
    # pick a random shade of brown for the trunk
    # pick a random shade of green for the tree top
    # draw the trunk and the top in the window


def main():
    width = 600
    height = 400
    gw = GraphWin("a pretty forest", width, height)

    # sky
    gw.setBackground("lightblue")

    # grass
    grassHeight = 0.75 * height
    p1 = Point(0, grassHeight)
    p2 = Point(width, height)
    grass = Rectangle(p1, p2)
    grass.setFill("darkgreen")
    grass.setOutline("darkgreen")
    grass.draw(gw)

    # sun
    sun = Circle(Point(width*.15, height*.1),width*.05)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(gw)

    # draw a single tree
    drawTree(grassHeight, gw)

    # wait for user input (mouse-click) before ending program/closing window
    click = gw.getMouse()
    gw.close()



main()
