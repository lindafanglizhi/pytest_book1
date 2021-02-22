#! /usr/bin python
# ! /usr/bin/env python3
# Author: lindafang
# Date: 2020-07-14 16:29
# File: test_pytest_selenium_browser.py


def test_baidu_title(selenium):
    selenium.get('http://www.baidu.com/')
    assert selenium.title == '百度一下，你就知道'


def test_baidu_current_url(selenium):
    selenium.get('http://www.baidu.com/')
    assert selenium.current_url == 'https://www.baidu.com/'


def test_baidu_so_getValue(selenium):
    selenium.get('http://www.baidu.com/')
    so = selenium.find_element_by_id('kw')
    so.send_keys('linda')
    assert so.get_attribute('value') == 'linda'
