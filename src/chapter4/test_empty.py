import sys

import pytest


def read_value():
    if sys.version_info >= (3, 8):
        return [1, 2, 3]
    else:
        return []


@pytest.mark.parametrize('test_input', read_value())
def test_empty(test_input):
    assert test_input
