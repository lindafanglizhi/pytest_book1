# Author: lindafang
# Date: 2020-11-25 15:59
# File: test_aaa.py
import pytest


def test_a_1():
    print("测试用例a_1")


def test_a_2():
    print("测试用例a_2")


def test_1():
    print("测试用例1111")
    assert 1 == 1


@pytest.mark.skip("跳过")
def test_2():
    print("测试用例22222")
    assert 1 == 1


def test_3():
    print("测试用例3333")


def test_4():
    print("测试用例44444444")
    assert 1 == 2
