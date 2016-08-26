from __future__ import print_function
from random import choice, randint
from string import ascii_uppercase
import uuid

# For later demos
# What does this return?
def commit_changesets(commit_id):
    return "I{}".format(commit_id[::-1])

# Tuple Generator
def generate_fake_table_row():
    k = 0
    while k <= 10:
        k += 1
        c = uuid.uuid4()
        a = ''.join(choice(ascii_uppercase) for i in range(5))
        b = randint(1, 1000)
        yield (k, a, b, c)

