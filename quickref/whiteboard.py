""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time.

# >>> q = Solution()
>>> Solution.elgoog("GOOGLE")
ELGOOG
ELGOOG
ELGOOG
"""
import pprint
import subprocess
from datetime import date
import os, sys


def main():
    import doctest
    doctest.testmod(verbose=True)


class Solution:
    def __init__(self):
        pass

    @classmethod
    def elgoog(self, reverse_string):
        """Calling a class method"""
        O = ""
        L = []
        print(reverse_string[::-1])
        for i in reverse_string:
            O = i + O
            L.insert(0, i)
        print(O)
        print(''.join(L))


if __name__ == '__main__':
    sys.exit(main())