# Author: lindafang
# Date: 2020-05-07 15:05
# File: conftest.py
import smtplib

import pytest


@pytest.fixture()
def login():
    print("\n用户名linda密码登陆！")


@pytest.fixture(scope='module')
def smtp_connection():
    return smtplib.SMTP("smtp.163.com", 25, timeout=5)
