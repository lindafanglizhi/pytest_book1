# Author: lindafang
# Date: 2020-10-05 14:27
# File: test_step_conftest_fixture.py
import allure


@allure.step
def passing_step():
    pass


def test_with_step_in_fixture_from_conftest(fixture_with_conftest_step):
    passing_step()
