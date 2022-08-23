"""
    Description: This program checks an inputted word against the dictionary file
    using the binary search
    Author: Jonas Pfefferman '24
    Date: 2/25/21
"""

from time import time
from searchesStepCount import *

def main():

    wordList = []

    word = str(input("word: "))
    wordList.append(word)

    while word != "Done":
        word = str(input("word: "))
        if word != "Done":
            wordList.append(word)
            print(wordList)

    dictList = []

    dictionaryFile = open("dictionaryFull.txt", 'r')
    for line in dictionaryFile:
        line = line.strip()
        dictList.append(line)
    dictionaryFile.close()

    t1 = float(time())
    for i in range(len(wordList)):
        word = wordList[i]

        IS_WORD, binarySteps = binarySearch(word, wordList)

    t2 = float(time())
    binaryTime = float(t2 - t1)

    t1 = float(time())
    for i in range(len(wordList)):
        word = wordList[i]

        IS_WORD, linearSteps = linearSearch(word, wordList)
    t2 = float(time())
    linearTime = t2 - t1

    print("Binary Search: %i" % (binarySteps))
    print("Binary Search Execution Time: %f" % (binaryTime))
    print("Linear Search: %i" % (linearSteps))
    print("Linear Search Execution Time: %f" % (linearTime))

    if IS_WORD == True:
        print("Found")

    else:
        print("NOT Found")



main()
