# Author: lindafang
# Date: 2020-08-13 11:36
# File: addnotepage.py
from .basepage import BasePage
from .locators import AddNotePageLoacators
from .locators import FirstOpenPageLocators


class FirstOpenPage(BasePage):
    # 继承的：BasePage是我的父类，父类中的所有方法我都能用。

    def permission_allowandok(self):
        BasePage.click_thing(self, FirstOpenPageLocators.btn_ok)
        BasePage.click_thing(self, FirstOpenPageLocators.btn_ok)
        BasePage.click_thing(self, FirstOpenPageLocators.permission_allow)


class AddNotePage(BasePage):
    def add_note_ok(self, title):
        BasePage.click_thing(self, AddNotePageLoacators.add_note)
        BasePage.click_thing(self, AddNotePageLoacators.add_icon)
        BasePage.set_value(self, AddNotePageLoacators.note_title, title)
        # self.driver.press_keycode(66)
        # BasePage.set_value(self, AddNotePageLoacators.note_editText, editText)
        BasePage.click_thing(self, AddNotePageLoacators.submit_complete)
