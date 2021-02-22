# Author: lindafang
# Date: 2020-05-17 14:25
# File: test_mark.parametrize.py

import pytest


@pytest.mark.parametrize("test_case", [1, 2, 3, 'orange', 'apple'])
def test_string(test_case):
    print("\n我们的测试数据：{}".format(test_case))


# 参数化，前面两个变量，后面是对应的数据；3+5--->test_input,8-->expected
@pytest.mark.parametrize("test_input,expected", [("3+5", 8),
                                                 ("2+5", 7),
                                                 ("7*5", 30),
                                                 ])
def test_eval(test_input, expected):
    # eval将字符串str当成有效的表达式来求值并返回计算结果
    assert eval(test_input) == expected
