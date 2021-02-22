# Author: lindafang
# Date: 2020-08-13 11:18
# File: desired_caps.py
from utils.get_path import PATH


def get_desired_caps():
    desired_caps = {
        "platformName": "android",
        "deviceName": "emulator-5554",
        # "platformVersion": "6.0",
        "app": PATH("../Papp/youdaonote_android_6.7.18_youdaoweb.apk"),
        # "unicodeKeyboard": True,
        # "resetKeyboard":False,
    }
    return desired_caps
