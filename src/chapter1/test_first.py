# Author: lindafang
# File: test_first.py
import pytest


def test_1():
    print("\n这是第一个测试方法")


def test_3():
    print("\n这是第三个测试方法")


#
# def t_2():
#     print("这是第二个测试方法")


if __name__ == "__main__":
    pytest.main(["-s", "test_first.py"])
