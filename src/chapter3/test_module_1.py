# Author: lindafang
# Date: 2020-12-01 11:22
# File: test_module_1.py


def test_ehlo(smtp_connection):
    response, _ = smtp_connection.ehlo()
    assert response == 250
    smtp_connection.extra_attr = 'test'
    assert 0  # 为了展示，强制置为失败


def test_noop(smtp_connection):
    response, _ = smtp_connection.noop()
    assert response == 250
    assert smtp_connection.extra_attr == 0  # 为了展示，强制置为失败
