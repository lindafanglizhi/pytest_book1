# Author: lindafang
# Date: 2020-11-25 14:04
# File: code.py
import os


def get_os_user_lower():
    username = os.getenv("USER")

    if username is None:
        raise OSError("用户环境还没设置.")

    return username.lower()
