from unittest import TestCase
from quickref import *


# Create some useful variables for tests.
food_list = [['apples', 'bananas', 'oranges'], ['hamburgers', 'pizza', 'tacos'],
             ['grasshoppers', 'horse', 'eels'], 27.0345, function_reference]
test_file_data = """klasdflhf
sdfdsf
asdfasdf
asfd
asdfasdf
klasdflhf
asfd
sdfdsf"""


class TestQuickref(TestCase):
    def test_string_demo(self):
        """
        """
        self.assertEqual(string_demo('Ed'), "Welcome to Ed's World!!!")

    def test_filtered_list(self):
        self.assertListEqual(filtered_list(food_list), ['apples', 'grasshoppers', 'hamburgers'])

    def test_zipping(self):
        """
        """
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
        """
        A variable can hold a function reference, and it is called when it looks like a function
        (i.e., with parenthesis and signature-appropriate arguments)
        """
        self.assertEqual(food_list[4](32, 76), "32 plus 76 equals 108")

    def test_phonetics(self):
        """
        """
        self.assertEqual(phonetics('L'), 'Lima')
        self.assertEqual(phonetics('%'), '$$ ERROR: character not found.')

    def test_significant(self):
        """ A tuple literal
        """
        t = ("Echo", "November", "Victor")
        self.assertEqual(significant(t), "Foxtrot Oscar Whiskey : and 'else' was executed.")

    def test_unique(self):
        # Nested function
        def create_test_file(create_file_name):
            """This creates a small file with repeated lines
            for methods finding unique lines
            DEMONSTRATES: writing to files in a context manager, multi-line strings
            """
            with open(create_file_name, mode='w') as fw:
                fw.write(test_file_data)
        filename = "test.txt"
        create_test_file(filename)
        self.assertEqual(unique(filename), "asdfasdf asfd klasdflhf sdfdsf")
        os.remove(filename)
        unique(filename)
        self.assertEqual(unique(filename), "File {} not found.".format(filename))

    def test_encode_rownum(self):
        self.assertEqual(encode_rownum(62), '10')
        self.assertEqual(encode_rownum(1234567), '5ban')
        self.assertEqual(encode_rownum(0), '0')

    def test_decode_url(self):
        self.assertEqual(decode_url('10'), 62)
        self.assertEqual(decode_url('5ban'), 1234567)
        self.assertEqual(decode_url('0'), 0)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(), "0 1 1 2 3 5 8 13 21 34 55 89")

    def test_permute(self):
        permute(4, list("ABCD"))

    def test_subprocess_ls(self):
        pass

    def test_walkies(self):
        d = walkies(".")

    def process_file_with_generators(self):
        pass

    def test_elgoog(self):
        self.assertEqual(elgoog("GOOGLE"), "ELGOOG|ELGOOG|ELGOOG|ELGOOG|ELGOOG|ELGOOG")

    def test_count_unique(self):
        """
        """
        self.assertDictEqual(count_unique("GOOGLE"), {'E': 1, 'G': 2, 'L': 1, 'O': 2})

    def test_unique_via_comp(self):
        """ Dictionaries are output by pprint in key order. The options are to keep the output on one line.
        """
        self.assertEqual("{'ac': 7, 'arcu': 7, 'eget': 10, 'et': 10, 'in': 11, 'mauris': 7, 'nec': 8, 'non': 7, 'vel': 8}",
                         pprint.pformat(dict(unique_via_comp("../data/lorem.txt")), width=999999))

    def test_default_dict(self):
        """ Note: This test is stand-alone, it has no part in quickref.py
        DEMONSTRATES: collections.defaultdict()
        """
        # defaultdict takes a callable, which is called with no parameters
        d = collections.defaultdict(lambda: '<missing>')
        d.update(name='John', action='ran')
        result = "{0[name]} {0[action]} to {0[object]}".format(d)
        self.failIf(result != 'John ran to <missing>')

    def test_templates(self):
        """
        Use string Templates
        :return:
        """
        sentence = "My oak is a mighty oak."
        (full_sub, partial_sub) = template_substitute("oak", "mighty")
        self.assertEquals(full_sub, sentence)
        self.assertEquals(partial_sub, sentence)