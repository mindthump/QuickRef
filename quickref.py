""" An example Python script
"""

import sys
import os
import subprocess
import pprint
import collections
import re
import string

# "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = string.digits + string.ascii_letters

phonetic_alphabet = """Alpha Bravo Charlie Delta
Echo Foxtrot Golf Hotel India
Juliet Kilo Lima Mike
November Oscar Papa Queen
Romeo Sierra Tango Uniform
Victor Whiskey X-ray Yankee Zulu"""


def string_demo(parameter):
    """
    DEMONSTRATES: Mixed single/double quote, formatting, concatenation, repetition.
    """
    return "Welcome to {name}'s".format(name=parameter) + " World" + '!' * 3


def filtered_list(list_to_filter):
    """ Lists and dicts can hold non-homogeneous types, including function references
    DEMONSTRATES: List comprehension w/filter clause, using the element's type
    """
    return sorted([element[0] for element in list_to_filter if type(element) is list])


def zipping(type_list, items_list):
    """
    DEMONSTRATES: Interweaving elements with zip(), coerced to a dictionary.
    The iterator stops when the shortest input iterable is exhausted.
    """
    food_dict = zip(type_list, items_list)
    return dict(food_dict)


def function_reference(param1, param2):
    """
    DEMONSTRATES: a function reference buried in a list, old-style formatting
    """
    total = param1 + param2
    # trinary(ish)
    # x = "is" if total > 100 else "is not"
    # old-style formatting needs a tuple, but see process_file_with_generators() below
    return "%s plus %s equals %s" % (param1, param2, total)


def phonetics(character):
    """
    DEMONSTRATES: mangling strings; dict comprehension, try/catch.
    """
    phonetic_words = []
    # Rip the lines themselves apart...
    for line in phonetic_alphabet.splitlines():
        # ...then rip apart the words on each line
        phonetic_words.extend(line.split())
    # Pack it all into a dict
    translation = {alphabet[x]: phonetic_words[x - 36] for x in range(36, 62)}
    # Using try/except to catch a KeyError; could also use dict.get() or a defaultdict to supply a default value
    try:
        c = translation[character]
        return c
    except KeyError:
        return '$$ ERROR: character not found.'


def significant(s_list):
    """ Do stuff with the second word in 'significant' lines.
    DEMONSTRATES: comprehensions with conditionals, for/else.
    """
    result = ""
    for word in [x.split()[1] for x in phonetic_alphabet.splitlines() if
                 x.split()[0] in s_list]:
        result += word + " "
    else:
        result += ": and 'else' was executed."
    return result


def unique(filename):
    """ Unique rows in a file
    DEMONSTRATES: set comprehension to eliminate duplicates, simple file read, try/catch (missing file exception).
    """
    try:
        with open(os.path.join(os.getcwd(), filename), 'r') as fr:
            ulines = {line.strip() for line in fr}
        return " ".join(sorted(ulines))
    except IOError:
        return "File {fn} not found.".format(fn=filename)


