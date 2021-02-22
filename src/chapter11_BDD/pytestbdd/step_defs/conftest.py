# Author: lindafang
# Date: 2020-10-22 13:19
# File: conftest.py

import pytest

from pytest_bdd import given
from selenium import webdriver

# Constants

LindaFang_HOME = 'https://www.jianshu.com/u/030c07091ea4'


# Fixtures

@pytest.fixture(scope='module')
def browser():
    # 打开浏览器
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Shared Given Steps

@given('LindaFang简书页')
def ddg_home(browser):
    # 进入lindaFang简书的页
    browser.get(LindaFang_HOME)
    assert '测试星云' in browser.page_source
