# Author: lindafang
# Date: 2020-04-30 15:00
# File: test_raise.py

import pytest


def f():
    # 解释器请求退出
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        print("如果确实是解释器请求退出这个原因引起的异常测试是通过的")
        f()


def test_mytest_error():
    with pytest.raises(ImportError):
        print("如果不是解释器请求退出这个原因引起的异常测试是不通过的")
        f()
