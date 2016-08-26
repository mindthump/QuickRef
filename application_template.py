# coding=utf-8
"""A Template Application"""
from __future__ import print_function
import sys
import os
import argparse
# For debugging
import pprint

def main(raw_parameters):
    """
    The main should do the 'construction' setup...
    - construct basic objects (including the app object)
    - resource allocation (files, network, outside apps)
    - process configuration (config files, complex param processing)
    ... then launch the application
    """
    # pprint.pprint(raw_parameters)
    parsed_args = parse_arguments(raw_parameters)
    app = Application(parsed_args)
    return app.run()


def parse_arguments(app_args):
    parser = argparse.ArgumentParser(description='Do something useful.')
    parser.add_argument('-f', '--foo', action='store', type=int, default=3)
    parser.add_argument('-n', '--name', action='store', default='Sam')
    return parser.parse_args(app_args)


class Application(object):
    """
    This is the entry point for the real work
    """

    def __init__(self, init_parameters):
        """ This is the docstring for the function """
        self.foo = init_parameters.foo
        self.name = init_parameters.name

    def run(self):
        # Create application objects, process as needed,
        # maybe sit in an event loop, whatever.
        print("Welcome to {name}'s".format(name=self.name) + " World" + '!' * int(self.foo))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))