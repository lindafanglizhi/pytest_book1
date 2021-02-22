# Author: lindafang
# Date: 2020-05-05 14:26
# File: test_assert_except.py

import pytest


def f():
    # 解释器请求退出
    raise SystemExit(1)


def test_mytest():
    # 当调用f()时出现SystemExit的异常时，就是正确的。出现其他异常就是错误的。
    # with pytest.raises(SystemExit):
    with pytest.raises(ValueError):
        f()


def myfunc():
    # 引起值错误
    raise ValueError("返回40013支付错误")


def test_match():
    # 当调用myfunc()时出现值错误是正确的，
    # 值的信息保存到excinfo中，并且可能断言值中的属性value的内容
    # with pytest.raises(ValueError) as excinfo:
    # 异常类型可以写多个，后面可以跟正则表达式，与断言类似
    with pytest.raises((ValueError, RuntimeError), match=r'.*40011.*'):
        myfunc()
    # assert '40013' in str(excinfo.value)
