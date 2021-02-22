# Author: lindafang
# Date: 2020-05-16 14:25
# File: test_fixture_params.py
import pytest


# 每次执行应用不同数据，一次应用一个。这个方法是准备不同数据的。
@pytest.fixture(params=['apple', 'banana'])
def fruit(request):
    # 将列表的数据每一个依次返回
    return request.param


def test_fruit(fruit):
    print("\n我今天吃{}".format(fruit))
    assert True


def test_cook_fruit(fruit):
    print("我今天做{}派。".format(fruit))
    assert True
