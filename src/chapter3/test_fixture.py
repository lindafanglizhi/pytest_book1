# Author: lindafang
# Date: 2020-08-16 14:25
# File: test_fixture.py

import pytest


# 不带参数时scope="function"
# 有个依赖关系，先登陆，与其他功能有依赖。


@pytest.fixture()
def login():
    print("\n用户名linda密码登陆！")


def test_cart(login):
    print('\n用例1，登陆后执行查看购物车其它功能1')


def test_find_goods():
    print('\n用例2，不登陆后执行浏览商品功能2')


def test_pay(login):
    print('\n用例3，登陆后执行支付功能3')
