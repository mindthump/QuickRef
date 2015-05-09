""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time.

>>> deck = Solution()
>>> deck.deal() # doctest: +ELLIPSIS
Unshuffled:
...
Shuffled:
...

"""

from BitVector import BitVector
import random
import copy


class Solution:

    def __init__(self):
        self.deck = []
        self.stack = ['8', 'K', '3', '10', '2', '7', '9', '5', 'Q', '4', 'A', '6', 'J']
        for suit in "CHSD":
            self.deck.append("A" + suit)
            for pip in range(2,11):
                self.deck.append(str(pip) + suit)
            for pip in "JQK":
                self.deck.append(str(pip) + suit)

    def deal(self):
        print("Unshuffled:")
        print(self.deck)
        shuffled = copy.copy(self.deck)
        random.shuffle(shuffled)
        print("Shuffled:")
        print(shuffled)
        dbv = BitVector(size = 52)
        for y in shuffled:
            dbv[self.deck.index(y)] = 1
            print(dbv)


if __name__ == '__main__':
    deck = Solution()
    deck.deal()