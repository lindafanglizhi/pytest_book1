# Author: lindafang
# Date: 2020-10-04 10:56
# File: job_title_locators.py
# 职称添加页元素定位
from selenium.webdriver.common.by import By


class JobTitlePageLocators(object):
    # 可以使用id定位，也可以换成XPATH定位，XPATH的编写技术可网上搜索XPATH定位
    btnAdd_btn = (By.XPATH, "//*[@id='btnAdd']")
    # btnAdd_btn = (By.ID, "btnAdd")
    jobTitle_jobTitle_text = (By.ID, "jobTitle_jobTitle")
    jobTitle_jobDescription_text = (By.ID, "jobTitle_jobDescription")
    jobTitle_jobSpec_upload = (By.ID, "jobTitle_jobSpec")
    jobTitle_note_text = (By.ID, "jobTitle_note")
    btnSave_submit = (By.ID, "btnSave")
