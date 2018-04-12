import copy
import itertools
import random
import collections


class Deck(object):
    """ A deck of cards, each represented by a suit and a rank character.
    The deck is originally in standard new-deck sort order. Since cards are
    removed as they are dealt, they can run out; this is indicated by a
    'EmptyDeckError' exception. The user needs to replace the cards or
    re-initialize it during a shuffle.
    """

    def __init__(self):
        """ Make an new, unshuffled deck.
        DEMONSTRATES: nested list comprehension.
        """
        # We're assigning to the cards property
        self.cards = [rank + suit for suit in "CHSD" for rank in "A23456789TJQK"]

    def shuffle(self, new_deck=False):
        """ random.shuffle() works in-place on an existing list, returns None.
        This method shuffles the remaining cards or optionally creates a
        new deck (new_deck=True), so it's up to the deck consumer to replace the
        dealt cards or empty the player's "hands".
        DEMONSTRATES: random.shuffle; copy.copy, BitVectors (see unit test)
        """
        if new_deck:
            self.__init__()
        random.shuffle(self.cards)

    def deal_one_card(self):
        """ Remove a card from the deck and return its value. Users need to watch for an empty deck.
        """
        if len(self.cards) <= 0:
            raise EmptyDeckError("Cannot deal a card, the deck is empty.")
        # Take from the start/top of the deck, pop() default is the end/bottom
        return self.cards.pop(0)

    def replace_cards_in_deck(self, cards, position=None):
        """ Replace a list of cards in the deck at a particular position (zero: top, default/out of bounds: bottom)
        """
        if position:
            self.cards[:position] = cards
        else:
            self.cards.extend(cards)

    def stack_the_deck(self):
        """ BONUS! A card trick deck setup. Search for "eight kings chased" to see what it means.
        Stacking the deck always builds an entire deck!
        DEMONSTRATES: itertools.cycle, list.append.
        """
        stacked_deck = []
        suits = itertools.cycle("CHSD")
        ranks = itertools.cycle(['8', 'K', '3', 'T', '2', '7', '9', '5', 'Q', '4', 'A', '6', 'J'])
        for card in range(52):
            stacked_deck.append(str(next(ranks)) + str(next(suits)))
        self.cards = stacked_deck


class EmptyDeckError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
