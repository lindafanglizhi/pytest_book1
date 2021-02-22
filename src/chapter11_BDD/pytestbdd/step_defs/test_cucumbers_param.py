# Author: lindafang
# Date: 2020-10-21 15:17
# File: test_cucumbers_param.py

from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import CucumberBasket

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}
scenarios('../features/cucumbers_param.feature', example_converters=CONVERTERS)


@given(parsers.cfparse('篮子原来有 "{initial:Number}" 个黄瓜', extra_types=EXTRA_TYPES))
@given('篮子原来有 "<initial>" 个黄瓜')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('添加 "{some:Number}" 个黄瓜到篮子中', extra_types=EXTRA_TYPES))
@when('添加 "<some>" 个黄瓜到篮子中')
def add_cucumbers(basket, some):
    basket.add(some)


@when(parsers.cfparse('从篮子中拿出 "{some:Number}" 个黄瓜', extra_types=EXTRA_TYPES))
@when('从篮子中拿出 "<some>" 个黄瓜')
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('篮子剩余 "{total:Number}" 个黄瓜', extra_types=EXTRA_TYPES))
@then('篮子剩余 "<total>" 个黄瓜')
def basket_has_total(basket, total):
    print(basket.count)
    assert basket.count == total
