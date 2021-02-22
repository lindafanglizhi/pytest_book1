# Author: lindafang
# Date: 2020-10-04 15:12
# File: add_jobtitle_method.py

# 相对位置调用
# from .login_locators import LoginPageLocators
from pages.base_public_method import BasePage
from pages.job_title_locators import JobTitlePageLocators
from pages.main_locators import MainPageLocators
# 绝对地 址调用，默认路径工程路径
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddJobtitlePage(BasePage):
    # 0进入job页
    def click_movetoelement_job(self):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*MainPageLocators.menu_admin_viewAdminModule_btn))
        # 可以通过链式方式解决鼠标悬停功能
        # ActionChains(self.driver)\
        #     .move_to_element(self.driver.find_element(*MainPageLocators.menu_admin_viewAdminModule_btn))\
        #     .move_to_element(self.driver.find_element(*MainPageLocators.menu_admin_viewJobTitleList))\
        #     .click(self.driver.find_element(*MainPageLocators.menu_admin_Job)).perform()
        # 也可通过一步步点击方式进入
        self.driver.find_element(*MainPageLocators.menu_admin_viewAdminModule_btn).click()
        self.driver.find_element(*MainPageLocators.menu_admin_Job).click()
        self.driver.find_element(*MainPageLocators.menu_admin_viewJobTitleList).click()

    # 方法
    # 1、点击添加jobtitle的按钮
    def click_add_jobtitle(self):
        element_click = self.driver.find_element(*JobTitlePageLocators.btnAdd_btn)
        element_click.click()

    # 2、输入jobtitle
    def enter_jobTitle(self, jobtitle):
        #    智能等待这个元素加载上， 点击，清除，输入,为什么*，参数是元组（By.ID,""）拆开
        #     等待用户名这个文本框加载上
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*JobTitlePageLocators.jobTitle_jobTitle_text))
        # 用户名元素定位
        element = self.driver.find_element(*JobTitlePageLocators.jobTitle_jobTitle_text)
        # 点击一下
        element.click()
        # 清空文本框
        element.clear()
        # 输入传入的内容
        element.send_keys(jobtitle)

    # 2、输入jobDescription
    def enter_jobDescription(self, description):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*JobTitlePageLocators.jobTitle_jobDescription_text))
        element = self.driver.find_element(*JobTitlePageLocators.jobTitle_jobDescription_text)
        element.clear()
        element.send_keys(description)

    # 3、输入上传文件名jobTitle_jobSpec_upload
    def enter_jobSpec_upload(self, upload_filename):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*JobTitlePageLocators.jobTitle_jobSpec_upload))
        element = self.driver.find_element(*JobTitlePageLocators.jobTitle_jobSpec_upload)
        element.clear()
        element.send_keys(upload_filename)

    # 4、输入注释文本note_text
    def enter_note_text(self, note_text):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*JobTitlePageLocators.jobTitle_note_text))
        element = self.driver.find_element(*JobTitlePageLocators.jobTitle_note_text)
        element.clear()
        element.send_keys(note_text)

    # 5、点击添加jobtitle

    def click_addjobtitle_submit(self):
        element_click = self.driver.find_element(*JobTitlePageLocators.btnSave_submit)
        element_click.click()

    # 6、返回要验证的文本，登陆成功
    def result_addjobtitle_sucess(self):
        # 验证 欢迎 Admin（text）出现   presene_of_element_located(locator),locator需要元组格式
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(MainPageLocators.welcome_link))
        return self.driver.find_element(*MainPageLocators.welcome_link).text
