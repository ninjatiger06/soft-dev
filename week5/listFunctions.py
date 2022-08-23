"""
    Descrption: This program implements a number of list operations on a list
                that is inputted by the user.
    Author: Jonas Pfefferman '24
    Date: 12/1/20
"""

#------------------------------------------------------------------------------#
def inputInteger(prompt):
    """
    Purpose: Takes input from a user and checks to see if it is an integer
    Parameters: Prompt (string) used to ask the user for input
    Return Val: The user's input (integer)

    """
    while True:
        userInput = input(prompt)
        try:
            intInput = int(userInput)
            return intInput
        except ValueError:
            print("That is not a valid integer.")


#------------------------------------------------------------------------------#
def getListFromUser():
    """
    Purpose: Asks the user to enter a series of positive integers (using the
             the inputInteger function as a try/except) and enters them into
             a list. When the user enters 0 or a negative integer, it
             returns a list of all the integers that were entered
    Parameters: None
    Return Val: All the positive integers inputted by the user (list of integers)

    """
    userList = []
    while True:
        inputPrompt = "Enter a positive integer: "
        intInput = inputInteger(inputPrompt)
        if intInput > 0:
            userList.append(intInput)
            print("The list is now", userList)
        else:
            return userList


#------------------------------------------------------------------------------#
def largestIndex(numList):
    """
    Purpose: Takes the list of integers inputted by the user and finds the index
             of the largest element.
    Parameters: The list of numbers inputted by the user (list of integers)
    Return Val: Greatest element on the list (integer), Index of greatest
                element (integer). If list is empty, -1 (integer)

    """
    if len(numList) == 0:
        return -1, -1

    else:
        highestNumber = 0
        for i in range(len(numList)):
            if numList[i] > highestNumber:
                highestNumber = numList[i]
                highestIndex = i

    return highestNumber, highestIndex


#------------------------------------------------------------------------------#
def smallestIndex(numList):
    """
    Purpose: Takes the list of integers inputted by the user and finds the index
             of the smallest element.
    Parameters: The list of numbers inputted by the user (list of integers)
    Return Val: Smallest element on the list (integer), Index of least element
                (integer). If list is empty, -1 (integer)

    """
    if len(numList) == 0:
        return -1, -1

    else:
        lowestNumber = 100000000000000000000000000000000
        for i in range(len(numList)):
            if numList[i] < lowestNumber:
                lowestNumber = numList[i]
                lowestIndex = i

    return lowestNumber, lowestIndex


#------------------------------------------------------------------------------#
def findElement(element, numList):
    """
    Purpose: Takes the list inputted by the user and an element and then returns
             the index of the first occurence of the element in the list.
    Parameters: The user-inputted element (integer), list of numbers inputted by
                the user (list of integers)
    Return Val: Index of element (integer). If the element does not occur or the
                list is empty, -1 (integer)

    """

    if len(numList) == 0:
        return -1

    else:
        elementIndex = -1
        for i in range(len(numList)):
            if numList[i] == element:
                elementIndex = i

        return elementIndex


#------------------------------------------------------------------------------#
def average(numList):
    """
    Purpose: Finds the average of all the elements in the list
    Parameters: The list of numbers inputted by the user (list of integers)
    Return Val: Average of all the elements (float), if no elements returns 0.0
                (float)

    """

    if len(numList) == 0:
        return 0.0

    else:
        runningTotal = 0
        for num in numList:
            runningTotal += num
        average = runningTotal / len(numList)
        return average


#------------------------------------------------------------------------------#
def doubleList(numList):
    """
    Purpose: Takes the list inputted by the user and doubles every element.
    Parameters: The list of numbers inputted by the user (list of integers)
    Return Val: Same list but with each element replaced and doubled (list of
                integers)

    """

    for i in range(len(numList)):
        numList[i] = numList[i] * 2

    return numList


#------------------------------------------------------------------------------#
def insertAtIndex(numList, insertedElement, insertIndex):
    """
    Purpose: Takes the list, an element, and the index and returns the list
             the element inserted at the index.
    Parameters: The list of numbers inputted by the user (list of integers), the
                number to insert (integer), the index to insert it at (integer)
    Return Val: Same list with the index inserted (list of integers), If the
                position index is not valid, returns list unchanged (list of
                integers), if the list is empty, returns the
                list (empty list)

    """
    if insertIndex > len(numList):
        return numList

    numList = numList[:insertIndex] + [insertedElement] + numList[insertIndex:]

    return numList


#------------------------------------------------------------------------------#
def removeAtIndex(numList, removeIndex):
    """
    Purpose: Takes the list and the index and returns the list with the element
             at that index removed.
    Parameters: The list of numbers inputted by the user (list of integers), and
                the index to remove the element at (integer)
    Return Val: Same list with the element at the index removed (list of
                integers), If the position index is not valid, returns list
                unchanged (list of integers), if the list is empty, returns the
                list (empty list)

    """
    if removeIndex > len(numList):
        return numList

    numList = numList[:removeIndex] + numList[removeIndex + 1:]

    return numList


#------------------------------------------------------------------------------#
def main():
    print("Enter positive integers that will be stored in a list.")
    print("Enter a number less than or equal to 0 to stop.\n")

    numList = getListFromUser()
    print("The original list is:\n%s" % (numList))

    greatestElement, greatestIndex = largestIndex(numList)
    print("\nThe largest item in the list is %i" % (greatestElement))
    print("The position of this item is %i" % (greatestIndex))
    leastElement, leastIndex = smallestIndex(numList)
    print("The smallest item in the list is %i" % (leastElement))
    print("The position of this item is %i" % (leastIndex))

    userElementPrompt = ("\nEnter an integer to search for: ")
    userElement = inputInteger(userElementPrompt)
    elementIndex = findElement(userElement, numList)
    print("This element was found at index %i" % (elementIndex))

    listAverage = average(numList)
    print("\nThe average of the items is %.1f" % (listAverage))

    numList = doubleList(numList)
    print("\nThe list with all the elements doubled is: %s" % (numList))

    insertedElementPrompt = ("\nElement to insert: ")
    insertedElement = inputInteger(insertedElementPrompt)
    insertIndexPrompt = ("Index at which to insert the new element: ")
    insertIndex = inputInteger(insertIndexPrompt)
    numList = insertAtIndex(numList, insertedElement, insertIndex)
    print("Inserting element %i at index %i yeilds the list: %s" % (insertedElement,
          insertIndex, numList))

    removeIndexPrompt = ("\nIndex of element to remove: ")
    removeIndex = inputInteger(removeIndexPrompt)
    numList = removeAtIndex(numList, removeIndex)
    print("The list with element at index %i is: %s" % (removeIndex, numList))



main()
