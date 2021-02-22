# Author: lindafang
# Date: 2020-12-01 13:32
# File: test_fixture_twofixtures-2.py

import pytest


# fixture可以嵌套使用
@pytest.fixture()
def login(open_browser):
    print('这是个登陆模块！')


@pytest.fixture(scope="module")
def open_browser():
    print('打开首页！')


def test_soso(login):
    print('case1: 登际后执行搜索')


def test_cakan():
    print('case2:不登陆就看')


def test_cart(login):
    print('case3,登陆，加购物车')
