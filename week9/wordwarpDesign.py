"""
  Description: Top down design for wordwarp.py
  Authors: Kenan Begovic '24, Jonas Pfefferman '24
  Date: 3/4/21
"""

#------------------------------------------------------------------------------#
def readFile(filename):
    """
    Description: Reads a file (in this case the dictionary) and turns all the
                 words into a list.
    Parmeters: Name of the dictionary file (string)
    Return Val: List of words in the dictionary (list of strings)
    """

    dictList = ["test", "testing", "is", "sin"]

    return dictList


#------------------------------------------------------------------------------#
def getRandomWord(dictList):
    """
    Description: Picks a random word out of the dictionary that is more than
                 a certain length
    Parameters: List of dictionary words (list of strings)
    Return Val: Random word chosen from the dictionary (string)
    """

    randomWord = "testing"

    return randomWord


#------------------------------------------------------------------------------#
def shuffleWord(randomWord):
    """
    Description: Takes the random word and jumbles all the letters to display
    Parameters: The random word (string)
    Return Val: A shuffled version of the random word (string)
    """

    shuffledWord = "stenigt"

    return shuffledWord


#------------------------------------------------------------------------------#
def createWords(randomWord, dictList):
    """
    Description: Takes the letters in the random word and mixes them in an
                 attempt to make other possible words
    Parameters: The random word (string)
    Return Val: A list of words created from the letters in the chosen word
                (list of strings)
    """

    word = "test"

    WORD_IS_VALID = validateWord(word, dictList)

    answersList = ["test", "is", "sin"]

    return answersList


#------------------------------------------------------------------------------#
def validateWord(word, dictList):
    """
    Description: Checks to see if the word is in the dictionary.
    Parameters: The jumbled word (string) and the dictionary list (list of
                strings)
    Return Val: True if the word is in the dictionary, False if not
    """

    return True
#------------------------------------------------------------------------------#
def createVisibleWords(answersList):
    """
    Description: Turns the list of answers into a displayed list of dashes.
    Parameters: The list of possible words (list of strings)
    Return Val: List of dashes in the place of words (list of strings)
    """

    visibleList = ["----", "--", "---"]

    return visibleList


#------------------------------------------------------------------------------#
def displayRules():
    """
    Description: Displays the rules of the game
    Parameters: None
    Return Val: None
    """

    return


#------------------------------------------------------------------------------#
def displayScore(visibleList, totalPoints):
    """
    Description: Displays the scorecard before each round of user-input
    Parameters: The list of visible words (list of strings) and the total number
                of the user's points (integer)
    Return Val: None
    """

    return


#------------------------------------------------------------------------------#
def userInput():
    """
    Description: Takes the user's word input
    Parameters: None
    Return Val: The user's inputted word (string)
    """

    input = "test"

    WORD_IS_VALID = validateWord(input)

    return input


#------------------------------------------------------------------------------#
def checkWord(word, answersList):
    """
    Description: Checks to see if the user's word is a possible answer
    Parameters: user's word (string) and the answers (list of strings)
    Return Val: True if the user's word is an answer, False if not
    """

    if word in answersList:
        return True

    else:
        return False


#------------------------------------------------------------------------------#
def updateVisibleWords(answersList, visibleList, inputtedWord):
    """
    Description: Changes the displayed visible words list to show any inputted
                 word if it is in the answers list
    Parameters: answers (list of strings), the visible list its self (list of
                strings), and the user's inputted word (string)
    Return Val: The visible word list (list of strings)
    """

    visibleList = ["test", "--", "---"]

    return visibleList


#------------------------------------------------------------------------------#
def isGameOver(totalPoints, answerList):
    """
    Description: Prints a scorecard at the end of the game
    Parameters: The user's total number of points (integer) and the answers
                (list of strings)
    Return Val: None
    """
    print(finalscore)
	  print(answersList)

#------------------------------------------------------------------------------#
def main():

    filename = "dictionaryFull.txt"
    dictList = readFile(filename)

    randomWord = getRandomWord(dictList)

    shuffledWord = shuffleWord(randomWord)

    answersList = createWords(randomWord, dictList)

    visibleList = createVisibleWords(answersList)

    displayRules()

    guessedWords = 0

    totalPoints = 0
    while guessedWords < len(answersList):
        displayScore(visibleList, totalPoints)

        inputtedWord = userInput()

        WORD_IN_LIST = checkWord(inputtedWord, answersList)

        if WORD_IN_LIST == False:
            if inputtedWord == "WW":
                shuffledWord = shuffleWord(shuffledWord)
                totalPoints += -5

            elif inputtedWord == "\n"
                break

        visibleList = updateVisibleWords(answersList, visibleList, inputtedWord)

        newPoints = 4
        totalPoints += newPoints

    gameOver(totalPoints, answersList)



main()
