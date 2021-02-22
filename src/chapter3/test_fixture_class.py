# Author: lindafang
# Date: 2020-12-01 11:10
# File: test_fixture_class.py

import pytest


@pytest.fixture(scope="class")
def first():
    print("\n获取用户名,scope为class级别只运行一次")
    a = "linda"
    return a


def test_3():
    print("不在类中的测试方法")


class TestCase():
    def test_1(self, first):
        '''用例传fixture'''
        print("测试账号：%s" % first)
        assert first == "linda"

    def test_2(self, first):
        '''用例传fixture'''
        print("测试账号：%s" % first)
        assert first == "linda"
