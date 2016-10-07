from __future__ import print_function
import this
from collections import defaultdict, namedtuple
# Don't do this: from utilities import *
from utilities import commit_changesets, generate_fake_table_row

panagram = "Mr. Jock, TV quiz PhD, bags few lynx."

print('--------------------')

# What kinds of objects are in bingo?
bingo = [('a', 1), ('b', 2), ('a', 3), ('c', 2), ('b', 5), ('b', 5)]
print("bingo has {} elements.".format(len(bingo)))
print(type(bingo[0]))
bingo[2] = ('a', 7)
print(bingo)

# Why is this useless?
# blah = tuple()
blah = (5, 6, 7, "gort", bingo)
try:
    # Even my IDE knows this is an error
    blah[2] = 15
except TypeError as te:
    print("Tuples are immutable, they only support count and index.")

# Must use the set function, [] () {} constructors are all taken
bongo = set()
# This is useless, like an empty tuple constructor:
# bango = frozenset()
for b in bingo:
    bongo.add(b)
# Same result: bongo = set(bingo)
print("bongo has {} elements, all unique.".format(len(bongo)))

try:
    bongo[2] = ('a', 7)
except TypeError as te:
    # Sets are mutable, but you can't assign to a particular
    # set item... you need to let the set handle it with add.
    print("Can't assign to an item in a set, use add().")

for t in generate_fake_table_row():
    print(t)

# Why does mutability matter?

print('--------------------')

some_data = {'y': "One", 'z': "Two"}
print(some_data)
try:
    bad = some_data['x']
except KeyError as ke:
    print("No such key: {}".format(ke.message))
# Default can be almost anything
better = some_data.get('x', "OK")
print("x is now {}".format(better))

print('--------------------')

# Default is an empty list
foo = defaultdict(list)
for k, v in bingo:
    foo[k].append(v)
print(foo)
print(foo['x'])

print('--------------------')

# Falsey-ness
x = "All of these are false."
if [] or {} or set() or () or "" or 0 or None or False:
    x = "At least one of these is true."
print(x)

a_boolean = 1 == 0
if a_boolean:
    print("a_boolean is True")
else:
    print("a_boolean is False")

print('--------------------')

commit_ids = ['74e041d3', '3bea427e', 'd1dbc75']
Gerrit = namedtuple('Gerrit', 'changeid commitid')
gerrits = []

for commit in commit_ids or []:
    # if commit_ids is "falsey", it's not iterable!
    gerrit_change_number = commit_changesets(commit)
    if gerrit_change_number:
        gerrits.append(Gerrit(changeid=gerrit_change_number, commitid=commit))
        # gerrits.append(Gerrit(gerrit_change_number, commit))
print(gerrits)
for gerrit in gerrits:
    print("Change '{}' is commit '{}'".format(gerrit.changeid, gerrit.commitid))

print('--------------------')


def total(p1, p2):
    """
    Showing a function reference in a list
    :param p1:
    :param p2:
    :return:
    """
    return p1 + p2


x = [7, 3, total]


def totalizer(args):
    return args[2](args[0], args[1])


print(totalizer(x))

print('--------------------')

x = "good"
y = "string"
print("This is " + x)
print("This is a %s %s" % (x, y))
print("This is a {} {}".format(x, y))
print("This is a {adjective} {noun}".format(adjective=x, noun=y))
d = {'noun': y, 'adjective': x}
print("This is a {adjective} {noun}".format(**d))

long_message = """This is a very\n{} multi-line {} with
{} formatting.""".format(x, y, 'complex')
print(long_message)
