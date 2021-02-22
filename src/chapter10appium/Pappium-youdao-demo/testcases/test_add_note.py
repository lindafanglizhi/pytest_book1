# Author: lindafang
# Date: 2020-08-13 11:55
# File: test_add_note.py

import unittest
from datetime import datetime

from appium import webdriver
from ddt import ddt, data

from pageobject import addnotepage
from utils import desired_caps
from utils.get_csvdata import get_csv_data
from utils.get_path import PATH


@ddt
class TestNote(unittest.TestCase):
    datafile = PATH("../Testdatas/addnotedata.csv")
    print(datafile)

    @classmethod
    def setUpClass(cls):
        desired_cap_value = desired_caps.get_desired_caps()
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap_value)
        # 先初始化页面，
        ok = addnotepage.FirstOpenPage(cls.driver)
        # 操作的方法
        ok.permission_allowandok()

    @classmethod
    def tearDownClass(cls):
        # 关闭app
        cls.driver.quit()

    # def test_addNote_nodate(self):
    #     # 初始化添加笔记页面
    #     add_note=addnotepage.AddNotePage(self.driver)
    #     add_note.save_pic("/Users/lindafang/PycharmProjects/Pappium-youdao-demo/shotpicture/"+str(datetime.now()) + "addnote.png")
    #     add_note.add_note_ok("这是笔记的标题","我今天很开心，跟大家共同渡过！")

    @data(*get_csv_data(datafile))
    def test_addNote(self, value):
        daily_title = value[0]
        daily_text = value[1]
        # 先初始化添加日记的页面
        addnote = addnotepage.AddNotePage(self.driver)
        addnote.add_note_ok(daily_title, daily_text)
        addnote.save_pic(PATH("../shotpicture/" + str(datetime.now())) + "addnote.png")
        # 这里少断言，先在页面找到要断言的元素，在locator中加入元素。
        # 在封装的方法中加入属性值 的获取，在这里加断言
        assert 1

    def test_edit_note(self):
        pass

    def test_delete_note(self):
        pass


if __name__ == '__main__':
    unittest.main()
