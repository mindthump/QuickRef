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
        """ A tuple literal
        """
        t = ("Echo", "November", "Victor")
        self.assertEqual(significant(t), "Foxtrot Oscar Whiskey : and 'else' was executed.")

    def test_unique(self):
        # Nested function
        def create_test_file(filename):
            """This creates a small file with repeated lines
            for methods finding unique lines
            DEMONSTRATES: writing to files in a context manager, multi-line strings
            """
            with open(filename, mode='w') as fw:
                fw.write("""klasdflhf
sdfdsf
asdfasdf
asfd
asdfasdf
klasdflhf
asfd
sdfdsf""")

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
        pass

    def process_file_with_generators(self):
        pass

    def test_elgoog(self):
        pass

    def test_count_unique(self):
        pass

    def test_constant_factory(self):
        d = collections.defaultdict(lambda: '<missing>')
        d.update(name='John', action='ran')
        # This also shows unpacking a dict for str.format()
        result = "{name} {action} to {object}".format(**d)
        self.failIf(result != 'John ran to <missing>')
