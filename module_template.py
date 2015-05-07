# ! /usr/bin/env python
"""A Python script template
>>> x = Example(['Ed', 'Tom', 'Sam'])
>>> x.parameters
['Ed', 'Tom', 'Sam']
>>> x.welcome()
Welcome to Ed's World!!!
"""

import sys, os  # load common libraries

def main(parameter_list):
    print(parameter_list)

class Example(object):
    def __init__(self, parameters):
        """ This is the docstring for the function """
        self.parameters = parameters

    def welcome(self):
        name_param = self.parameters[0]
        print("Welcome to {name}'s".format(name=name_param) + " World" + '!' * 3)


if __name__ == "__main__":
    sys.exit(main(sys.argv))