import random

MAX_VALUE = 100

# Design and write a program that assigns a number
# (chosen by you) between 1 and 10 to a variable
real_number = random.randrange(1,MAX_VALUE+1)

# Adapt the program to give the user 5 guesses.
for i in range(5):
    # then prompts the user to guess the number.
    user_guess = int(input("Please guess an integer between 1 and " + str(MAX_VALUE) + ", inclusive: "))

    if real_number < user_guess:
        print("You guessed too high!")
    elif real_number > user_guess:
        print("You guessed too low!")
    else:
        print("Bingo! Yahtzee! You guessed it!")
        exit()
