# Author: lindafang
# Date: 2020-11-25 16:00
# File: test_bbb.py
import time

import pytest


@pytest.fixture(scope="function")
def setup_demo():
    # raise TypeError("ERROR!")
    yield
    raise TypeError("ERROR!")


def test_b_2():
    print("测试用例b_2")


def test_b_1():
    print("测试用例b_1")


def test_5():
    print("测试用例55555555")
    time.sleep(3)


def test_6():
    print("测试用例66666666")
    time.sleep(3)
    assert 1 == 2
