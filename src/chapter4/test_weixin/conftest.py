# # Author: lindafang
# # Date: 2020-11-03 15:49
# # File: conftest.py
import pytest
import requests


#
# # scope =session整个session使用一个fixture,token
# # scope  =function每个函数使用一个fixture,token
# # scope class,整个类使用一个fixture,token
@pytest.fixture(scope='session')
def get_access_token1():
    get_url = 'https://api.weixin.qq.com/cgi-bin/token'
    params = {'grant_type': 'client_credential',
              'appid': 'wxd8e5ab621f5d6902',
              'secret': '2dbfc49b5beb5f40d001646bee7cba28'
              }
    res = requests.get(url=get_url, params=params)
    res_json = res.json()
    return res_json['access_token']
