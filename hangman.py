import random

def main():
	gameOver = False
	print("Hangman Game\n\n")

	wordList = ["banana", "rectangle", "laptop", "curtains", "skyscraper",
	                 "computer", "python", "programming", "facemask", "samurai",
	                 "tracksuit", "duvet", "enemies", "stopwatch", "physics",
	                 "pythagorean", "blanket", "musket", "warriors", "conditioner"
	                 ]

	# Use random to pick a random word from the list
	secretWord = random.choice(wordList).lower()

	# Create a list and populate it with N '-'
	# Where N = length of word
	guessed_word = []
	for letter in secretWord:
		guessed_word.append("-")

	# Store a history of guessed letters
	guessedLetters = []

	difficultySelect = True

	# Difficulty selection
	while difficultySelect == True:
		print("What difficulty mode would you like to play? [1, 2, 3]")
		print("1 - Easy\n2 - Medium\n3 - Hard")
		difficultyMode = int(input())
		if difficultyMode == 1:
			print("You selected easy!\n")
			lives = 18
			difficultySelect = False
			continue
		if difficultyMode == 2:
			print("You selected medium!\n")
			lives = 10
			difficultySelect = False
			continue
		if difficultyMode == 3:
			print("You selected hard!\n")
			lives = 7
			difficultySelect = False
			continue
		else:
			print("Invalid input - enter the number corresponding to the difficulty mode!")

	while gameOver == False:
		print("You have " + str(lives) + " lives remaining.\n")
		print("Currently guessed:\n")
		# Strip brackets and commas to print out
		print(*guessed_word, sep='')
		print("\nEnter a guess")

		# Check that the input was a letter and account for upper case
		guess = input().lower()
		# Check the input is only 1 character
		if len(guess) != 1:
			print("Please only enter one letter at a time")
			continue
		# If the guess is a letter and hasn't already been guessed, proceed
		if guess.isalpha() and guess not in guessedLetters:
			# Go through the secret word
			for letter in range(len(secretWord)):
				# See if the guessed letter is in the word
				if guess == secretWord[letter]:
					print("Correct\n")
					# Replace the - with the letter and add letter to history
					guessed_word[letter] = guess
					guessedLetters.append(guess)
					# if all the - have been replaced, it means they guessed the word
					if "-" not in guessed_word:
						print("Congratulations, you win!")
						print("You correctly guessed the word " + secretWord)	
						playAgain("Would you like to play again?")
			# If the letter isn't in the word, subtract 1 from lives and add letter to history
			if guess not in secretWord:
					print("Incorrect\n")
					lives-=1
					guessedLetters.append(guess)
			# If lives = 0, game over!
			if lives == 0:
				print("Unlucky! The word was " + secretWord)
				print("Game over!")
				playAgain("Would you like to play again?")
		# The input was a repeat or invalid
		else:
			print("You already tried that letter, or didn't enter a letter!")

# Play again function
def playAgain(prompt):
	valid = False
	while valid == False:
		answer = input(prompt + " [Y/N]").lower()
		# Run the program again if chosen, if not just leave
		if answer == "y":
			main()
		if answer == "n":
			exit()
		else:
			print("Invalid input")

main()


