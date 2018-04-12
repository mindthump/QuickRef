#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
import sys
import os
import logging.handlers
import argparse
import pprint
import traceback
import shelve
import uuid
import json
import random
import inspect
import datetime

# from _version import __version__
__version__ = '0.0n'


class ApplicationName(object):
    """
    Override parse_arguments and run(), implement super()
    """

    def __init__(self, init_parameters):
        """
        This is the docstring for the function.
        Make parameters into fields, get the DB, etc.
        This assumes every subclass needs the DB.
        :param init_parameters:
        """
        # For reporting the exit code, could be set anywhere
        self.app_status = 0
        self.logger = logging.getLogger('ApplicationName')
        self.parser = argparse.ArgumentParser(description='An application.')
        self.args = self.parse_app_arguments(init_parameters)
        self.setup_logging()
        # TODO: Use Mongo or Cassandra.
        self.db = shelve.open('ApplicationName.dbm')

    def __del__(self):
        if hasattr(self, 'db'):
            self.db.close()

    def parse_app_arguments(self, app_args):
        """
        Override this if necessary
        :param app_args: raw argument list
        :return: parsed arguments Namespace
        """
        self.parser.add_argument('--silent', action='store_true')
        self.parser.add_argument('--verbose', action='store_true')
        self.parser.add_argument('--debug', action='store_true')
        self.parser.add_argument('-c', '--count', action='store', type=int, help="Some number", default=3)
        self.parser.add_argument('-f', '--flag', action='store_true', help="A flag, true if specified")
        self.parser.add_argument('--version', action='version', version='%(prog)s, version {}'.format(__version__))
        self.additional_arguments()
        return self.parser.parse_args(app_args)

    def additional_arguments(self):
        """
        OVERRIDE THIS!!
        """
        self.parser.add_argument('--name', action='store', default='Sam')

    def setup_logging(self):
        """
        Set up logging for this and imported modules.
        """
        # This needs to be at the 'lowest' level.
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(u'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Console
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        # File
        logfile = os.path.realpath(os.path.abspath(os.path.join(os.path.split(__file__)[0], 'ApplicationName.log')))
        # Specifying an encoding keeps it from converting line endings on Windows
        fh = logging.FileHandler(logfile, encoding='utf-8')
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        if self.args.silent:
            # Only silent on the console
            ch.setLevel(logging.ERROR)
        if self.args.verbose:
            ch.setLevel(logging.INFO)
            fh.setLevel(logging.DEBUG)
        # Overrides verbose
        if self.args.debug:
            ch.setLevel(logging.DEBUG)
            fh.setLevel(logging.DEBUG)

    def execute_common_action(self, values):
        """
        Some action common to all cubclasses.
        :param values:
        :return:
        """
        situation = "Running {app}#{method} \n... with {values}".format(
            app=self.__class__.__name__,
            method=inspect.currentframe().f_code.co_name,
            values=values)
        self.logger.debug(situation)
        _id = uuid.uuid4().hex
        self.db[_id] = values
        return _id

    def dump_db(self, row_format_fn):
        """
        Simple dump of DB rows, flexible through a passed
        function to perform the formatting.
        :param row_format_fn:
        :return:
        """
        for row_id, row_val in self.db.iteritems():
            dumped = row_format_fn(row_val)
            self.logger.debug("{r}: {v}".format(r=row_id[:7], v=dumped))
        return None

    def run(self):
        """
        OVERRIDE THIS!!
        :return:
        """
        self.logger.info(u"Args: {}".format(self.args))
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
        new_row = self.execute_common_action(json.dumps([now, random.randint(0, 10)]))
        self.logger.warn("New row: {}".format(new_row))
        self.dump_db(lambda r: pprint.pformat(json.loads(r)))

        return 0


if __name__ == "__main__":
    # Setup and run the application
    raw_parameters = sys.argv[1:]
    # pprint.pprint(raw_parameters)
    app = ApplicationName(raw_parameters)
    result = app.run()
    sys.exit(result)
