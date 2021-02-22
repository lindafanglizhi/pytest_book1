# Author: lindafang
# Date: 2020-12-01 13:55
# File: conftest.py
import pytest


@pytest.fixture
def username():
    return 'username'


@pytest.fixture
def other_username(username):
    return 'other-' + username


@pytest.fixture(params=['one', 'two', 'three'])
def parametrized_username(request):
    return request.param


@pytest.fixture
def non_parametrized_username(request):
    return 'username'
