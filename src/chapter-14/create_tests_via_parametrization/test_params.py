# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(params=['apple', 'banana'])
def fruit(request):
    return request.param


def test_fruit(fruit):
    print('这是我要输入的测试数据：我今天吃的是%s' % fruit)
