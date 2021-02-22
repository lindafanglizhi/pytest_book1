# Author: lindafang
# Date: 2020-10-04 11:28
# File: base_public_method.py
# 把所 有页面公共一些方法写在里


class BasePage(object):
    # 初始化是在类加载时加载的方法，在浏览器打开基础上，浏览器参数
    # 初始化打开浏览器
    def __init__(self, driver):
        self.driver = driver

    # 截图
    def save_picture(self, filepath):
        self.driver.save_screenshot(filepath)
