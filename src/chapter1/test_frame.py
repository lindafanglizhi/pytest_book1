# Author: lindafang
# Date: 2020-04-28 21:38
# File: test_frame.py
import pytest


# 模块中的方法
def setup_module():
    print("\nsetup_module：整个test_module.py模块只执行一次")


def teardown_module():
    print("teardown_module：整个test_module.py模块只执行一次")


def setup_function():
    print("setup_function：每个非类函数测试用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个非类函数测试用例结束后都会执行")


# 测试模块中的用例1


def test_one():
    print("正在执行测试模块----test_one")


def test_one_1():
    print("正在执行测试模块----test_one_1")


# 测试模块中的用例2
def test_two():
    print("正在执行测试模块----test_two")


# 测试类
class TestCase(object):
    def setup_class(self):
        print("\nsetup_class：在类中所有测试用例执行之前")

    def teardown_class(self):
        print("teardown_class：在类中所有测试用例执行之后")

    def setup_method(self):
        print("setup_method: 每个类中测试方法用例开始前执行")

    def teardown_method(self):
        print("teardown_method: 每个类中测试方法用例结束后执行")

    def setup(self):
        print("setup：每个类中测试方法用例开始前都会执行")

    def teardown(self):
        print("teardown：每个类中测试方法用例结束后都会执行")

    def test_three(self):
        print("正在执行测试类----test_three")

    def test_four(self):
        print("正在执行测试类----test_four")


if __name__ == "__main__":
    pytest.main(["-s", "test_frame.py"])
