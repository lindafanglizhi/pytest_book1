# Author: lindafang
# Date: 2020-10-22 13:11
# File: test_web_jianshu.py

import time

from pytest_bdd import scenarios, when, then, parsers
from selenium.webdriver.common.keys import Keys

# Constants

LindaFang_HOME = 'https://www.jianshu.com/u/030c07091ea4'

# Scenarios

scenarios('../features/web_jianshu.feature')


# When Steps

@when(parsers.parse('搜索"{phrase}"的文章'))
@when(parsers.parse('搜索任何一个"<phrase>"的文章'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)


# Then Steps

@then(parsers.parse('显示"{phrase}"的文章'))
def results_have_one(browser, phrase):
    time.sleep(2)
    results = browser.page_source
    assert phrase in results


@then(parsers.parse('显示这个"<phrase>"所包含的文章'))
def search_results(browser, phrase):
    time.sleep(2)
    results = browser.page_source
    assert phrase in results
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
