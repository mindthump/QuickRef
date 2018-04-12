""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time."""

import os
import sys
import pprint
import collections
import re
import doctest


def main():
    # doctest.testmod(verbose=True)
    pprint.pprint(['{} = "{}"'.format(k, v) for k, v in os.environ.items()], width=99)


if __name__ == '__main__':

    sys.exit(main())
