# import numpy as np
# import re
# from math import sqrt, prod

##########
# Part 1 #
##########


def round(decks):
    if not (decks[0] and decks[1]):
        return decks[0] or decks[1]
    a, b = decks[0].pop(), decks[1].pop()
    if a > b:
        decks[0] = [b, a] + decks[0]
    else:
        decks[1] = [a, b] + decks[1]
    return round(decks)


with open('22.txt') as f:
    decks = [list(reversed([int(n) for n in deck.splitlines()[1:]]))
             for deck in f.read().split('\n\n')]

print(sum([(i+1)*c for i, c in enumerate(round(decks))]))

##########
# Part 2 #
##########


def game(decks):
    hands = set()
    while True:  # Apparently too many combinations to recurse through, so we loop.
        if str(decks) in hands:
            return True, decks[0]
        if not decks[1]:
            return True, decks[0]
        elif not decks[0]:
            return False, decks[1]
        hands |= {str(decks)}
        a, b = decks[0].pop(), decks[1].pop()
        if a > len(decks[0]) or b > len(decks[1]):
            a_wins = a > b
        else:
            a_wins, _ = game([decks[0][-a:], decks[1][-b:]])
        if a_wins:
            decks[0] = [b, a] + decks[0]
        else:
            decks[1] = [a, b] + decks[1]


with open('22.txt') as f:
    decks = [list(reversed([int(n) for n in deck.splitlines()[1:]]))
             for deck in f.read().split('\n\n')]

print(sum([(i+1)*c for i, c in enumerate(game(decks)[1])]))
