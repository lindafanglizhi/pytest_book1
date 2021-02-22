# Author: lindafang
# Date: 2020-07-14 09:59
# File: test_my_program.py
from my_program import cau


class Test_cover:
    def test_add(self):
        a = cau(1, 2, 3)
        assert a == 3

    def test_sub(self):
        a = cau(2, 3, 2)
        assert a == 1
