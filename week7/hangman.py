"""
	Description: This program recreates the game hangman, in which a word is
                 chosen in secret, and the player tries to guess the word by
                 guessing letters until either they've guessed all the letters
                 in the word or they run out of chances or "whamies"
    Author: Jonas Pfefferman '24
    Date: 1/4/21
"""

import random

#------------------------------------------------------------------------------#
def getRandomWord(dictionary):
	"""
    Description: Randomly selects a word (with 4 or more letters) from the dictionary
    Parameters: filename (path) of a .txt file with all the words in the dictionary (str)
    Return Value: a random word from the dictionary (string)
    """
	file = open("dictionary.txt", 'r') 			# opens file
	wordList = []						# make a list of all words >= 4 letters
	for line in file:					# loop over each line in the file
		word = line.strip()				# remove whitespace from the end of the line
		if len(word) >= 4:				# only include words with 4 or more letters
			wordList.append(word)		# add word to our list of acceptable words

	# randomly choose a single word from our new list and send it back to 'main' func
	randomWord = random.choice(wordList)
	return randomWord


#------------------------------------------------------------------------------#
def getLetter():
	"""
		Description: Asks the user to input a single lower-case letter between
		a and z. It will repeat the question until it has this.
		Parameters: None
		Return Value: Single lower-case letter from a-z (string)
	"""

	prompt = "Enter letter: "
	while True:
		userInput = str(input(prompt))
		if len(userInput) > 1:
			prompt = "Illegal choice; enter letter: "
		elif userInput.isalpha() == False:
			prompt = "Illegal choice; enter letter: "
		elif userInput.islower() == False:
			prompt = "Illegal choice; enter letter: "
		else:
			return userInput


#------------------------------------------------------------------------------#
def printStatus(visibleWord, whammiesLeft):
	"""
		Description: Prints the game status to the screen (the visible word and
					 remaining whammies).
		Parameters: visible version of the word (list of strings), number of
					whammies remaining (integer)
		Return Value: None
	"""
	print("\n*********************\nCurrent guess:")
	print("".join(visibleWord))
	print("\nYou have %i whammies remaining" % (whammiesLeft))


#------------------------------------------------------------------------------#
def scoreLetter(letter, secretWord, visibleWord):
	"""
		Description: This functions checks to see if the guessed letter is one of
					 the letters in the word. If it is, it then reveals that
					 letter to be visible in the word that is shown on-screen.
		Parameters: guessed letter (string), secret word (string), visible word
					(list of strings)
		Return Value: True (boolean) if the letter is in the secret word, False
					  (boolean) if it isn't in the secret word
	"""
	INWORD = False
	for i in range(len(secretWord)):
		if secretWord[i] == letter:
			visibleWord[i] = letter
			INWORD = True
	return INWORD

#------------------------------------------------------------------------------#
def main():
	print("Welcome to Hangman! Choose letters to uncover the secret word.")
	print("Beware: 6 incorrect choices means you lose!")
	whammiesLeft = 6

	secretWord = getRandomWord("dictionary.txt")
	print(secretWord)
	print("\nThere are %i letters in the word." % (len(secretWord)))

	visibleWord = []
	for i in range(len(secretWord)):
		visibleWord.append("-")

	while "".join(visibleWord) != secretWord or whammiesLeft > 0:
		gameStatus = printStatus(visibleWord, whammiesLeft)
		letter = getLetter()
		guessLetterStatus = scoreLetter(letter, secretWord, visibleWord)

		if guessLetterStatus == False:
			whammiesLeft += -1
			print("Whammy! %s is not in the word" % (letter))

	if "-" in visibleWord == False:
		print("\nCongratulations! You Win!")
		print("You correctly guessed the word %s, with %i whammies remaining" % (secretWord, whammiesLeft))
	elif whammiesLeft == 0:
		print("\nSorry, you lose.")
		print("The word was %s" % (secretWord))


main()
