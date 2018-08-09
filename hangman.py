import random

gameOver = False
print("Hangman Game")

wordList = ["banana", "rectangle", "laptop", "curtains", "skyscraper",
                 "computer", "python", "programming", "facemask", "samurai",
                 "tracksuit", "duvet", "enemies", "stopwatch", "physics",
                 "pythagorean", "blanket", "musket", "warriors", "conditioner"
                 ]

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
	print("Enter a guess")
	print("You have " + str(lives) + " lives remaining.")
	print("Current word state:\n")
	print(guessed_word)

	guess = input().lower()
	# Check that the input was a letter and account for upper case
	if guess.isalpha() and guess not in guessedLetters:
		# Go through the secret word
		for letter in range(len(secretWord)):
			# See if the guessed letter is in the word
			if guess == secretWord[letter]:
				print("Correct")
				# Replace the - with the letter and add letter to history
				guessed_word[letter] = guess
				guessedLetters.append(guess)
		# If the letter isn't in the word, subtract 1 from lives and add letter to history
		if guess not in secretWord:
				print("Incorrect")
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


