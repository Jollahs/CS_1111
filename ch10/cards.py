import random

suits = ["❤️","♠️","♦️","♣️"]
ranks = []
for i in range(0,10):
    ranks.append(str(i))

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(rank + suit)


# shuffle the deck
random.shuffle(deck)

# divide the deck in half
p1_hand = []

p1_hand = deck[0:len(deck)//2]
p2_hand = deck[len(deck)//2:]
# num_cards = len(deck)
# for i in range(num_cards//2):
#     p1_hand.append(deck.pop())
# p2_hand = deck


while len(p1_hand) > 0 and len(p2_hand) > 0:
    # Each player plays a card (remove it from the top)
    p1_played_card = p1_hand.pop(0)
    p2_played_card = p2_hand.pop(0)

    print("P1 ", len(p1_hand), ":", p1_played_card, "  P2 ", len(p2_hand), ":", p2_played_card )
    if int(p1_played_card[0]) > int(p2_played_card[0]):
        # player 1 wins
        print("<--")
        p1_hand.append(p1_played_card)
        p1_hand.append(p2_played_card)
    elif int(p1_played_card[0]) < int(p2_played_card[0]):
        print("-->")
        p2_hand.append(p1_played_card)
        p2_hand.append(p2_played_card)
    else:
        print("DRAW")
        p1_hand.append(p1_played_card)
        p2_hand.append(p2_played_card)

    random.shuffle(p1_hand)
    random.shuffle(p2_hand)

print("P1 hand:", len(p1_hand), "cards")
print("P2 hand:", len(p2_hand), "cards")
# whoever's card is higher gets both cards (put them on the bottom)
