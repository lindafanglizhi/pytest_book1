# Author: lindafang
# Date: 2020-12-01 14:13
# File: test_something_else1.py

# content of tests/test_something_else.py
def test_username(parametrized_username):
    assert parametrized_username in ['one', 'two', 'three']


def test_username1(non_parametrized_username):
    assert non_parametrized_username == 'username'
