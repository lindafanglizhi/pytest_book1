# Author: lindafang
# Date: 2020-08-14 08:55
# File: test_add_note_pytest.py
from datetime import datetime

import allure
import pytest
import yaml

from pageobject import addnotepage
from utils.get_path import PATH


@allure.feature("笔记功能")
class TestNotePytest(object):
    @allure.step("初始化，打开手机，同意权限")
    @pytest.fixture(scope='module', autouse=True)
    def agree_init(self, run_app):
        # 初始化driver，文件级通用
        # 先初始化页面，
        ok = addnotepage.FirstOpenPage(run_app)
        # 操作的方法
        ok.permission_allowandok()

    @allure.story("添加笔记功能")
    @pytest.mark.regression
    @allure.severity("critical")
    @pytest.mark.parametrize("add",
                             yaml.safe_load(open(PATH("../Testdatas/" + "addnotedata.yaml"), 'r', encoding='utf8')))
    def test_addnote(self, add, run_app):
        note_title = add
        # 初始化添加笔记页
        with allure.step("初始化添加页面"):
            addnote = addnotepage.AddNotePage(run_app)
        # # 添加标题和内容
        addnote.add_note_ok(note_title)
        # # 截图
        addnote.save_pic(PATH("../shotpicture/" + str(datetime.now())) + "addnote.png")

    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_deletenote(self):
        pass


if __name__ == '__main__':
    pytest.main()
