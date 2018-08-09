import random

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

guessState = []
guessedLetters = []
lives = 10

while gameOver == False:
	print("You have " + str(lives) + " lives remaining.\n")
	print("Current word state:\n")
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
					gameOver = True
		# If the letter isn't in the word, subtract 1 from lives and add letter to history
		if guess not in secretWord:
				print("Incorrect\n")
				lives-=1
				guessedLetters.append(guess)
		# If lives = 0, game over!
		if lives == 0:
			print("Unlucky! The word was " + secretWord)
			print("Game over!")
			gameOver = True
	# The input was a repeat or invalid
	else:
		print("You already tried that letter, or didn't enter a letter!")


