from builtins import range
from random import choice, randint
from string import ascii_uppercase
import uuid


def generate_fake_table_row():
    """
    Tuple Generator
    When it falls through the end of the function, a
    StopException is raised to signal the caller we're done
    """
    for k in range(10):
        c = uuid.uuid4()
        a = "".join(choice(ascii_uppercase) for i in range(5))
        b = randint(1, 1000)
        yield k, a, b, c


def function_reference(param1, param2):
    """
    DEMONSTRATES: a function reference buried in a list, old-style formatting
    """
    total = param1 + param2
    # trinary(ish)
    # x = "is" if total > 100 else "is not"
    # old-style formatting needs a tuple, but see process_file_with_generators() below
    return "{} plus {} equals {}".format(param1, param2, total)


# Create some useful variables for tests.
food_list = [
    ["apples", "bananas", "oranges"],
    ["hamburgers", "pizza", "tacos"],
    ["grasshoppers", "horse", "eels"],
    27.0345,
    function_reference,
]
test_file_data = """klasdflhf
sdfdsf
asdfasdf
asfd
asdfasdf
klasdflhf
asfd
sdfdsf"""
