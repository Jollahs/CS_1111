import random

def pick_random_rps():
    # pick a random number between 0 and 2 inclusive
    random_number = random.randrange(0,3)

    # convert number to rps
    if random_number == 0:
        return "ROCK"
    elif random_number == 1:
        return "PAPER"
    else:
        return "SCISSORS"

def play_rock_paper_scissors():

    # Each player picks randomly: rock, paper, or scissors
    player1_pick = pick_random_rps()
    player2_pick = pick_random_rps()

    print("Player 1 picked", player1_pick)
    print("Player 2 picked", player2_pick)

    # Compare players picks and choose winner
    if (player1_pick == "ROCK" and player2_pick == "PAPER") or \
        (player1_pick == "SCISSORS" and player2_pick == "ROCK") or \
        (player1_pick == "PAPER" and player2_pick == "SCISSORS"):
        print("PLAYER 2 WINS!")
        return 2
    elif (player2_pick == "ROCK" and player1_pick == "PAPER") or \
        (player2_pick == "SCISSORS" and player1_pick == "ROCK") or \
        (player2_pick == "PAPER" and player1_pick == "SCISSORS"):
        print("PLAYER 1 WINS!")
        return 1
    else:
        print("TIE")
        return 0




if __name__ == '__main__':
    player1_wins = 0
    player2_wins = 0

    for i in range(10000):
        winner = play_rock_paper_scissors()

        if winner == 1:
            player1_wins = player1_wins + 1
        elif winner == 2:
            player2_wins += 1  # same as player2_wins = player2_wins + 1

    print("Of 10000 games, player 1 won", player1_wins,"and player 2 won", player2_wins)
