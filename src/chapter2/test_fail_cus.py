# Author: lindafang
# Date: 2020-05-05 18:40
# File: test_fail_cus.py
class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    # 为了能看到更详细的信息
    def __repr__(self):
        return str(self.val)


def test_foo_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2  # , '第一个实例中内容与第二实例中内容不相等'


def test_num():
    assert 1 == 2, '这两个值不相等'
