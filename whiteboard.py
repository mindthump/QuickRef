""" This 'whiteboard' file is for experimentation and concept validation only; it can change at any time.

Regular Expressions
Manipulating files

"""
import pprint
import subprocess
from datetime import date
import os


class Solution:
    def __init__(self):
        pass

    def subprocess_ls(self):
        foo = subprocess.check_output(['ls', '-l'])
        x = foo.split("\n")
        pprint.pprint(x)

    def walkies(self):
        for path, dirs, files in os.walk(os.path.abspath(os.path.join(os.getcwd(), os.pardir))):
            pass

    def process_file_with_generators(self):
        with open("/Users/ed/Google Drive/test_data.csv") as data_file:
            first_col = (line.split(',')[0] for line in data_file)
            middle = (line.split('-')[2] for line in first_col)
            for index, value in enumerate(middle):
                print "{}: {}".format(index, value)


if __name__ == '__main__':
    s = Solution()
    s.process_file_with_generators()