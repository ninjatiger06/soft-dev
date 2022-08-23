"""
    Description: This takes a user's weekly step goal, window dimensions, and a
                 data file containing their weekly steps to graph out for each
                 day if they made their step goal and displays their step
                 averages and other data.
    Author: Jonas Pfefferman '24
    Date: 2/8/21
"""

from graphics import *

#------------------------------------------------------------------------------#
def getIntInput(prompt, minVal, maxVal):
    """
    Purpose: Checks to see if the user-input matches with the minimum and maximum
             value allowed for each field
    Parameters: Question prompt (string), minimum value (integer), maximum value
                (integer)
    Return Value: The user's step goal (integer), window width (integer),
                   window height (integer)
    """

    userInput = inputInteger(prompt)
    while True:
        if minVal <= userInput and maxVal >= userInput:
            return userInput
        else:
            print("Invalid entry: Must be between %i and %i" % (minVal, maxVal))
            userInput = inputInteger(prompt)


#------------------------------------------------------------------------------#
def inputInteger(prompt):
    """
    Purpose: Asks for the user's input then runs a try/except to see if it works
             as an integer
    Parameters: Question prompt (string)
    Return Value: User-input in the correct data type (integer)
    """
    while True:
        inputInteger = input(prompt)
        try:
            intInput = int(inputInteger)
            return intInput
        except ValueError:
            print("That is not a valid integer.")


#------------------------------------------------------------------------------#
def readFile(filename):
    """
    Purpose: Reads through the given data file and takes the name of each day
             and the number of steps walked that day
    Parameters: Data file name
    Return Value: a list of the names of the days of the week, a list of the
                  number of steps taken each day
    """

    stepList = []

    stepFile = open(filename, 'r')
    for line in stepFile:
        line = line.strip()
        lineList = line.split(",")
        day = lineList[0]
        step = int(lineList[1])
        stepList.append([day, step])
    stepFile.close()

    return stepList


#------------------------------------------------------------------------------#
def stepCalculations(stepList):
    """
    Purpose: Runs all the calculations for the total and average number of steps
             taken
    Parameters: the list of the user's daily number of steps
    Return Value: the total number of steps and the average per day
    """
    stepTotal = 0
    for list in stepList:
        stepTotal += list[1]

    stepAverage = stepTotal / len(stepList)

    return stepTotal, stepAverage


#------------------------------------------------------------------------------#
def createGraphWin():
    """
    Purpose: Creates the graphics window
    Parameters: window width (integer), window height (integer)
    Return Value: Window
    """

    #get graphic window width
    windowWidth = getIntInput("Enter width of window: ", 200, 2500)

    #get graphic window height
    windowHeight = getIntInput("Enter height of window: ", 200, 1300)

    gw = GraphWin("Get Fit!", windowWidth, windowHeight)

    return gw


#------------------------------------------------------------------------------#
def displayText(gw, stepGoal, stepAverage, stepTotal):
    """
    Purpose: displays text at the top of the graphics window
    Parameters: window width (integer), window height (integer), user's step
                goal (integer), user's daily average (integer), user's total
                number of steps (integer)
    Return Value: none
    """
    p1 = Point(0, 0)
    p2 = Point(gw.getWidth(), gw.getHeight() / 8)
    textBox = Rectangle(p1, p2)
    textBox.setFill("white")
    textBox.setOutline("white")
    textBox.draw(gw)

    textSize = determineTextSize(gw)

    y = (gw.getHeight() / 8) / 2
    x1 = gw.getWidth() * 0.15
    x2 = gw.getWidth() * 0.5
    x3 = gw.getWidth() * 0.85

    t1 = Text(Point(x1, y), "Daily goal: %d" % (stepGoal))
    t1.setSize(int(textSize * 0.65))
    t1.setFill("black")
    t1.setOutline("black")
    t1.draw(gw)

    t2 = Text(Point(x2, y), "Average steps: %d" % (stepAverage))
    t2.setSize(int(textSize * 0.65))
    t2.setFill("black")
    t2.setOutline("black")
    t2.draw(gw)

    t3 = Text(Point(x3, y), "Total steps: %d" % (stepTotal))
    t3.setSize(int(textSize * 0.65))
    t3.setFill("black")
    t3.setOutline("black")
    t3.draw(gw)

    return


