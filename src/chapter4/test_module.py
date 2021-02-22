import pytest


# pytestmark = pytest.mark.parametrize('test_input, expected', [(1, 2), (3, 4)])
#
#
# def test_module(test_input, expected):
#     assert test_input + 1 == expected


@pytest.fixture()
def expected():
    return 2


@pytest.fixture()
def input():
    return 0


@pytest.mark.parametrize('input', [(1)])
# @pytest.mark.parametrize('input, expected', [(1, 2)])
def test_sample(input, expected):
    assert input + 1 == expected
