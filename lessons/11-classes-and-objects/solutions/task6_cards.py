import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["♠", "♥", "♦", "♣"]:
            for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        """Removes the top card from the deck and returns it"""
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


deck = Deck()
deck.shuffle()

hand = []
for i in range(5):
    hand.append(deck.deal())

# Join the cards' string representations together with spaces between them
hand_text = ""
for card in hand:
    hand_text = hand_text + str(card) + " "

print(f"Your hand: {hand_text}")
print(f"There are {len(deck)} cards left in the deck")
