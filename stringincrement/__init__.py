from nose.tools import assert_equals
from nose.plugins.attrib import attr

import string_incrementer

def check(package, word, ideal_output):
    output = package.string_incrementer(word)
    assert_equals(output, ideal_output, f"{output} != {ideal_output}")

@attr('Level_1')
def test_string_incrementer_1():
    level_1_tests = ["foo2","bar3","stephane8","hello6"]
    level_1_tests_output = ["foo3","bar4", "stephane9","hello7"]
    for word, ideal_output in zip(level_1_tests, level_1_tests_output):
        yield check, string_incrementer, word, ideal_output
