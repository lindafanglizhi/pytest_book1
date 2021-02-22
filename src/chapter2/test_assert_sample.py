# Author: lindafang
# Date: 2020-04-30 16:33
# File: test_assert_sample.py
import textwrap
from math import sqrt

from pytest import approx


# 勾股定理求斜边值sqrt是平方根
def magnitude(x, y):
    return sqrt(x * x + y * y)


def test_mag():
    assert magnitude(3, 4) == 5


# 这是加了个绝对值abs的函数，这样浮点小数的计算的误差小于0.0001,这个断言是正确的
# 这个断言是比较运算符
def test_simple_math():
    assert abs(0.1 + 0.2) - 0.3 < 0.0001


# approx函数是解决浮点小数的问题的，所以此断言也是正确的
def test_approx_simple():
    assert 0.1 + 0.2 == approx(0.3)


def test_approx_simple_fail():
    assert 0.1 + 0.2 == approx(0.35)


# 比较一个长文本哪里不同
def get_long_class_description(class_name):
    assert class_name == "warrior"
    return textwrap.dedent(
        """\
    A seasoned veteran of many battles. High Strength and Dexterity
    allow to yield heavy armor and weapons, as well as carry
    more equipment while keeping a light roll. Weak in magic.            
    """
    )


# 比较一个长文本哪里不同
def test_warrior_long_description():
    desc = get_long_class_description("warrior")
    assert (
            desc
            == textwrap.dedent(
        """\
    A seasoned veteran of many battles. Strength and Dexterity
    allow to yield heavy armor and weapons, as well as carry
    more equipment. Weak in magic.            
    """
    )
    )


# 防御性的编程，如果不是战士直接退出，是战士判断返回的是否正确
def get_starting_equipment(class_name):
    assert class_name == "战士"
    return ["长剑", "战士装备", "盾"]


def test_get_starting_equiment():
    expected = ["长剑", "战士装备"]
    assert get_starting_equipment("战士") == expected, "装备不符"


# 测试返回类型是否一致
def test_isinstance():
    task_id = 10
    assert isinstance(task_id, int)
