# Author: lindafang
# Date: 2020-10-22 11:48
# File: test_interface_api.py

import requests

from pytest_bdd import scenarios, given, then, parsers

# Shared Variables
HRM_API = 'https://cn.bing.com/search'

# Scenarios

scenarios('../features/interface_api.feature', example_converters=dict(phrase=str))


# Given Steps

@given('查询关键字 "<phrase>"')
def ddg_response(phrase):
    params = {'q': phrase, 'cvid': '214DA874AFE04224A1125033896419D2'}
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    response = requests.get(HRM_API, params=params, headers=headers)
    return response


# Then Steps

@then('结果包含 "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    assert phrase in ddg_response.text


@then(parsers.parse('响应状态码是 "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code
