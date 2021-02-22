# Author: lindafang
# Date: 2020-08-14 08:57
# File: conftest.py
import pytest
from appium import webdriver

from utils import desired_caps
# 在哪个包下，这个包下所有文件共享的数据写在这里
from utils.get_path import PATH
from utils.get_yaml import get_yaml_data


@pytest.fixture(scope='session')
def run_app(request):
    desired_cap_value = desired_caps.get_desired_caps()
    driver = webdriver.Remote(get_yaml_data(PATH("../config/conf.yaml"))['base_url'], desired_cap_value)

    def close_app():
        driver.quit()

    request.addfinalizer(close_app)
    return driver
