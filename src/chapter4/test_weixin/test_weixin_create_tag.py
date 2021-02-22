# Author: lindafang
# Date: 2020-11-03 15:28
# File: test_weixin_create_tag.py
import pytest
import requests
import yaml


@pytest.mark.parametrize('create',
                         yaml.safe_load(open('data/test_weixin_create_tag.yaml', 'r', encoding='utf8')))
def test_create_tag(get_access_token1, create):
    url = create['url'] + get_access_token1
    json_data = create['data']
    result = create['result']['name']
    res = requests.post(url, json=json_data)
    assert res.status_code == 200
    assert res.json()['tag']['name'] == result
