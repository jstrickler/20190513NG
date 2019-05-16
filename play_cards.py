#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

print(CardDeck)

# create new object d1
d1 = CardDeck("Zach")
# d1 is "self"

# bad programmer! no biscuit!
# print(d1._dealer_name)

# access a property
# (variable)
print(d1.dealer_name)

print(d1)

d1.dealer_name = "Freida"
# doing this:
# CardDeck.dealer_name(d1, "Fredia")

print(d1.dealer_name)

d2 = CardDeck("Franz")

d2.dealer = "Billy"

d1.shuffle()

print(d1.cards)

d2.shuffle()

for i in range(10):
    print(d1.draw())


print(d1.cards)

print(len(d1))
print(len(d2))


print(d1)
print(d2)

d1.spam()

print(d1.show_suits())
print(CardDeck.show_suits())
print('-' * 60)
j1 = JokerDeck("Jimmy")
j1.shuffle()
print(j1)
print(len(j1))
print(d1)