def encode_rownum(row_number_to_encode):
    """ encode_rownum() and decode_url() functions could be used in a URL shortener, essentially base62 encoding
    DEMONSTRATES: recursion, divmod to get both integer quotient and remainder
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
    """ Inverse of encode_rownum()
    DEMONSTRATES: string indexing, power function
    """
    i = 0
    rownum = 0
    while len(str_to_decode):
        char_to_decode = str_to_decode[-1]
        str_to_decode = str_to_decode[:-1]
        idx = alphabet.index(char_to_decode)
        rownum += (pow(62, i) * idx)
        i += 1
    return rownum


def fibonacci():
    """ Use the fibonacci_generator() to get one element at a time.
    DEMONSTRATES: using generator functions
    """
    outstr = ''
    for f in fibonacci_generator():
        if f <= 100:
            outstr += str(f) + ' '
        else:
            break
    # remove trailing space
    return outstr.strip()


def fibonacci_generator():
    """ Returns next number in fibonacci series.
    DEMONSTRATES: generators (yield statement)
    """
    # a trick to bootstrap the series
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # sweet swap trick


def permute(n, array):
    """ Permutations using Heap's Algorithm.
    DEMONSTRATES: recursion, python no-temp swap trick
    ABCD
    BACD
    ...
    BDAC
    DBAC
    ABDC
    BADC
    """
    if n == 1:
        pass
        # TODO: yield? It seems to be very complex with recursion.
        # print(array)
    else:
        for i in range(0, n):
            # Recurse, permuting the first through (n-1)th elements
            permute(n - 1, array)
            # Swap with nth element: ith element if even, first element if odd
            j = i if (n % 2 == 0) else 0
            # Cool python swap trick, no temporary variable needed
            array[j], array[n - 1] = array[n - 1], array[j]


def subprocess_ls():
    """
    Run a simple subprocess. The test is meaningless
    because 'ls' output is unpredictable.
    Note: subprocess returns bytes (not str) unless "universal_newlines=True"
    DEMONSTRATES: subprocess (to run system commands).
    """
    foo = subprocess.check_output(['ls', '-l'], universal_newlines=True)
    x = foo.splitlines()
    pprint.pprint(x)


def walkies(root):
    """
    DEMONSTRATES: os.walk function, including "pruning"

    :return: [(path, [dirs], [files]), ...]
    """
    contents = []
    excluded_dirs = (".git", ".idea", "__pycache__",)
    # "tree" is a generator
    tree = os.walk(root, topdown=True)
    for root, dirs, files in tree:
        # Pruning: "list[:]" replaces the values, doesn't create a new list
        # With 'topdown=True', altering the "dirs" element changes what the next iteration searches
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        contents.append((root, dirs, files))
    return contents


def process_file_with_generators():
    """ Look at generators expressions. I wish I had reviewed this more before the interview :(
    DEMONSTRATES: generator expressions, print.format with tuple.
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
    with open("data/test_data.csv") as data_file:
        # The inner generator breaks the line by commas and returns the first element,
        # the outer generator breaks that by dashes and returns the third element
        # The 'next' outers and inners are produced only when they are actually used
        inner = (line.split(',')[0] for line in data_file)
        outer = (line.split('-')[2] for line in inner)  # Nested generator
        # Enumerate returns two values (index, value) but since we only supply
        # one variable name it is stored as a tuple. The new-style string format
        # requires the tuple to be unpacked with "*".
        for t in enumerate(outer):
            print("{}: {}".format(*t))


def elgoog(string_to_reverse):
    """ Multiple ways to reverse a string
    DEMONSTRATES: Negative count string slice, concatenation, slice into front
    """
    # These two approaches actually build strings, not a list of characters.
    # This is not optimal - it produces a new immutable string each time
    concat_before_start = ""
    for i in string_to_reverse:
        concat_before_start = i + concat_before_start
    # Much better, the string build happens internally.
    negative_slice = string_to_reverse[::-1]

    # Interesting: reversed() does not return a reversed string, but
    # rather a 'reversed iterator' instance!
    cheating = reversed(string_to_reverse)

    # We don't want to use a comprehension for this next approach.
    # Since each list.insert() actually returns None, you'd only
    # be using it for a side effect (a bad practice!).
    insert_at_front_of_list = []
    for i in string_to_reverse:
        # Produces list that need to be joined
        insert_at_front_of_list.insert(0, i)

    slice_into_front_of_list = []
    for i in string_to_reverse:
        # Produces list that need to be joined
        slice_into_front_of_list[:0] = i

    reverse_as_list = list(string_to_reverse)
    reverse_as_list.reverse()

    r1 = concat_before_start
    r2 = negative_slice
    r3 = ''.join(cheating)
    r4 = ''.join(insert_at_front_of_list)
    r5 = ''.join(slice_into_front_of_list)
    r6 = ''.join(reverse_as_list)
    return "{}|{}|{}|{}|{}|{}".format(r1, r2, r3, r4, r5, r6)


def count_unique(m):
    """ Counting unique items in an iterable
    DEMONSTRATES: collections.Counter (dict subclass)
    """
    # All items at once, what it was really created for
    d1 = collections.Counter(m)
    return dict(d1)
    # One item at a time
    # d2 = collections.Counter()
    # for letter in m:
    #     d2[letter] += 1
    # pprint.pprint(dict(d2))


def unique_via_comp(file_name):
    """
    """
    c = collections.Counter()
    with open(file_name) as f:
        for l in f:
            w = re.findall(r"[\w']+", l)
            c.update(w)
    # There must be a way to avoid these from being collected
    del c['']
    return c.most_common(9)


def template_substitute(noun, adjective):
    input = string.Template('My ${zzz} is a ${qqq} ${zzz}.')
    full = input.substitute({'zzz': noun, 'qqq': adjective})
    partial = string.Template(input.safe_substitute(zzz=noun))
    partial_completed = partial.substitute(qqq=adjective)
    return full, partial_completed


if __name__ == '__main__':
    sys.exit()
