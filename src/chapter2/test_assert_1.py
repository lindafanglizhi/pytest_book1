# Author: lindafang
# Date: 2020-04-30 14:00
# File: test_assert_1.py


def f():
    return 3


# 断言f()的返回值是否等于4
def test_f():
    assert f() == 4
