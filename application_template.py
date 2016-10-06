# coding=utf-8
"""A Template Application"""
from __future__ import print_function
import sys
import os
import argparse
# For debugging
import pprint


# from _version import __version__
__version__ = '0.0n'

def main(raw_parameters):
    """
    The main should do the 'construction' setup...
    - construct basic objects (including the app object)
    - resource allocation (files, network, outside apps)
    - process configuration (config files, complex param processing)
    ... then launch the application
    """
    # pprint.pprint(raw_parameters)
    app = Application(parse_arguments(raw_parameters))
    status = app.run()
    return status


def parse_arguments(app_args):
    parser = argparse.ArgumentParser(prog='Template', description='Do something useful.')
    parser.add_argument('-c', '--count', action='store', type=int, help="Some number", default=3)
    parser.add_argument('-n', '--name', action='store', help="Your name", default='Sam')
    parser.add_argument('-f', '--flag', action='store_true', help="A flag, true if specified")
    parser.add_argument('-v', '--verbose', action='store_true', help="Outputs informational messages")
    parser.add_argument('--version', action='version', version='%(prog)s, version {}'.format(__version__))
    return parser.parse_args(app_args)


class Application(object):
    """
    This is the real working part
    """

    def __init__(self, init_parameters):
        """ This is the docstring for the function """
        # For reporting the exit code, could be set anywhere
        self.app_status = 0
        self.count = init_parameters.count
        self.name = init_parameters.name
        self.flag = init_parameters.flag
        self.verbose = init_parameters.verbose

    def run(self):
        """
        Create application objects, process as needed,
        maybe sit in an event loop, whatever.
        :return:
        """
        print("Welcome to {name}'s".format(name=self.name) + " World" + '!' * int(self.count))
        return self.app_status

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
