# Author: lindafang
# Date: 2020-08-13 11:23
# File: locators.py

from appium.webdriver.common.mobileby import MobileBy


class FirstOpenPageLocators(object):
    btn_ok = (MobileBy.ID, "com.youdao.note:id/btn_ok")
    permission_allow = (MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")


class AddNotePageLoacators(object):
    add_note = (MobileBy.ID, "com.youdao.note:id/add_note")
    add_icon = (MobileBy.ID, "com.youdao.note:id/add_icon")
    note_title = (MobileBy.ID, "com.youdao.note:id/note_title")
    # note_editText = (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
    #                                /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText
    # // android.widget.EditText
    note_editText = (MobileBy.XPATH, "//android.widget.EditText")
    submit_complete = (MobileBy.ID, "com.youdao.note:id/actionbar_complete_text")
