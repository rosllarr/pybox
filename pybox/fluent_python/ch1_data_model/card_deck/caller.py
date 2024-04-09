from pprint import pprint

from french_deck import FrenchDeck, spades_high


deck = FrenchDeck()

pprint(deck.__dict__)

for card in sorted(deck, key=spades_high):
    pprint(card)
