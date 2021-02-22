# Author: lindafang
# Date: 2020-12-01 12:51
# File: test_request.py

import smtplib

import pytest


@pytest.fixture(scope='module', params=['smtp.163.com', 'smtp.126.com', "mail.python.org"])
def smtp_connection_params(request):
    server = request.param
    with smtplib.SMTP(server, 587, timeout=5) as smtp_connection:
        yield smtp_connection


def test_parames(smtp_connection_params):
    response, _ = smtp_connection_params.ehlo()
    assert response == 250
