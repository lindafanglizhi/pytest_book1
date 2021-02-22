# Author: lindafang
# Date: 2020-04-28 16:42
# File: test_frame_1.py

import pytest


# 模块中的方法
def setup_module():
    print("\nsetup_module：整个test_module.py模块只执行一次")


def teardown_module():
    print("teardown_module：整个test_module.py模块只执行一次")


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


# 测试模块中的用例1
def test_one():
    print("正在执行测试模块----test_one")


# 测试模块中的用例2
def test_two():
    print("正在执行测试模块----test_two")


if __name__ == "__main__":
    pytest.main(["-s", "test_frame_1.py"])
