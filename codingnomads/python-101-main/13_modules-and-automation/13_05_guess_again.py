# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

def guess_my_number():
    # Set the range for the number to be guessed
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)

    # Set the number of attempts allowed
    max_attempts = 5

    print(f"Welcome to Guess My Number! I have chosen a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it correctly.")

    # Start the guessing loop
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Take a guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

# Start the game
if __name__ == "__main__":
    guess_my_number()