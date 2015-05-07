# ! /usr/bin/env python
"""An example Python script
>>> q = QuickRef('argument value')
>>> q.param()
The value of the main function argument is 'argument value'
>>> q.phonetics()
{'A': 'Alpha', 'C': 'Charlie', 'B': 'Bravo', 'E': 'Echo', 'D': 'Delta', 'G': 'Golf', 'F': 'Foxtrot', 'I': 'India', 'H': 'Hotel', 'K': 'Kilo', 'J': 'Juliet', 'M': 'Mike', 'L': 'Lima', 'O': 'Oscar', 'N': 'November', 'Q': 'Queen', 'P': 'Papa', 'S': 'Sierra', 'R': 'Romeo', 'U': 'Uniform', 'T': 'Tango', 'W': 'Whiskey', 'V': 'Victor', 'Y': 'Yankee', 'X': 'X-ray', 'Z': 'Zulu'}
>>> q.significant()
Here is where we do stuff with the Foxtrot
Here is where we do stuff with the Oscar
Here is where we do stuff with the Whiskey
'else' is executed when a 'for' loop finishes without a 'break'.
>>> q.traffic()
Traffic light yellow is #2
No 'blue' light.
>>> filename = "test.txt"
>>> q.unique(filename)
asfd
klasdflhf
asdfasdf
sdfdsf
>>> # Test catch of missing file
>>> os.remove(filename)
>>> q.unique(filename)
File test.txt not found.
>>> q.encode_rownum(62)
10
>>> q.encode_rownum(1234567)
5ban
>>> q.encode_rownum(0)
0
>>> q.decode_url('5ban')
1234567
>>> q.decode_url('10')
62
>>> q.decode_url('0')
0
>>> q.fibonacci()
0 1 1 2 3 5 8 13 21 34 55 89
>>> q.permute(3, list("ABC"))
ABC
BAC
CAB
ACB
BCA
CBA
>>> main('Ed')
Welcome to Ed's World!!!
['apples', 'hamburgers', 'grasshoppers']
{'weird': ['grasshoppers', 'horse', 'eels'], 'fruit': ['apples', 'bananas', 'oranges'], 'meals': ['hamburgers', 'pizza', 'tacos']}
32 plus 76 equals 108
Result 108 is over one hundred
"""

import sys, os  # load common libraries


def main(parameter):
    """Mixed single/double quote, formatting, concatenation, repetition."""
    print("Welcome to {name}'s".format(name=parameter) + " World" + '!' * 3)  # use print function
    food = [['apples', 'bananas', 'oranges'], ['hamburgers', 'pizza', 'tacos'],
            ['grasshoppers', 'horse', 'eels'], 27.0345, demo]  # list can hold other data types, incl. function refs
    print([element[0] for element in food if type(element) is list])  # list comprehension w/filter clause
    food_types = ['fruit', 'meals', 'weird']
    food_dict = dict(zip(food_types, food))  # interweave elements, coerce to dictionary
    print(food_dict)
    food[4](32, 76)  # a variable can hold a function reference


def demo(param1, param2):
    results = param1 + param2
    print("{0} plus {2} equals {1}".format(param1, results, param2))  # nameless but ordered
    x = "is" if results > 100 else "is not"  # trinary(ish)
    print("Result %s %s over one hundred" % (results, x))  # old-style needs a tuple


class QuickRef(object):
    def __init__(self, parameter):
        """Constructor for the class."""
        self.parameter = parameter
        self.phonetic_alphabet = """Alpha Bravo Charlie Delta
Echo Foxtrot Golf Hotel India
Juliet Kilo Lima Mike
November Oscar Papa Queen
Romeo Sierra Tango Uniform
Victor Whiskey X-ray Yankee Zulu"""
        self.traffic_light = {'red': 1, 'yellow': 2, 'green': 3}
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        with open("test.txt", mode='w') as fw:
            fw.write("""klasdflhf
sdfdsf
asdfasdf
asfd
asdfasdf
klasdflhf
asfd
sdfdsf""")

    def param(self):
        """Simple printing of the parameters."""
        print("The value of the main function argument is '{}'".format(self.parameter))

    def phonetics(self):
        """Mangling lines; dict comprehension."""
        phonetics = []
        for line in self.phonetic_alphabet.splitlines():
            phonetics += line.split()
        translation = {self.alphabet[x]: phonetics[x - 36] for x in range(36, 62)}
        print(translation)

    def significant(self):
        """Do stuff with the second word in 'significant' lines: comprehensions with conditionals."""
        for word in [x.split()[1] for x in self.phonetic_alphabet.splitlines() if
                     x.split()[0] in ("Echo", "November", "Victor")]:
            print("Here is where we do stuff with the {}".format(word))
        else:
            print("'else' is executed when a 'for' loop finishes without a 'break'.")

    def traffic(self):
        """Print formatting; traffic_light['blue'] raises KeyError."""
        print("Traffic light yellow is #{tl_num}".format(tl_num=self.traffic_light['yellow']))
        try:
            print(self.traffic_light['blue'])
        except KeyError:
            print("No 'blue' light.")

    def unique(self, filename):
        """Simple file I/O, and using a set to eliminate duplicates."""
        try:
            with open(filename, 'r') as fr:
                ulines = {line.strip() for line in fr}
            for l in ulines: print l  # single line is not idiomatic but sometimes useful
        except IOError:
            print "File {fn} not found.".format(fn=filename)

    def encode_rownum(self, rownum_to_encode):
        """encode_rownum() and decode_url() functions could be used in a URL shortener, essentially base62 encoding"""
        if rownum_to_encode == 0:
            return 0
        encoded_url = ''
        base = len(self.alphabet)
        while (rownum_to_encode):
            q, r = divmod(rownum_to_encode, base)
            # str() in case something "looks" numeric
            # prepend the encoded_url char so it's easier to decode
            encoded_url = str(self.alphabet[r]) + str(encoded_url)
            rownum_to_encode = q
        print(encoded_url)

    def decode_url(self, str_to_decode):
        i = 0
        rownum = 0
        while (len(str_to_decode)):
            char_to_decode = str_to_decode[-1]
            str_to_decode = str_to_decode[0:-1]
            idx = self.alphabet.index(char_to_decode)
            rownum += (pow(62, i) * idx)
            i += 1
        return rownum

    def fibonacci(self):
        """Use the fibonacci generator."""
        outstr = ''
        for f in self.fibonacci_generator():
            if f <= 100:
                outstr += str(f) + ' '
            else:
                break
        print outstr.strip()  # remove trailing space

    def fibonacci_generator(self):
        """Returns next number in fibonacci series."""
        n = 0
        prev = 1  # a trick to bootstrap the series
        while True:
            yield n
            prev, n = n, prev + n  # sweet swap trick

    def permute(self, n, array):
        """Permutations using Heap's Algorithm."""
        if n == 1:
            print(''.join(array))
        else:
            for i in range(0, n):
                # Recurse, permuting the first through (n-1)th elements
                self.permute(n - 1, array)
                # Swap with nth element: ith element if even, first element if odd
                j = i if (n % 2 == 0) else 0
                # Cool python swap trick
                array[j], array[n - 1] = array[n - 1], array[j]


if __name__ == "__main__":
    sys.exit(main('Ed'))


