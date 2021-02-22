# Author: lindafang
# Date: 2020-08-04 11:27
# File: login_method.py
# 封装一些login页面的方法
# 相对位置调用
# from .login_locators import LoginPageLocators
from pages.base_public_method import BasePage
# 绝对地 址调用，默认路径工程路径
from pages.login_locators import LoginPageLocators
from pages.main_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    # 方法

    # 1、输入用户名
    def enter_username(self, username):
        #    智能等待这个元素加载上， 点击，清除，输入,为什么*，参数是元组（By.ID,""）拆开
        #     等待用户名这个文本框加载上
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*LoginPageLocators.username_text))
        # 用户名元素定位
        element = self.driver.find_element(*LoginPageLocators.username_text)
        # 点击一下
        # element.click()
        # 清空文本框
        element.clear()
        # 输入传入的内容
        element.send_keys(username)

    # 2、输入密码
    def enter_password(self, password):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*LoginPageLocators.password_text))
        element = self.driver.find_element(*LoginPageLocators.password_text)
        element.clear()
        element.send_keys(password)

    # 3、点击登陆

    def click_login(self):
        element_click = self.driver.find_element(*LoginPageLocators.login_submit)
        element_click.click()

    # 4、返回要验证的文本，登陆成功
    def result_login_sucess(self):
        # 验证 welcome Admin（text）出现   presene_of_element_located(locator),locator需要元组格式
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(MainPageLocators.welcome_link))
        return self.driver.find_element(*MainPageLocators.welcome_link).text
