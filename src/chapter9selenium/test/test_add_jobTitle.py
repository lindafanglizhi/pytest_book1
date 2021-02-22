# Author: lindafang
# Date: 2020-10-07 22:41
# File: test_add_jobTitle.py
import os
from datetime import datetime

import allure
import pytest
from pages.add_jobtitle_method import AddJobtitlePage
from pages.base_public_method import BasePage
from pages.login_method import LoginPage

from ..Utils.get_path import get_par_path
from ..Utils.log import conf
from ..Utils.read_yml import get_yaml_data

with allure.step("0、从数据文件中读取职称添加数据信息"):
    yaml_path = os.path.join(get_par_path(), "datafile/addjob_data.yaml")
    test_data = get_yaml_data(yaml_path)


class TestClass(object):

    @allure.step("从配置文件中读取登陆数据")
    @pytest.fixture()
    def login_data(self):
        self.log = conf.logcon()
        self.log.info("read config.yaml")
        yaml_path = os.path.join(get_par_path(), "config/config.yaml")
        test_data = get_yaml_data(yaml_path)
        return test_data

    @allure.feature("登陆功能")
    @allure.step("使用管理员身份登陆")
    def test_login(self, init_driver, login_data):
        self.log.info("login")
        init_driver.get(login_data['baseurl'] + "/symfony/web/index.php/auth/login")
        init_driver.maximize_window()
        init_driver.implicitly_wait(30)
        base_page = BasePage(init_driver)
        with allure.step("初始化登陆页"):
            login_page = LoginPage(init_driver)
        with allure.step("输入用户名密码点击登陆"):
            login_page.enter_username(login_data['username'])
            login_page.enter_password(login_data['password'])
            login_page.click_login()
        with allure.step("断言admin是否登陆成功并截图"):
            assert 'Admin' in login_page.result_login_sucess()
            pic_path = os.path.join(get_par_path(), "shootpicture/")
            base_page.save_picture(pic_path + str(datetime.now()) + 'login.png')

    @allure.step("0、这是初始化数据")
    @pytest.fixture()
    def get_data(self, request):
        value = request.param
        return value

    @allure.feature("添加职称功能")
    @pytest.mark.parametrize("get_data", test_data, indirect=True)
    def test_2add_jobtitle(self, init_driver, get_data):
        job = get_data['case']
        jobTitle = job["jobTitle"]
        jobDescription = job["jobDescription"]
        note_text = job["note_text"]
        base_page = BasePage(init_driver)
        addjobtitle_page = AddJobtitlePage(init_driver)
        with allure.step("1、进入职称页"):
            addjobtitle_page.click_movetoelement_job()
            addjobtitle_page.click_add_jobtitle()
        with allure.step("2、输入信息"):
            addjobtitle_page.enter_jobTitle(jobTitle)
            addjobtitle_page.enter_jobDescription(jobDescription)
        with allure.step("3、上传文件"):
            data_path = os.path.join(get_par_path(), "datafile")
            addjobtitle_page.enter_jobSpec_upload(data_path + "/upload.log")
        with allure.step("4、提交保存"):
            addjobtitle_page.enter_note_text(note_text)
            addjobtitle_page.click_addjobtitle_submit()
        with allure.step("5、断言添加成功并截图"):
            assert jobTitle in init_driver.page_source
            pic_path = os.path.join(get_par_path(), "shootpicture/")
            pic_name = pic_path + str(datetime.now()) + '_addjob.png'
            base_page.save_picture(pic_name)
            allure.attach.file(pic_name, attachment_type=allure.attachment_type.PNG)
