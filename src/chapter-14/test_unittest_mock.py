# Author: lindafang
# Date: 2020-05-03 19:45
# File: test_unittest_mock.py

from unittest import mock

import pytest

config = {"mykey": "ORIGINAL"}


@pytest.fixture(scope="function")
@mock.patch.dict(config, {"mykey": "MOCKED"})
def my_fixture():
    return config["mykey"]


def test_foobar(my_fixture):
    assert my_fixture == "MOCKED"
