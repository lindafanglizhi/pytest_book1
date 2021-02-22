# Author: lindafang
# Date: 2020-12-01 13:56
# File: conftest.py
import pytest


@pytest.fixture
def username(username):
    return 'overridden-' + username
