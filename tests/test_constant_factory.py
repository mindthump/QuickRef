from unittest import TestCase
import collections
from quickref import constant_factory


class TestConstant_factory(TestCase):
    def test_constant_factory(self):
        d = collections.defaultdict(constant_factory('<missing>'))
        d.update(name='John', action='ran')
        # This also shows unpacking a dict for str.format()
        result = "{name} {action} to {object}".format(**d)
        self.failIf(result != 'John ran to <missing>')
