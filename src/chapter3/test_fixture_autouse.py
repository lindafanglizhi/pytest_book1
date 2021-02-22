# Author: lindafang
# Date: 2020-12-01 11:10
# File: test_fixture_autouse.py
import pytest


# autouse=True 不用要测试方法中传参调用，默认全使用，
@pytest.fixture(autouse=True)
def open_browser():
    print('打开首页！')


def test_login():
    print('case1: 登陆')


def test_search():
    print('case2:搜索')


def test_exit():
    print('case3,退出')
