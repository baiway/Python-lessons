from dataclasses import dataclass, field
import random

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


@dataclass(order=True)
class Card:
    # `value` comes first, so cards are sorted by value. `compare=False` means
    # the rank and suit are ignored when comparing cards, and `init=False` means
    # we don't pass `value` in ourselves: `__post_init__` works it out instead.
    value: int = field(init=False)
    rank: str = field(compare=False)
    suit: str = field(compare=False)

    def __post_init__(self) -> None:
        """Called automatically by the generated `__init__`"""
        self.value = RANKS.index(self.rank) + 1

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"


deck = [Card(rank, suit) for suit in "♠♥♦♣" for rank in RANKS]
hand = random.sample(deck, 5)

print("Hand:   " + " ".join([str(card) for card in hand]))
print("Sorted: " + " ".join([str(card) for card in sorted(hand)]))
