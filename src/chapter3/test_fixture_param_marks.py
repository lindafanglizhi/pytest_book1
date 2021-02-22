# Author: lindafang
# Date: 2020-05-16 14:25
# File: test_fixture_param_marks.py

import pytest


# 而第二个数据做个标记为预期失败。
@pytest.fixture(params=[('3+5', 8),
                        pytest.param(('6*9', 42),
                                     marks=pytest.mark.xfail,
                                     id='failed')])
def data_set(request):
    return request.param


def test_data(data_set):
    # eval可以将字符串中的表达式进行计算，也就是3+5计算后与8比对，6*9计算后与42比对
    assert eval(data_set[0]) == data_set[1]
