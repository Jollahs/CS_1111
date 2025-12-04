import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        for rank in range(10):
            for suit in ["H", "D", "C", "S"]:
                self.cards.append(Card(suit, rank))

    def deal_one(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        return "Deck has " + str(len(self.cards)) + " cards left"

class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def sum(self):
        total = 0
        for card in self.cards:
            total += card.rank
        return total

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

deck = Deck()

print(deck)

player1_hand = Hand()
player2_hand = Hand()

deck.shuffle()

player1_hand.add(deck.deal_one())
player2_hand.add(deck.deal_one())

player1_hand.add(deck.deal_one())
player2_hand.add(deck.deal_one())

print("Player 1 hand: ", player1_hand)
print("Player 2 hand: ", player2_hand)

while player1_hand.sum() < 21:
    player1_hand.add(deck.deal_one())

while player2_hand.sum() < 21:
    player2_hand.add(deck.deal_one())


print("Player 1 hand: ", player1_hand)
if player1_hand.sum() > 21:
    print("BUST!")
print("Player 2 hand: ", player2_hand)
if player2_hand.sum() > 21:
    print("BUST!")
