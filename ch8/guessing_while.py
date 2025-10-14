import random

def prompt_user():
    ret_val = int(input("Pick a hidden number between 1 and 100: "))
    return ret_val

num_guesses = 0

# Pick a hidden number between 1 and 100.
hidden_number = random.randrange(1, 101)

# Prompt the user for a guess.
user_guess = prompt_user()
num_guesses += 1

# While the user’s guess is not the hidden number,
while user_guess != hidden_number:
    # 	if their guess is higher, tell them it’s higher
    if user_guess > hidden_number:
        print("Too high!")
    else:
        # 	otherwise tell them it’s lower.
        print("Too low!")

    # 	Then prompt them for a new guess
    user_guess = prompt_user()
    num_guesses += 1


# At this point: user_guess == hidden_number
# Don’t forget to tell them when they get it right!
print("You got it in", num_guesses,"guesses!!!")
