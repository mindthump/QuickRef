""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time."""

import os
import sys
import pprint
import collections
import re
import doctest


filename = "/Users/ed/lorem.txt"


def main():
    doctest.testmod(verbose=True)


def constant_factory(value):
    """
    Using a defaultdict with a constant for missing values
    '%(name)s %(action)s to %(object)s' % d
    >>> d = collections.defaultdict(constant_factory('<missing>')); \
    d.update(name='John', action='ran'); \
    "{name} {action} to {object}".format(**d)
    'John ran to <missing>'
    """
    return lambda: value


def unique_via_comp():
    """
    Dictionaries are output by pprint in key order. The options are to keep the output on one line.
    >>> pprint.pprint(dict(unique_via_comp()), compact=True, width=999999)
    {'ac': 7, 'arcu': 7, 'eget': 10, 'et': 10, 'in': 11, 'mauris': 7, 'nec': 8, 'non': 7, 'vel': 8}

    """
    c = collections.Counter()
    with open(filename) as f:
        for l in f:
            w = re.findall(r"[\w']+", l)
            c.update(w)
    # These must be a way to avoid these from being collected
    del c['']
    return c.most_common(9)


if __name__ == '__main__':

    pprint.pprint(['{} = "{}"'.format(k, v) for k, v in os.environ.items()], width=99)

    sys.exit(main())