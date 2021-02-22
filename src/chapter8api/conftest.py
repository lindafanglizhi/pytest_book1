# Author: lindafang
# Date: 2020-10-08 16:49
# File: conftest.py
import pytest
import requests


@pytest.fixture(scope='session')
def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?' \
          'grant_type=client_credential&appid=wx7007dc5642cc0a80&secret=903b6bb501713b6e22db74342003a5a9'
    rep = requests.get(url)
    return rep.json()['access_token']