#------------------------------------------------------------------------------#
def drawBar(gw, stepList, stepGoal):
    """
    Purpose: draws the bars in the bar graph
    Parameters: the graphics window, the list of days of the week and steps (list
                of lists of strings, integers)
    Return Value: None
    """
    tallestBarVal = 0
    for dayData in stepList:
        barVal = dayData[1]
        if barVal > tallestBarVal:
            tallestBarVal = barVal

    barProp = tallestBarVal / (gw.getHeight() * (7/8))

    for i in range(len(stepList)):
        barHeight = stepList[i][1] / barProp
        barWidth = gw.getWidth() / len(stepList)

        x1 = barWidth * i
        x2 = barWidth * (i+1)
        y1 = gw.getHeight() - barHeight
        y2 = gw.getHeight()

        p1 = Point(x1, y1)
        p2 = Point(x2, y2)

        bar = Rectangle(p1, p2)
        barColor = determineBarColor(stepList[i][1], stepGoal)
        bar.setFill(barColor)
        bar.setOutline("black")
        bar.setWidth(4)
        bar.draw(gw)

        barLabel = stepList[i][0][:3]
        labelX = int(x1 + barWidth / 2)
        labelY = gw.getHeight() * .9
        labelPos = Point(labelX, labelY)
        label = Text(labelPos, barLabel)
        textSize = determineTextSize(gw)
        label.setSize(textSize)
        label.setStyle("bold")
        label.draw(gw)

    goalLine = createGoalLine(gw, stepGoal, barProp)

    return


#------------------------------------------------------------------------------#
def determineBarColor(stepsWalked, stepGoal):
    """
    Purpose: checks the steps walked on a certain day against the user's goal
             to determine whether the bar should be green, for meeting/exceeding
             the goal or red for not meeting the goal
    Parameters: number of steps walked per day (integer) and the user's step
                goal (integer)
    Reutrn Value: color of bar (string)
    """
    if stepsWalked >= stepGoal:
        color = "green"
    else:
        color = "red"

    return color


#------------------------------------------------------------------------------#
def createGoalLine(gw, stepGoal, barProp):
    """
    Purpose: Creates the line in the window at the step goal
    Parameters: user's daily step goal (integer)
    Return Value: None
    """
    x1 = 0
    y = gw.getHeight() - (stepGoal / barProp)
    x2 = gw.getWidth()

    p1 = Point(x1, y)
    p2 = Point(x2, y)

    goalLine = Line(p1, p2)
    goalLine.setFill("black")
    goalLine.setOutline("black")
    goalLine.setWidth(2)
    goalLine.draw(gw)


#------------------------------------------------------------------------------#
def determineTextSize(gw):
    if gw.getWidth() >= 1000:
        textSize = gw.getWidth() * .0144

    elif gw.getWidth() < 500:
        textSize = gw.getWidth() * .04

    else:
        textSize = gw.getWidth() * .028

    return int(textSize)


#------------------------------------------------------------------------------#
def main():

    #get file name
    filename = input("Enter file name with step data: ")

    #get step goal
    stepGoal = getIntInput("Enter step goal: ", 1000, 20000)


    #Read the file and collect its data into lists
    stepList = readFile(filename)

    #Make necessary calculations
    stepTotal, stepAverage = stepCalculations(stepList)

    #create graphics window
    gw = createGraphWin()
    topText = displayText(gw, stepGoal, stepAverage, stepTotal)
    bar = drawBar(gw, stepList, stepGoal)

    click = gw.getMouse()
    gw.close()



main()
