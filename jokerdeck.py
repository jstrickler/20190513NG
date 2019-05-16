#!/usr/bin/env python

from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        self._cards.append(('Joker', 1))
        self._cards.append(('Joker', 2))

