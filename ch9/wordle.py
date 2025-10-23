

#computer picks a word
word = "CRIMP"

#USER GETS 5 guesses
GUESS_COUNT = 5

# for each guess
for GUESS in range(GUESS_COUNT):
    usr_guess = input("GUESS:\n")
    assert len(usr_guess) == 5

    # we check if it's correct
    if usr_guess == word:
        #if it is, game over, they win
        print("WELL DONE!")
        exit()

    feedback = ""
    #if not, mark letters based on correct identity and position
    for idx in range(len(usr_guess)):
        if word[idx] == usr_guess[idx]:
            feedback = feedback + "X"
        elif usr_guess[idx] in word:
            feedback = feedback + "O"
        else:
            feedback = feedback + " "
    print(feedback)
