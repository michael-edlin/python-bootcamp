# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

import string

def hangman():
    # Hard-code the word to be guessed
    word_to_guess = "python"
    word_length = len(word_to_guess)
    attempts_left = 6  # Number of allowed incorrect guesses
    guessed_word = ["_"] * word_length  # Display blanks
    guessed_letters = set()  # Track guessed letters

    print("Welcome to Hangman!")
    print("Try to guess the word letter by letter.")
    print("You have 6 attempts to guess the word correctly.")

    while attempts_left > 0:
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Ask for user input
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"Good job! The letter '{guess}' is in the word.")
            # Update the guessed_word list
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts_left -= 1

        # Check if the player has won
        if "_" not in guessed_word:
            print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nYou've run out of attempts. The word was: {word_to_guess}")
        print("Better luck next time!")

if __name__ == "__main__":
    hangman()