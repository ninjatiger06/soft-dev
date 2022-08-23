"""
    Description: This program checks an inputted word against the dictionary file
    using the binary search
    Author: Jonas Pfefferman '24
    Date: 2/25/21
"""

from searches import *

def main():

    word = str(input("word: "))

    wordList = []

    dictionaryFile = open("dictionaryFull.txt", 'r')
    for line in dictionaryFile:
        line = line.strip()
        wordList.append(line)
    dictionaryFile.close()

    IS_WORD = binarySearch(word, wordList)

    if IS_WORD == True:
        print("Found")

    else:
        print("NOT Found")



main()
