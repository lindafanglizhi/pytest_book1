# Author: lindafang
# Date: 2020-08-04 10:55
# File: login_locators.py
# 主页元素 定位方式
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    welcome_link = (By.ID, "welcome")
    menu_admin_viewAdminModule_btn = (By.ID, "menu_admin_viewAdminModule")
    menu_admin_Job = (By.ID, "menu_admin_Job")
    menu_admin_viewJobTitleList = (By.ID, "menu_admin_viewJobTitleList")
