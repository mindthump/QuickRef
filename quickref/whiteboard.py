""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time."""

import os, sys
import pprint
import collections


def main():
    import doctest
    doctest.testmod(verbose=True)


def elgoog(reverse_string):
    """Calling a class method
    >>> elgoog("GOOGLE")
    ELGOOG
    ELGOOG
    ELGOOG
    """
    print(reverse_string[::-1])
    concat_before_start = ""
    as_list_insert_before_first = []
    for i in reverse_string:
        concat_before_start = i + concat_before_start
        as_list_insert_before_first.insert(0, i)
    print(concat_before_start)
    print(''.join(as_list_insert_before_first))

def count_unique(m):
    """Counting unique items in an iterable
    Super useful for doctests: pprint orders dict by the keys!
    >>> pprint.pprint(dict(count_unique("GOOGLE")))
    {'E': 1, 'G': 2, 'L': 1, 'O': 2}
    """
    d = collections.Counter()
    for letter in m:
        d[letter] += 1
    return d


if __name__ == '__main__':
    sys.exit(main())