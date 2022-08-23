"""
  Description: This is a game that takes a word from the dictionary, scrambles it,
               and has the user guess other words from the letters to gain points.
  Authors: Kenan Begovic '24, Jonas Pfefferman '24
  Date: 3/4/21
"""

import random
from searches import *

#------------------------------------------------------------------------------#
def readFile(filename):
    """
    Description: Reads a file (in this case the dictionary) and turns all the
                 words into a list.
    Parmeters: Name of the dictionary file (string)
    Return Val: List of words in the dictionary (list of strings)
    """

    fileList = []

    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        lineList = list(line)
        if len(lineList) >= 4 and len(lineList) <= 6:
            word = "".join(lineList)
            fileList.append(word)
    file.close()
    return fileList


#------------------------------------------------------------------------------#
def getRandomWord(dictList):
    """
    Description: Picks a random word out of the dictionary that is more than
                 a certain length
    Parameters: List of dictionary words (list of strings)
    Return Val: Random word chosen from the dictionary (string)
    """

    randomWord = ""

    while len(randomWord) != 6:
        randomWord = random.choice(dictList)

    return randomWord


#------------------------------------------------------------------------------#
def shuffleWord(randomWord):
    """
    Description: Takes the random word and jumbles all the letters to display
    Parameters: The random word (string)
    Return Val: A shuffled version of the random word (string)
    """

    listWord = list(randomWord)
    random.shuffle(listWord)
    shuffledWord = "".join(listWord)

    return shuffledWord


#------------------------------------------------------------------------------#
def createWords(randomWord, dictList):
    """
    Description: Loops over each word in the dictionary and sends to
                 checkWordLetters(). If that's true, it adds the word to a list
                 of answers
    Parameters: The random word (string) and the list of dictionary words (list
                of strings)
    Return Val: A list of words created from the letters in the chosen word
                (list of strings)
    """

    answersList = []
    visibleList = []
    answersListLen = random.randrange(6, 15)

    for word in dictList:
        IS_WORD_MAKEABLE = checkWordLetters(randomWord, word)
        WORD_IS_ALPHA = randomWord.isalpha()
        if IS_WORD_MAKEABLE == True and WORD_IS_ALPHA == True:
            answersList.append(word)
            dashWord = "-" * len(word)
            visibleList.append(dashWord)
        if len(answersList) == answersListLen:
            break

    return answersList, visibleList


#------------------------------------------------------------------------------#
def checkWordLetters(randomWord, word):
    """
    Decription: Checks to see if there are enough letters in the random word to
                make the chosen word in the dictionary
    Parameters: Chosen word from the dictionary (string) and the random word (string)
    Return Val: True if there are enough letters, false if not
    """

    for letter in word:
        letterCount = word.count(letter)
        randomWordLetterCount = randomWord.count(letter)

        if letterCount > randomWordLetterCount:
            return False

    return True


#------------------------------------------------------------------------------#
def displayRules():
    """
    Description: Displays the rules of the game
    Parameters: None
    Return Val: None
    """

    print("Welcome to Word Warp v0.1!")
    print("Find as many words as you can from the given letters.")
    print("Only words of 4 or more letters count!")
    print("Longer words are worth more points:")
    print("\n\t4 letters.....4 points")
    print("\t5 letters.....5 points")
    print("\t6letters.....6 points")
    print("\nHit the ENTER key if you want to quit.")
    print("Enter ww to shuffle the given letters (and lose 5 points)")


#------------------------------------------------------------------------------#
def displayScore(visibleList, totalPoints, shuffledWord):
    """
    Description: Displays the scorecard before each round of user-input
    Parameters: The list of visible words (list of strings) and the total number
                of the user's points (integer)
    Return Val: None
    """
    print("----------------------------------------")
    print("\nCurrent Score: %i" % (totalPoints))
    print("Possible Words: %s" % (visibleList))
    print("\tLetters: %s" % (shuffledWord))


#------------------------------------------------------------------------------#
def getInput(shuffledWord, visibleList):
    """
    Description: Takes the user's word input and validates it
    Parameters: The shuffled word (string) and the visible list (list of strings)
    Return Val: The user's inputted word (string)
    """

    while True:
        userInput = str(input("\nYour Word: "))

        userInput = userInput.lower()
        userInput = userInput.strip()
        if userInput == "ww" or userInput == "":
            return userInput

        elif userInput.isalpha() == False:
            print("Not a valid word.")

        elif len(userInput) < 4 or len(userInput) > 6:
            print("Words must be 4-6 letters in length.")

        elif userInput in visibleList:
            print("That word has already been guessed!")

        elif validateLetters(userInput, shuffledWord) == False:
            print("Only the given letters can be used to make a word.")

        else:
            return userInput


#------------------------------------------------------------------------------#
def validateLetters(userInput, shuffledWord):
    """
    Description: Checks the letters of the user's input to see if they're within
                 those of the shuffled word.
    Parameters: The user's input (string) and the shuffled word (string)
    Return Val: True if there are enough letters from the shuffled word to match
                the user's input (boolean), False if not (boolean)
    """

    for letter in userInput:
        if letter not in shuffledWord:
            return False
        elif userInput.count(letter) > shuffledWord.count(letter):
            return False

    return True


#------------------------------------------------------------------------------#
def updateVisibleWords(visibleList, answerIndex, inputtedWord):
    """
    Description: Changes the displayed visible words list to show any inputted
                 word if it is in the answers list
    Parameters: the visible list its self (list of
                strings), the user's inputted word (string), and the index of
                the correct answer (integer)
    Return Val: The visible word list (list of strings)
    """

    for i in range(len(visibleList)):
        if i == answerIndex:
            visibleList[i] = inputtedWord

    return visibleList


#------------------------------------------------------------------------------#
def gameOver(totalPoints, answersList):
    """
    Description: Prints a scorecard at the end of the game
    Parameters: The user's total number of points (integer) and the answers
                (list of strings)
    Return Val: None
    """

    print("\nGame OVER.")
    print("Your final score was: %i" % (totalPoints))
    print("Possible Words: %s" % (answersList))

#------------------------------------------------------------------------------#
def main():

    dictList = readFile("dictionaryFull.txt")

    totalPoints = 0

    answersList = []

    while True:
        answersList = []
        while len(answersList) < 6:
            randomWord = getRandomWord(dictList)

            shuffledWord = shuffleWord(randomWord)

            answersList, visibleList = createWords(randomWord, dictList)

        displayRules()

        guessedWords = 0

        while guessedWords < len(answersList):
            displayScore(visibleList, totalPoints, shuffledWord)

            inputtedWord = getInput(shuffledWord, visibleList)

            if inputtedWord == "ww":
                shuffledWord = shuffleWord(shuffledWord)
                totalPoints -= 5
                print("-5")

            elif inputtedWord == "":
                break

            else:
                answerIndex = binarySearchIndex(inputtedWord, answersList)
                if answerIndex != -1:
                    totalPoints += len(inputtedWord)
                    print("+%i" % (len(inputtedWord)))
                    guessedWords += 1
                    visibleList = updateVisibleWords(visibleList, answerIndex, inputtedWord)
                else:
                    print("Not a valid word.")

        gameOver(totalPoints, answersList)

        if inputtedWord == "":
            break

        elif guessedWords == len(answersList):
            print("Good job!! You got all of the words!")
            playAgain = str(input("\nPlay Again with the chance to get a higher score? (Y/N) "))
            playAgain = playAgain.upper()
            if playAgain == "N":
                break



main()
