# Author: lindafang
# Date: 2020-11-17 09:33
# File: test_usefixtures.py
import pytest


@pytest.fixture()
def driver1():
    driver = 8
    print(driver)


@pytest.fixture()
def login():
    print("登陆")


@pytest.mark.usefixtures
def test_driver():
    assert 1
