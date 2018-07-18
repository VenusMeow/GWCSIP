#import the random number generator
from random import *

#setting up the list of words for guessing
words = ["yellow","red","blue","purple","black","white","orange","green","grey"]

#introduction
print("Welcome to the game! The category is going to be colors")

#pick a random word to be guess
randomIndex = randint(0,len(words)-1)
chosen = words[randomIndex]

#setting up the guessing board (dashes) and wrong answer board (wrong)
dashes = []
wrong = []

#flag for use later, to check if they didn't guess the letter correctly
flag = False

#setting up the guessing board with correct number of dashes
for i in range(len(chosen)):
	dashes.append("-")

#the player only have 10 trials
turns = 10

#start guessing
while turns > 0:
	#reset the flag for a fresh round
	flag = False
	#get user input for one guess
	guess = input("Guess a letter:  ")

	#check if they guess the letter correctly
	for i in range(len(chosen)):
		if (chosen[i]==guess):
			#if they get it correctly, replace dashes at all corresponded positions
			dashes[i] = guess
			#set flag for this round to be true since they guessed the letter correctly
			flag = True

	#if they got the letter wrong, it will be added to the wrong answer board
	if (flag == False):
		wrong.append(guess)

	#show player the guessing board and the wrong answers
	print("Guessing board: ", dashes)
	print("Wrong answers: ",wrong)

	#if they got the letter correct, also ask if they can guess the whole word already
	if (flag == True):
		answer = input("Can you guess the word? ")

		#if they answer yes and they got it correctly, break the while loop and end the game
		if (answer=="yes"):
			wordGuess = input("What do you guess? ")
			if (wordGuess==chosen):
				print("You win!")
				break

	#decreasing turns for each round
	turns -= 1

#if the players haven't got the correct guess of word but turns are already out, they lose
if (turns==0):
	print("You lose!")
