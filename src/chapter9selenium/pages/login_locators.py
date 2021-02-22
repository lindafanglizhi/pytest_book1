# Author: lindafang
# Date: 2020-10-04 10:55
# File: login_locators.py

# 登陆页元素 定位方式
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    # 登陆用户名的元素定位，采用元组形式，通过id定位
    username_text = (By.ID, "txtUsername")
    password_text = (By.ID, "txtPassword")
    login_submit = (By.ID, "btnLogin")
