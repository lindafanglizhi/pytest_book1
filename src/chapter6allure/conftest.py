# Author: lindafang
# Date: 2020-10-05 14:25
# File: conftest.py
import allure
import pytest


@allure.step('步骤在conftest.py')
def conftest_step():
    pass


@pytest.fixture
def fixture_with_conftest_step():
    conftest_step()
