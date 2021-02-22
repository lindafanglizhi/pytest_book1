# Author: lindafang
# Date: 2020-10-8 08:56
# File: conftest.py
import os
import sys

import allure
import pytest
from selenium import webdriver

from ..Utils.get_path import get_par_path
from ..Utils.log import conf

sys.path.append('..')


@allure.feature('打开浏览器')
@pytest.fixture(scope="session", autouse=True)
def init_driver(request):
    log = conf.logcon()
    log.info('setup_class')
    driver_path = os.path.join(get_par_path(), "driver/chromedriver")
    driver = webdriver.Chrome(executable_path=driver_path)

    def close_browser():
        driver.quit()

        # 无论执行正确和错误最终都执行关闭浏览器的方法
        request.addfinalizer(close_browser)

    return driver
