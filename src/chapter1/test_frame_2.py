# Author: lindafang
# Date: 2020-04-28 16:42
# File: test_frame_1.py

import pytest


# 测试类
class TestCase(object):
    def setup_class(self):
        print("\nsetup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def setup_method(self):
        print("setup_method: 每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method: 每个用例结束后执行")

    def setup(self):
        print("setup：每个用例开始前都会执行")

    def teardown(self):
        print("teardown：每个用例结束后都会执行")

    def test_three(self):
        print("正在执行测试类----test_three")

    def test_four(self):
        print("正在执行测试类----test_four")


if __name__ == "__main__":
    pytest.main(["-s", "test_frame_2.py"])
