#!/usr/bin/env python
import random

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    # constructor
    def __init__(self, x):
        # set self._dealer_name
        self.dealer_name = x
        self._make_deck()

    @classmethod
    def show_suits(cls):
        return cls.SUITS


    # instance method (private)
    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    # property
    @property
    def cards(self):
        return self._cards

    # instance method (public)
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()


    # dealer getter
    @property
    def dealer_name(self):
        return self._dealer_name

    # dealer setter
    @dealer_name.setter
    def dealer_name(self, wombat):
        if isinstance(wombat, str):
            # overwrite previous value
            self._dealer_name = wombat
        else:
            raise TypeError("Dealer must be a str")

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return "{}({})".format(my_name, len(self))

    def spam(self):
        print("Hooray! Class is almost over!")
