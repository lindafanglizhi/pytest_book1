# Author: lindafang
# Date: 2020-05-09 20:42
# File: test_skip_class.py
import pytest


@pytest.mark.skip("作用于类中的每一个用例，所以 pytest 共收集到两个 SKIPPED 的用例。")
class TestMyClass():
    def test_one(self):
        assert True

    def test_two(self):
        assert True
