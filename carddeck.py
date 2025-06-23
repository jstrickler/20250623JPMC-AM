import random
from card import Card

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def draw(self):
        return self._cards.pop()
    
    def shuffle(self):
        random.shuffle(self._cards)

    def __str__(self):
        return f"CardDeck:{len(self._cards)}"

    def __repr__(self):
        return "CardDeck()"

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

if __name__ == "__main__":
    d1 = CardDeck()
    print(f"{d1 = }")
    d1.shuffle()
    print(f"{d1.cards = }")
    for _ in range(5):
        card = d1.draw()
        print(card)
    print(d1)
    print(f"{d1 = }")
    print(d1.get_ranks())
    print(CardDeck.get_ranks())
