import pytest

from _pytest.mark.structures import ParameterSet


#
# @pytest.mark.parametrize('input, expected', [(1, 2)])
# def test_sample1(input):
#     assert input + 1 == 1
#
#
# @pytest.mark.parametrize('input, expected', [(1, 2)])
# def test_sample2(input, expected=2):
#     assert input + 1 == expected
#
#
# @pytest.fixture()
# def expected():
#     return 1
#
#
# @pytest.mark.parametrize('input, expected', [(1, 2)])
# def test_sample3(input, expected):
#     assert input + 1 == expected

#
#
# @pytest.mark.parametrize('input, expected', [(1, 2), [2, 3], set([3, 4])])
# def test_sample4(input, expected):
#     print(expected)
#     assert input + 1 == expected

# @pytest.mark.parametrize(
#     ('n', 'expected'),
#     [(4, 2),
#     pytest.param(6, 3, marks=pytest.mark.xfail(), id='XPASS')])
# def test_params(n, expected):
#     assert n / 2 == expected


# 参数化，前面两个变量，后面是对应的数据；3+5--->test_input,8-->expected
# @pytest.mark.parametrize("test_input,expected",[("3+5", 8),
#                                                 ("2+5", 7),
#                                                 pytest.param("6*9", 42, marks=pytest.mark.xfail),
#                                                 ])
# def test_eval(test_input, expected):
#     # eval将字符串str当成有效的表达式来求值并返回计算结果
#     assert eval(test_input) == expected
#
#
@pytest.mark.parametrize(
    'input, expected',
    [(1, 2), ParameterSet(values=(3, 4), marks=[], id=None)])
def test_sample10(input, expected):
    assert input + 1 == expected
