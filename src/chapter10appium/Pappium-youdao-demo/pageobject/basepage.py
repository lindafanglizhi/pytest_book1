# Author: lindafang
# Date: 2020-08-13 11:27
# File: basepage.py

import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

log = logging.getLogger("linda's test")


class BasePage(object):

    def __init__(self, driver):
        # init
        # self
        # 设置driver的类型,所有方法在没有实例时才能点出来
        self.driver: WebDriver = driver
        log.info("这是个初始化驱动！")

    def set_value(self, locator, value):

        if (WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
        )):
            # 参数传递，元组格式与非元组格式
            element = self.driver.find_element(*locator)
            element.click()
            element.clear()
            element.send_keys(value)
        else:
            log.error("无法输入信息，找不到元素")

    def click_thing(self, locator):
        if (WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
        )):
            element = self.driver.find_element(*locator)
            element.click()
        else:
            log.error("无法点击，找不到元素")

    def save_pic(self, filepath):
        self.driver.get_screenshot_as_file(filepath)

    def swipe_up(self, driver):
        # 兼容性-适合所有手机，获得屏幕大小--宽，高
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        # swipe（x=起始点x坐标，y=起始点y的坐标，x1=滑动到的点的x坐标，y1=滑动到的点的y坐标）
        # 0，0的点是在屏幕左上角。
        self.driver.swipe(width / 2, height / 3 * 2, width / 2, height / 3 * 1)

    def swipe_down(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        self.driver.swipe(width / 2, height / 3, width / 2, height / 3 * 2)

    def swipe_right(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        self.driver.swipe(width / 10, height / 2, width / 10 * 9, height / 2)

    def swipe_left(self, driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        self.driver.swipe(width / 10 * 9, height / 2, width / 10, height / 2)
