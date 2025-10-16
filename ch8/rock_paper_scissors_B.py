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

user_prompt = "ROCK, PAPER, or SCISSORS (or QUIT)? "

def get_valid_input():
    player1_pick = input(user_prompt)
    while (player1_pick != "ROCK" and player1_pick != "PAPER" and \
           player1_pick != "SCISSORS" and player1_pick != "QUIT"):
        print("INVALID INPUT! TRY AGAIN!")
        player1_pick = input(user_prompt)

    return player1_pick

QUIT = -2

def simulate_one_throw():
    # Each player picks randomly: rock, paper, or scissors
    # player1_pick = pick_random_rps()
    player1_pick = get_valid_input()
    if player1_pick == "QUIT":
        return QUIT

    player2_pick = pick_random_rps()

    print("Player 1 picked", player1_pick)
    print("Player 2 picked", player2_pick)

    # Compare players picks and choose winner
    if (player1_pick == "ROCK" and player2_pick == "PAPER") or \
            (player1_pick == "SCISSORS" and player2_pick == "ROCK") or \
            (player1_pick == "PAPER" and player2_pick == "SCISSORS"):
        winner = 2
    elif (player2_pick == "ROCK" and player1_pick == "PAPER") or \
            (player2_pick == "SCISSORS" and player1_pick == "ROCK") or \
            (player2_pick == "PAPER" and player1_pick == "SCISSORS"):
        winner = 1
    else:
        winner = 0

    print("PLAYER", winner, "WINS!")
    return winner


def play_one_round_rps():
    winner = -1

    while winner != 1 and winner != 2 and winner != QUIT:
        winner = simulate_one_throw()

    return winner


if __name__ == '__main__':
    player1_wins = 0
    player2_wins = 0

    continue_playing = True
    num_games = 0
    while continue_playing:
        winner = play_one_round_rps()

        if winner != QUIT:
            num_games += 1
            if winner == 1:
                player1_wins = player1_wins + 1
            elif winner == 2:
                player2_wins += 1  # same as player2_wins = player2_wins + 1
        else:
            continue_playing = False

    print("Of", num_games,"games, player 1 won", player1_wins,"and player 2 won", player2_wins)
