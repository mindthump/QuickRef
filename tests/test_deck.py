import unittest
import copy
import BitVector
import sys, os
import inspect

# Some folderol to get this project's root on the path.
cmd_parent_folder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "..")))
if cmd_parent_folder not in sys.path:
    sys.path.insert(0, cmd_parent_folder)
from Deck import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.test_deck = Deck()
        # Make a copy so we have something to compare.
        self.original_deck = copy.copy(self.test_deck.cards)
        self.stack = ['8C', 'KH', '3S', 'TD', '2C', '7H', '9S', '5D', 'QC', '4H', 'AS', '6D', 'JC', '8H', 'KS', '3D', 'TC',
                 '2H', '7S', '9D', '5C', 'QH', '4S', 'AD', '6C', 'JH', '8S', 'KD', '3C', 'TH', '2S', '7D', '9C', '5H',
                 'QS', '4D', 'AC', '6H', 'JS', '8D', 'KC', '3H', 'TS', '2D', '7C', '9H', '5S', 'QD', '4C', 'AH', '6S',
                 'JD']
        self.FULL_DECK = "1111111111111111111111111111111111111111111111111111"

    def test_shuffle(self):
        """ Shuffling the deck. All cards should be accounted for, but not in the same order.
        """
        self.test_deck.shuffle()
        # Make sure the shuffle happened (the decks are not equal)
        self.assertNotEqual(self.original_deck, self.test_deck.cards)
        # Show all the cards are still there
        self.assertEqual(self.account_for_cards(), self.FULL_DECK)

    def account_for_cards(self):
        # Account for each card in the current deck compared to the original, using a BitVector
        deck_bitvector = BitVector.BitVector(size=len(self.original_deck))
        for y in self.test_deck.cards:
            deck_bitvector[self.original_deck.index(y)] = 1
        return str(deck_bitvector)

    def test_stacked_deck(self):
        self.test_deck.stack_the_deck()
        self.assertListEqual(self.test_deck.cards, self.stack)

    def test_dealing(self):
        """ Use a stacked deck so we know the correct order
        """
        # The post-deal comparison would need to be adjusted for different hand sizes!
        HAND_SIZE = 7
        POST_DEAL = "1011111011111111111011111011011111011111111111110111"
        initial_deck_size = len(self.test_deck.cards)
        self.test_deck.stack_the_deck()
        hand = []
        for card in range(HAND_SIZE):
            hand.append(self.test_deck.deal_one_card())
        self.assertEqual(hand, self.stack[0:HAND_SIZE])
        remaining_cards = initial_deck_size - HAND_SIZE
        self.assertEqual(len(self.test_deck.cards), remaining_cards)
        # Show the dealt cards are now missing.
        self.assertEqual(self.account_for_cards(), POST_DEAL)
        # TODO: Test _where_ the cards are replaced
        self.test_deck.replace_cards_in_deck(hand)
        self.assertEqual(self.account_for_cards(), self.FULL_DECK)


# This lets you run the tests on the command line
if __name__ == '__main__':
    unittest.main()