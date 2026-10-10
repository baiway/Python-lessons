import random

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        """Returns the card's value, from 1 (ace) to 13 (king)"""
        return RANKS.index(self.rank) + 1

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["♠", "♥", "♦", "♣"]:
            for rank in RANKS:
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

score = 0
current = deck.deal()
while len(deck) > 0:
    print(f"The current card is {current}")
    guess = input("Will the next card be higher or lower? (h/l) ").lower()
    while guess not in ["h", "l"]:
        guess = input("Please enter 'h' or 'l': ").lower()

    next_card = deck.deal()
    print(f"The next card is {next_card}")

    # I've decided that a card with the same value counts as a correct guess
    went_higher = next_card.value() > current.value()
    if next_card.value() == current.value():
        print("Same value! Have that one for free.")
    elif (guess == "h" and went_higher) or (guess == "l" and not went_higher):
        print("Correct!")
    else:
        print("Wrong!")
        break

    score = score + 1
    current = next_card

print(f"Game over! Your score was {score}.")
