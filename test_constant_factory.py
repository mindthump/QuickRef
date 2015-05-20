from unittest import TestCase
import collections
from whiteboard import constant_factory

__author__ = 'ed'


class TestConstant_factory(TestCase):
    def test_constant_factory(self):
        d = collections.defaultdict(constant_factory('<missing>'))
        d.update(name='John', action='ran')
        result = "{name} {action} to {object}".format(**d)
        self.failIf(result != 'John ran to <missing>')
