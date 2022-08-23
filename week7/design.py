"""
    Description: This is the top-down design for getfit.py, which takes a user's
                 weekly step goal, window dimensions, and a data file containing
                 their weekly steps to graph out for each day if they made their
                 step goal and displays their step averages and other data.
    Author: Jonas Pfefferman '24
    Date: 1/25/21
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

    print("In getIntInput()")
    userInput = inputInteger(prompt)
    return userInput


#------------------------------------------------------------------------------#
def inputInteger(prompt):
    """
    Purpose: Asks for the user's input then runs a try/except to see if it works
             as an integer
    Parameters: Question prompt (string)
    Return Value: User-input in the correct data type (integer)
    """
    print("In inputInteger()")
    userInput = int(14)
    return userInput


#------------------------------------------------------------------------------#
def readFile(filename):
    """
    Purpose: Reads through the given data file and takes the name of each day
             and the number of steps walked that day
    Parameters: Data file name
    Return Value: a list of the names of the days of the week, a list of the
                  number of steps taken each day
    """

    print("In readFile()")
    stepList = [["monday", 1], ["tuesday", 3], ["wednesday", 5]]
    return weekdayNames, stepsWalked


#------------------------------------------------------------------------------#
def stepCalculations(stepsWalked):
    """
    Purpose: Runs all the calculations for the total and average number of steps
             taken
    Parameters: the list of the user's daily number of steps
    Return Value: the total number of steps and the average per day
    """
    print("In stepCalculations()")
    stepTotal = 12
    stepAverage = 4
    return stepTotal, stepAverage


#------------------------------------------------------------------------------#
def createGraphWin():
    """
    Purpose: Creates the graphics window
    Parameters: window width (integer), window height (integer)
    Return Value: Window
    """

    #get graphic window width
    windowWidth = getIntInput("prompt", 0, 10)

    #get graphic window height
    windowHeight = getIntInput("prompt", 0, 10)

    print("In createGraphWin()")

    gw = GraphWin("window", windowWidth, windowHeight)

    return gw


#------------------------------------------------------------------------------#
def createGoalLine(stepGoal):
    """
    Purpose: Creates the line in the window at the step goal
    Parameters: user's daily step goal (integer)
    Return Value: None
    """

    print("In createGoalLine()")

    return


#------------------------------------------------------------------------------#
def drawBar(gw, stepsWalked, weekdayNames, stepGoal):
    """
    Purpose: draws the bars in the bar graph
    Parameters: window's width (integer), window's height (integer), number of
                steps walked per day (integer), names of days of the week (string)
    Return Value: None
    """
    print("In drawBar")

    barColor = determineBarColor(stepsWalked, stepGoal)

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

    print("In determineBarColor()")

    return "green"


#------------------------------------------------------------------------------#
def displayText(gw, stepGoal, stepAverage, stepTotal):
    """
    Purpose: displays text at the top of the graphics window
    Parameters: window width (integer), window height (integer), user's step
                goal (integer), user's daily average (integer), user's total
                number of steps (integer)
    Return Value: none
    """

    print("In topText")

    return


#------------------------------------------------------------------------------#
def main():

    #get file name
    filename = "file.data"

    #get step goal
    stepGoal = getIntInput("prompt", minStepVal, maxStepVal)


    #Read the file and collect its data into lists
    stepList = readFile(filename)

    #Make necessary calculations
    stepTotal, stepAverage = stepCalculations(stepsWalked)

    #create graphics window
    gw = createGraphWin()
    goalLine = createGoalLine(stepGoal)
    for i in range(len(weekdayNames)):
        bar = drawBar(gw, stepsWalked, weekdayNames, stepGoal)
    topText = displayText(gw, stepGoal, stepAverage, stepTotal)



main()
