# Author: lindafang
# Date: 2020-12-01 13:56
# File: test_something.py
import pytest


#
# def test_username(username):
#     assert username == 'username'


@pytest.fixture
def username(username):
    return 'overridden-' + username


def test_username(username):
    assert username == 'overridden-username'


@pytest.mark.parametrize('username', ['directly-overridden-username'])
def test_username(username):
    assert username == 'directly-overridden-username'


@pytest.mark.parametrize('username', ['directly-overridden-username-other'])
def test_username_other(username, other_username):
    assert other_username == 'other-directly-overridden-username-other'
