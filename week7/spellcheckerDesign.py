"""
    Description: This program takes a document with misspelled words and finds
                 a correct spelling for each one based off of words similar to
                 it and how often they show up.
    Authors: Kenan Begovic '24, Sopo Guan '24, Jonas Pfefferman '24
    Date: 1/20/21
"""

def readFile(fileName):
  """
  Purpose: Read in all the typos from a document and store each word in a list
  Parameters: None
  Return Value: List of all the typos
  """
  #typosFile = open("typos.txt", 'r')
    #for line in typosFile:
        #line = line.strip()
        #typosList.append(line)
    #typosFile.close()
  print("in readFile()")
  typos = ["asd", "pgq", "aegro"]
  return typos


#------------------------------------------------------------------------------#
def readSystemWords(dictFile):
  """
  Purpose: Read in dictionary and store each word in a list
  Parameters: None
  Return Value: List of all the words in the dictionary
  """
  #dictionaryFile = open("dictionaryFull.txt", 'r')
      #for line in dictionaryFile:
          #line = line.strip()
          #dictionaryList.append(line)
      #dictionaryFile.close()
  print("in readSystemWords()")
  words = ["a", "and", "as"]
  return words


#------------------------------------------------------------------------------#
def readWrdCnt(countFile):
	"""
	Purpose: Reads through through Word Count puts words in list
  Parameters: None
  Return Value: A list of each word and a number relating to how often it appears
	"""
	print("in WrdCnt")

	count = []
	return count


#------------------------------------------------------------------------------#
def dictCheck(typo, dictionaryList):
  """
  Purpose: Checks to see if the typo is in the computer
  Parameters: The typo and the list of all dictionary words
  Return Value: True if the word is in the dictionary, False if not
  """
    #for typo in typosList:
        #if typo in dictionaryList:
            #return True
        #else:
            #return False
  print("in dictCheck()")
  return False


#------------------------------------------------------------------------------#
def insertionCheck(typo):
  """
  Purpose: removes an extra letter and adds to the list of possible words
  Parameters: The typo
  Return Value: Possible Words
  """
  print("in insertionCheck()")
  possibleWords = ["and", "pig", "agro"]
  return possibleWords


#------------------------------------------------------------------------------#
def transposeCheck(typo):
  """
  Purpose: switches the letters around and returns a list of all possible words
  Parameters: The typo
  Return Value: Possible Words
  """
  print("in transposeCheck()")
  possibleWords = ["as", "ping", "aero"]
  return possibleWords


#------------------------------------------------------------------------------#
def subCheck(typo):
  """
  Purpose: Substitutes a letter with one with a similar/the same sound
  Parameters: The typo
  Return Value: Possible Words
  """
  print("in subCheck()")
  possibleWords = ["as", "ping", "aero"]
  return possibleWords


#------------------------------------------------------------------------------#
def lacking(typo):
	"""
	Purpose: Insterts a letter into the word
  Parameters: The typo
  Return Value: Possible Words
	"""
	print("in lacking()")
	possbileWords = ["aa", "pogg", "aeroplane"]
	return possbileWords


#------------------------------------------------------------------------------#
def cutWords(possibleWords):
  """
  Purpose: Checks the possible words against the word count and picks the options
           with the use rate
  Parameters: list of possible words
  Return Value: edited list of likely words
  """
  print("in cutWords()")
  likelyWords = ["as", "pig", "agro"]


#------------------------------------------------------------------------------#
def displayWords(likelyWords):
  """
  Purpose: Takes all the most likely words and displays them for the user
  Parameters: List of the most likely words
  Return Value: None
  """

  print("in displayWords()")


#------------------------------------------------------------------------------#
def main():

  fileName = str(input("filename to check: "))
  words = readFile(fileName)
  english = readSystemWords("/usr/share/dict/words")
  wordCounts = readWrdCnt("/usr/share/dict/words")

  print(len(english))
  print(english[2])

  possibleWords = []

  for i in range(len(words)):
    typo = words[i]
    wordInDict = dictCheck(typo, english)
    if wordInDict == True:
      print("This word is not incorrect")
    else:
      possibleInsertions = insertionCheck(typo)
      possibleTranspo = transposeCheck(typo)
      possibleSubs = subCheck(typo)
      possibleLacking = lacking(typo)
      possibleWords = possibleInsertions + possibleTranspo + possibleLacking
      likelyWords = cutWords(possibleWords)
      displayWords(likelyWords)



main()
