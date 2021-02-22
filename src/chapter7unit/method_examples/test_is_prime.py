# Author: lindafang
# Date: 2020-09-03 14:33
# File: test_is_prime.py

import pytest

from src.chapter7unit.method_examples.is_prime import is_prime


class TestPrimes(object):
    """测试is_prime"""

    def test_is_five_prime(self):
        """5是不是质数？"""
        assert is_prime(5) is True

    def test_is_four_non_prime(self):
        """4不是质数"""
        assert is_prime(4) is False

    def test_is_zero_not_prime(self):
        """测试边界值0是不是质数"""
        assert is_prime(0) is False


if __name__ == '__main__':
    pytest.main()
