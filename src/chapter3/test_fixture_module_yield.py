# Author: lindafang
# Date: 2020-08-16 14:25
# File: test_fixture_module_yield.py
import pytest


# 在整个模块只做一次的事，范围是模块级别的。


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，打开百度首页")

    yield

    print('执行teardown')
    print('最后关闭浏览器')


# open在第一个方法中使用，其他方法可以不加
def test_s7():
    print('用例7，')


# 如果第一个方法中没有open,则第一个方法单独执行，再执行下面二个方法
def test_s8(open):
    print('用例8，')


# 也就是说，open加在哪个测试方法中，就从该方法以后实现open依赖注入效果
def test_s9(open):
    print('用例9，')
