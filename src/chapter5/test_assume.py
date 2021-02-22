# Author: lindafang
# Date: 2020-10-22 16:40
# File: test_assume.py
import pytest

# 输入的测试数据有3种，我们需要断言同时满足三种情况

# x == y
# x+y > 1
# x > 1
from pytest_assume.plugin import assume


@pytest.mark.parametrize(('x', 'y'),
                         [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    print("测试数据x=%s, y=%s" % (x, y))
    assert x == y
    assert x + y > 1
    assert x > 1


@pytest.mark.parametrize(('x', 'y'),
                         [(1, 1), (1, 0), (0, 1)])
def test_simple_assume1(x, y):
    print("测试数据x=%s, y=%s" % (x, y))
    pytest.assume(x == y)
    pytest.assume(x + y > 1)
    pytest.assume(x > 1)
    print("测试完成！")


@pytest.mark.parametrize(('x', 'y'),
                         [(1, 1), (1, 0), (0, 1)])
def test_simple_assume_with(x, y):
    print("测试数据x=%s, y=%s" % (x, y))
    with assume: assert x == y
    with assume: assert x + y > 1
    with assume: assert x > 1
    print("测试完成！")
