# Author: lindafang
# Date: 2020-10-05 16:11
# File: test_title.py

import allure
import pytest


@allure.title("这是一个正常的标题")
def test_with_a_title():
    assert 2 + 2 == 4


@allure.title("这是标题支持其他国家文字: Привет!こんにちは！")
def test_with_unicode_title():
    assert 3 + 3 == 6


@allure.title("参数化标题: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [
    (2, 2, 4),
    (1, 2, 5)
])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected


@allure.title("动态标题")
def test_with_dynamic_title():
    assert 2 + 2 == 4
    allure.dynamic.title('替换动态标题是最终标题')
