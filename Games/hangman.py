# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 09:04:51 2018

@author: ShirleyLiu
"""
#This is hangman game

import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
	index = random.randint(0,len(wordList) - 1)
	return wordList[index]

def ShowInfo(missedLetters,correctLetters,secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()

	print('Missed letters:',end=' ')
	print(missedLetters)

	blank = '_' * len(secretWord)
	for i in range(0,len(secretWord)):
		if secretWord[i] in correctLetters:
			blank = blank[:i] + secretWord[i] + blank[i+1:]

	for letters in blank:
		print(letters,end=' ')
	print()

# def getGuess(AlreadyGuessed):
# 	print('Guess a letter.')
# 	guess = input().lower()

# 	if len(guess) != 1:
# 		print('Please guess A letter.')
# 	elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
# 		print('Please guess a LETTER.')
# 	elif guess in AlreadyGuessed:
# 		print('You\'ve already guess this letter,\n Please guess another letter.')
# 	else:
# 		return guess

#####################
# cannot use function former, because it can lead to NoneType return
#
## Traceback (most recent call last):
#   File "/Users/kevinliu/Documents/Code/PythonNote/Games/hangman.py", line 97, in <module>
#     if guess in secretWord:#guess true
# TypeError: 'in <string>' requires string as left operand, not NoneType
#####################

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def guessAgain():
	print('Do you want to guess again? (yes or no)')
	return input().lower().startswith('y')

# main program
print('H A N G M A N')
correctLetters = ''
missedLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	ShowInfo(missedLetters,correctLetters,secretWord)
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:#guess true
		correctLetters = correctLetters + guess

		guessAll = True
		for letter in secretWord:
			if letter not in correctLetters:
				guessAll = False
				break

		if guessAll:
			print('Yes! the secret words is \''+ secretWord +'\'.You have won!')
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess

		if len(missedLetters) == len(HANGMAN_PICS) - 1:
			ShowInfo(missedLetters,correctLetters,secretWord)
			print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
			gameIsDone = True

	if gameIsDone:
		if guessAgain():
			correctLetters = ''
			missedLetters = ''
			secretWord = getRandomWord(words)
			guessDone = False
		else:
			break
