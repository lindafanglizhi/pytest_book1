# Author: lindafang
# Date: 2020-12-01 13:56
# File: test_something.py


import pytest


@pytest.fixture
def parametrized_username():
    return 'overridden-username'


@pytest.fixture(params=['one', 'two', 'three'])
def non_parametrized_username(request):
    return request.param


def test_username(parametrized_username):
    assert parametrized_username == 'overridden-username'


def test_parametrized_username(non_parametrized_username):
    assert non_parametrized_username in ['one', 'two', 'three']
