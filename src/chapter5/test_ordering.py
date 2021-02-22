# Author: lindafang
# Date: 2020-07-14 14:28
# File: test_ordering.py

def test_03():
    print("\ntest_03")


def test_04():
    print("test_04")


class TestA(object):
    def test_05(self):
        print("test_05")

    # @pytest.mark.last
    def test_06(self):
        print("test_06")


class TestC(object):
    # @pytest.mark.run(order=1)
    def test_01(self):
        print("\ntest_01")

    def test_02(self):
        print("test_02")
