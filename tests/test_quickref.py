# coding=utf-8
import sys
import os.path
import pprint
from src.quickref import *
from src.utilities import food_list, test_file_data

# Allows the tests to be run from any directory
LOREM_TXT_FIILENAME = os.path.dirname(__file__) + "/data/lorem.txt"


def test_string_demo():
    """
    """
    assert string_demo("Ed") == "Welcome to Ed's World!!!"


def test_filtered_list():
    assert filtered_list(food_list) == ["apples", "grasshoppers", "hamburgers"]


def test_zipping():
    """
    """
    # Since there are only three food_types, it will only pick up the first three items in food_list.
    food_types = ["fruit", "meals", "weird"]
    expected_result = {
        "fruit": ["apples", "bananas", "oranges"],
        "meals": ["hamburgers", "pizza", "tacos"],
        "weird": ["grasshoppers", "horse", "eels"],
    }
    x = zipping(food_types, food_list)
    assert len(x) == len(expected_result)
    for k, v in x.items():
        assert v == expected_result[k]


def test_use_function_reference():
    """
    A variable can hold a function reference, and it is called when it looks like a function
    (i.e., with parenthesis and signature-appropriate arguments)
    The reference used here is set up in the utilities module
    """
    assert food_list[4](32, 76) == "32 plus 76 equals 108"


def test_phonetics():
    """
    """
    assert phonetics("L") == "Lima"
    assert phonetics("%") == "$$ ERROR: character not found."


def test_significant():
    """ A tuple literal
    """
    t = ("Echo", "November", "Victor")
    assert significant(t) == "Foxtrot Oscar Whiskey : and 'else' was executed."


def test_unique():
    # Nested function
    def create_test_file(create_file_name):
        """This creates a small file with repeated lines
        for methods finding unique lines
        DEMONSTRATES: writing to files in a context manager, multi-line strings
        """
        with open(create_file_name, mode="w") as fw:
            fw.write(test_file_data)

    filename = "test.txt"
    create_test_file(filename)
    assert unique(filename) == "asdfasdf asfd klasdflhf sdfdsf"
    os.remove(filename)
    unique(filename)
    assert unique(filename) == "File {} not found.".format(filename)


def test_encode_rownum():
    assert encode_rownum(62) == "10"
    assert encode_rownum(1234567) == "5ban"
    assert encode_rownum(0) == "0"


def test_decode_url():
    assert decode_url("10") == 62
    assert decode_url("5ban") == 1234567
    assert decode_url("0") == 0


def test_fibonacci():
    assert fibonacci() == "0 1 1 2 3 5 8 13 21 34 55 89"


def test_permute():
    permute(4, list("ABCD"))


def test_subprocess_ls():
    z = subprocess_ls()
    # The 'ls -l' output is unpredictable, except for the first part of the first line.
    assert z[0].startswith("total")
    # Since we use -al the last charachter of the second line should be a dot (for the current directory).
    assert z[1].endswith(".")
    pass


# Patch replaces stdout with a string to catch the sysout stream
def test_catch_stdout(capsys):
    print_something()
    out, err = capsys.readouterr()
    assert err == ""
    assert (
        out
        == u"""This is the mock/patch part of the test.
This output will be caught by the capsys fixture.
"""
    )
    pass


def test_walkies():
    d = walkies(".")
    pass


def process_file_with_generators():
    pass


def test_elgoog():
    assert elgoog("GOOGLE") == "ELGOOG|ELGOOG|ELGOOG|ELGOOG|ELGOOG|ELGOOG"


def test_count_unique():
    """
    """
    assert count_unique("GOOGLE") == {"E": 1, "G": 2, "L": 1, "O": 2}


def test_unique_via_comp():
    """ Dictionaries are output by pprint in key order. The options are to keep the output on one line.
    """
    unique_values_ = unique_via_comp(LOREM_TXT_FIILENAME)
    assert (
        "{'ac': 7, 'arcu': 7, 'eget': 10, 'et': 10, 'in': 11, 'mauris': 7, 'nec': 8, 'non': 7, 'vel': 8}"
        == pprint.pformat(dict(unique_values_), width=999999)
    )


def test_default_dict():
    """ Note: This test is stand-alone, it has no part in quickref.py
    DEMONSTRATES: collections.defaultdict()
    """
    # defaultdict takes a callable, which is called with no parameters
    d = collections.defaultdict(lambda: "<missing>")
    d.update(name="John", action="ran")
    result = "{name} {action} to {object}".format(
        name=d["name"], action=d["action"], object=d["object"]
    )
    assert result == "John ran to <missing>"


def test_templates():
    """
    Use string Templates
    :return:
    """
    expected_sentence = "My oak is a mighty oak."
    (full_sub, partial_sub) = template_substitute("oak", "mighty")
    assert full_sub == expected_sentence
    assert partial_sub == expected_sentence
