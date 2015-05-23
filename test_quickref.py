from unittest import TestCase
from quickref import *


# Create some useful variables for tests.
food_list = [['apples', 'bananas', 'oranges'], ['hamburgers', 'pizza', 'tacos'],
        ['grasshoppers', 'horse', 'eels'], 27.0345, function_reference]


class TestQuickref(TestCase):

    def test_string_demo(self):
        """
        """
        self.assertEqual(string_demo('Ed'), "Welcome to Ed's World!!!")

    def test_filtered_list(self):
        self.assertListEqual(filtered_list(food_list), ['apples', 'grasshoppers', 'hamburgers'])

    def test_zipping(self):
        food_types = ['fruit', 'meals', 'weird']
        expected_result = {
            'fruit': ['apples', 'bananas', 'oranges'],
            'meals': ['hamburgers', 'pizza', 'tacos'],
            'weird': ['grasshoppers', 'horse', 'eels']}
        x = zipping(food_types, food_list)
        self.assertEqual(len(x), len(expected_result))
        for k, v in x.items():
            self.assertListEqual(v, expected_result[k])

    def test_use_function_reference(self):
        # a variable can hold a function reference, and it is called when it looks like a function
        # (i.e., with parenthesis and signature-appropriate arguments)
        self.assertEqual(food_list[4](32, 76), "32 plus 76 equals 108")

    def test_phonetics(self):
        """
        """
        self.assertEqual(phonetics('L'), 'Lima')
        self.assertEqual(phonetics('%'), '$$ ERROR: character not found.')

    def test_significant(self):
        """     >>> significant()
        Here is where we do stuff with the Foxtrot
        Here is where we do stuff with the Oscar
        Here is where we do stuff with the Whiskey
        'else' is executed when a 'for' loop finishes without a 'break'.
        """
        pass

    def test_unique(self):
        pass

    def test_encode_rownum(self):
        pass

    def test_decode_url(self):
        pass

    def test_fibonacci(self):
        pass

    def test_permute(self):
        pass

    def test_subprocess_ls(self):
        pass

    def test_walkies(self):
        pass

    def process_file_with_generators(self):
        pass

    def test_elgoog(self):
        pass

    def test_count_unique(self):
        pass
