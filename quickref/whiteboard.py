""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time."""

import os, sys
import pprint
import collections


def main():
    import doctest
    doctest.testmod(verbose=True)


class Solution:
    def __init__(self, someparam):
        self.some_class_param = someparam
        pass

    @classmethod
    def elgoog(self, reverse_string):
        """Calling a class method
        >>> Solution.elgoog("GOOGLE")
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

    def count_unique(self, m):
        """Counting unique items in an iterable
        Super useful for doctests: pprint orders dict by the keys!
        >>> pprint.pprint(dict(Solution('x').count_unique("GOOGLE")))
        {'E': 1, 'G': 2, 'L': 1, 'O': 2}

        :return: unique list
        """
        d = collections.Counter()
        for letter in m:
            d[letter] += 1
        return d


if __name__ == '__main__':
    sys.exit(main())