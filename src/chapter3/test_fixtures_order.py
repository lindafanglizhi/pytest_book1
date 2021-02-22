# Author: lindafang
# Date: 2020-12-01 13:32
# File: test_fixture_order.py

import pytest

order = []


@pytest.fixture(scope="session", autouse=True)
def session1():
    order.append("session1")


@pytest.fixture(scope="module", autouse=True)
def module1():
    order.append("module1")


# function1嵌套调用function3,所以先执行function3再执行function1
@pytest.fixture(autouse=True)
def function1(function3):
    order.append("function1")


@pytest.fixture
def function3():
    order.append("function3")


# autouse在所在function之前使用
@pytest.fixture(autouse=True)
def autouse1():
    order.append("autouse1")


@pytest.fixture(autouse=True)
def function2():
    order.append("function2")


def test_order(module1):
    assert order == ["session1", "module1", "autouse1", "function3", "function1", "function2"]
    # 特意断言错误查看执行顺序
    assert order == ["session1"]
