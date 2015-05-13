# ! /usr/bin/env python
"""An example Python script
"""

import sys
import os
import doctest
import random
import copy
import subprocess
import pprint
import BitVector
import collections


def main():
    doctest.testmod(verbose=True)

# Create some useful variables for tests.
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
phonetic_alphabet = """Alpha Bravo Charlie Delta
Echo Foxtrot Golf Hotel India
Juliet Kilo Lima Mike
November Oscar Papa Queen
Romeo Sierra Tango Uniform
Victor Whiskey X-ray Yankee Zulu"""

# A deck of cards, each represented by a suit and a rank character.
# The deck is originally in standard new-deck sort order.
deck = []
# For "Eight Kings Chased" setup
# stack = ['8', 'K', '3', '10', '2', '7', '9', '5', 'Q', '4', 'A', '6', 'J']
for suit in "CHSD":
    deck.append("A" + suit)
    for rank in range(2, 11):
        deck.append(str(rank) + suit)
    for rank in "JQK":
        deck.append(str(rank) + suit)


def create_test_file(filename):
    """This creates a small file with repeated lines
    for methods finding unique lines
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


def demo(parameter):
    """Some basic demos.
    >>> demo('Ed')
    Welcome to Ed's World!!!
    ['apples', 'grasshoppers', 'hamburgers']
    {'fruit': ['apples', 'bananas', 'oranges'],
     'meals': ['hamburgers', 'pizza', 'tacos'],
     'weird': ['grasshoppers', 'horse', 'eels']}
    32 plus 76 equals 108
    Result 108 is over one hundred
    """

    # Mixed single/double quote, formatting, concatenation, repetition.
    print("Welcome to {name}'s".format(name=parameter) + " World" + '!' * 3)

    # Lists and dicts can hold non-homogeneous types, including function references
    food = [['apples', 'bananas', 'oranges'], ['hamburgers', 'pizza', 'tacos'],
            ['grasshoppers', 'horse', 'eels'], 27.0345, function_reference]

    # list comprehension w/filter clause, using the element's type
    print(sorted([element[0] for element in food if type(element) is list]))

    # Interweaving elements with zip(), coerced to a dictionary
    food_types = ['fruit', 'meals', 'weird']
    food_dict = dict(zip(food_types, food))
    pprint.pprint(food_dict)

    # a variable can hold a function reference, and it is called when it looks like a function
    # (i.e., with parenthesis and signature-appropriate arguments)
    food[4](32, 76)


def function_reference(param1, param2):
    """This function appears as a reference buried in a list in demo()
    """
    results = param1 + param2
    print("{0} plus {2} equals {1}".format(param1, results, param2))  # nameless but ordered
    x = "is" if results > 100 else "is not"  # trinary(ish)
    print("Result %s %s over one hundred" % (results, x))  # old-style needs a tuple


def phonetics(character):
    """Mangling lines; dict comprehension.
    >>> phonetics('L')
    'Lima'
    >>> phonetics('%')
    '$$ ERROR: character not found.'
    """
    phonetics = []
    # Rip the lines themselves apart...
    for line in phonetic_alphabet.splitlines():
        # ...then rip apart the words on each line
        phonetics.extend(line.split())
    # Pack it all into a dict
    translation = {alphabet[x]: phonetics[x - 36] for x in range(36, 62)}
    # Using try/except to catch a KeyError; could also use dict.get() or a defaultdict to supply a default value
    try:
        c = translation[character]
        return c
    except KeyError:
        return '$$ ERROR: character not found.'


def significant():
    """Do stuff with the second word in 'significant' lines: comprehensions with conditionals.
    >>> significant()
    Here is where we do stuff with the Foxtrot
    Here is where we do stuff with the Oscar
    Here is where we do stuff with the Whiskey
    'else' is executed when a 'for' loop finishes without a 'break'.
    """
    for word in [x.split()[1] for x in phonetic_alphabet.splitlines() if
                 x.split()[0] in ("Echo", "November", "Victor")]:
        print("Here is where we do stuff with the {}".format(word))
    else:
        print("'else' is executed when a 'for' loop finishes without a 'break'.")


def unique(filename):
    """Simple file I/O, and using a set to eliminate duplicates.
    Test exception for missing file.
    Also, this is a static method since it doesn't actually refer to any class stuff.
    >>> filename = "test.txt"; create_test_file(filename); unique(filename)
    ['asdfasdf', 'asfd', 'klasdflhf', 'sdfdsf']
    >>> os.remove(filename); unique(filename) # doctest: +ELLIPSIS
    File ... not found.
    """
    try:
        with open(os.path.join(os.getcwd(), filename), 'r') as fr:
            ulines = {line.strip() for line in fr}
        pprint.pprint(sorted(ulines))
    except IOError:
        print("File {fn} not found.".format(fn=filename))


def encode_rownum(row_number_to_encode):
    """encode_rownum() and decode_url() functions could be used in a URL shortener, essentially base62 encoding
    >>> encode_rownum(62)
    '10'
    >>> encode_rownum(1234567)
    '5ban'
    >>> encode_rownum(0)
    '0'
    """
    if row_number_to_encode == 0:
        return '0'
    encoded_url = ''
    base = len(alphabet)
    while row_number_to_encode:
        q, r = divmod(row_number_to_encode, base)
        # str() in case something "looks" numeric
        # prepend the encoded_url char so it's easier to decode
        encoded_url = str(alphabet[r]) + str(encoded_url)
        row_number_to_encode = q
    return encoded_url


def decode_url(str_to_decode):
    """Inverse of encode_rownum()
    >>> decode_url('5ban')
    1234567
    >>> decode_url('10')
    62
    >>> decode_url('0')
    0

    :param str_to_decode: the shortened URL (or whatever)
    :return: row number
    """
    i = 0
    rownum = 0
    while len(str_to_decode):
        char_to_decode = str_to_decode[-1]
        str_to_decode = str_to_decode[0:-1]
        idx = alphabet.index(char_to_decode)
        rownum += (pow(62, i) * idx)
        i += 1
    return rownum


def fibonacci():
    """Use the fibonacci_generator() to get one element at a time.
    >>> fibonacci()
    0 1 1 2 3 5 8 13 21 34 55 89
    """
    outstr = ''
    for f in fibonacci_generator():
        if f <= 100:
            outstr += str(f) + ' '
        else:
            break
    print(outstr.strip())  # remove trailing space


def fibonacci_generator():
    """Returns next number in fibonacci series."""
    n = 0
    prev = 1  # a trick to bootstrap the series
    while True:
        yield n
        prev, n = n, prev + n  # sweet swap trick


def permute(n, array):
    """Permutations using Heap's Algorithm.
    >>> permute(4, list("ABCD")) # doctest: +ELLIPSIS
    ABCD
    BACD
    ...
    BDAC
    DBAC
    ABDC
    BADC
    """
    if n == 1:
        print(''.join(array))
    else:
        for i in range(0, n):
            # Recurse, permuting the first through (n-1)th elements
            permute(n - 1, array)
            # Swap with nth element: ith element if even, first element if odd
            j = i if (n % 2 == 0) else 0
            # Cool python swap trick
            array[j], array[n - 1] = array[n - 1], array[j]


def get_shuffled_deck():
    """Deal out and track cards from a shuffled deck.
    Can't match a shuffled deck, but we can verify all of the cards are there with a BitVector
    >>> get_shuffled_deck() # doctest: +ELLIPSIS
    Unshuffled:
    ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD']
    Shuffled:
    1111111111111111111111111111111111111111111111111111
    ...
    """
    print("Unshuffled:")
    print(deck)
    # Make a (shallow) copy so we don't shuffle the "template" deck.
    # shuffle() works in-place on an existing list, returns None
    shuffled = copy.copy(deck)
    random.shuffle(shuffled)
    print("Shuffled:")
    dbv = BitVector.BitVector(size=52)
    for y in shuffled:
        dbv[deck.index(y)] = 1
    print(dbv)
    return shuffled


def subprocess_ls():
    """Run a simple subprocess. the doctest is pretty stupid because 'ls' output is unpredictable.
    >>> subprocess_ls()  # doctest: +ELLIPSIS
    ['...'']
    """
    foo = subprocess.check_output(['ls', '-l'])
    x = foo.split("\n")
    pprint.pprint(x)


def walkies():
    """
    >>> d = walkies(); pprint.pprint(d) # doctest: +ELLIPSIS
    [('/Users/ed/PycharmProjects/QuickRef',
    ...

    :return: [(path, [dirs], [files]), ...]
    """
    contents = [x for x in os.walk(os.path.abspath(os.getcwd()))]
    return contents


def process_file_with_generators():
    """Look at generators expressions. I wish I had reviewed this more before the interview :(
    >>> process_file_with_generators() # doctest: +ELLIPSIS
    0: 4853
    1: 4991
    2: 4c82
    3: 462e
    4: 43b6
    5: 4d4c
    ...
    54: 4138
    55: 4ee3
    56: 4842
    57: 4205
    """
    with open("/Users/ed/Google Drive/test_data.csv") as data_file:
        # The inner generator breaks the line by commas and returns the first element,
        # the outer generator breaks that by dashes and returns the third element
        # The 'next' outers and inners are produced only when they are actually used
        inner = (line.split(',')[0] for line in data_file)
        outer = (line.split('-')[2] for line in inner)
        for index, value in enumerate(outer):
            print("{}: {}".format(index, value))


if __name__ == "__main__":
    sys.exit(main())