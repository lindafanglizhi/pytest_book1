# Author: lindafang
# Date: 2020-05-14 16:57
# File: test_xfail_param.py

import sys

import pytest


@pytest.mark.parametrize(
    ('n', 'expected'),
    [(2, 1),
     pytest.param(2, 1, marks=pytest.mark.xfail(), id='XPASS'),
     pytest.param(0, 1, marks=pytest.mark.xfail(raises=ZeroDivisionError), id='XFAIL'),
     pytest.param(1, 2, marks=pytest.mark.skip(reason='无效的参数，跳过执行')),
     pytest.param(1, 2, marks=pytest.mark.skipif(sys.version_info <= (3, 8), reason='请使用3.8及以上版本的python。'))])
def test_params(n, expected):
    assert 2 / n == expected
