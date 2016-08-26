from __future__ import print_function
from collections import defaultdict, namedtuple
# Don't do this: from utilities import *
from utilities import commit_changesets, get_table_row

print('--------------------')

# What kinds of objects are in bingo?
bingo = [('a', 1), ('b', 2), ('a', 3), ('c', 2), ('b', 5), ('b', 5)]
print("bingo has {} elements".format(len(bingo)))
print(type(bingo[0]))
bingo[2] = ('a', 7)
print(bingo)

# Why is this useless?
# blah = tuple()
blah = (5, 6, 7, "gort", bingo)
try:
    blah[2] = 15
except TypeError as te:
    print("Tuples are immutable.")

# Must use the function! [] () {} are all taken
bongo = set()
for b in bingo:
    bongo.add(b)
# Same result: bongo = set(bingo)
print("bongo has {} elements".format(len(bongo)))

try:
    bongo[2] = ('a', 7)
except TypeError as te:
    print("Sets are also immutable.")

for t in get_table_row():
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

# Default is an emmpty list
foo = defaultdict(list)
for k, v in bingo:
    foo[k].append(v)
print(foo)
print(foo['x'])

print('--------------------')

# Falsey-ness
x = None
if [] or {} or set() or () or "" or 0 or None or False:
    x = True
print(x)

print('--------------------')

commit_ids = ['74e041d3', '3bea427e', 'd1dbc75']
gerrits = []
Gerrit = namedtuple('Gerrit', 'changeid commitid')

for commit_id in commit_ids or []:
    # if commit_ids is "falsey", it's not iterable!
    gerrit_change_number = commit_changesets(commit_id)
    if gerrit_change_number:
        gerrits.append(Gerrit(changeid=gerrit_change_number, commitid=commit_id))
print(gerrits)
print(gerrits[1].commitid)

print('--------------------')

def total(p1, p2):
    return p1 + p2

x = [7, 3, total]

def totalizer(args):
    return args[2](args[0], args[1])

print(totalizer(x))