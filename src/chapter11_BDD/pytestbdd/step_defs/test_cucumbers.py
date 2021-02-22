# Author: lindafang
# Date: 2020-10-21 14:24
# File: test_cucumbers.py
from pytest_bdd import scenario, given, when, then

from cucumbers import CucumberBasket


@scenario('../features/cucumbers.feature', '摘黄瓜到篮子')
def test_add():
    pass


@given("篮子原来有 2 个黄瓜")
def basket():
    # 初始化要测试的篮子方法，传入初始化数据起始数量为2
    return CucumberBasket(initial_count=2)


@when("添加 4 个黄瓜到篮子中")
def add_cucumbers(basket):
    # basket参数类似pytest.fixture，basket()函数的返回
    # 是CucumberBasket类的实例
    # 执行添加功能
    basket.add(4)


@then("篮子剩余 6 个黄瓜")
def basket_has_total(basket):
    # 获得CucumberBasket中属性并断言添加是否成功
    assert basket.count == 6
