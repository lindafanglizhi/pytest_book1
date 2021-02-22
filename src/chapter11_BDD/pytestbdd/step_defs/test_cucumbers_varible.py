# Author: lindafang
# Date: 2020-10-21 15:17
# File: test_cucumbers_varible.py

from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import CucumberBasket

scenarios('../features/cucumbers_varible.feature')

EXTRA_TYPES = {
    'Number': int,
}


# 通过外部传递参数的方式，initial对应参数，Number对应要传的数据
@given(parsers.cfparse('篮子原来有 "{initial:Number}" 个黄瓜', extra_types=EXTRA_TYPES))
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('添加 "{some:Number}" 个黄瓜到篮子中', extra_types=EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@when(parsers.cfparse('从篮子中拿出 "{some:Number}" 个黄瓜', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('篮子剩余 "{total:Number}" 个黄瓜', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    print(basket.count)
    assert basket.count == total
