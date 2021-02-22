# Author: lindafang
# Date: 2020-11-03 16:00
# File: test_weixin_update_tag.py
import pytest
import requests
import yaml


@pytest.fixture(scope='session', params=yaml.safe_load(open('data/test_weixin_get_tags.yaml', 'r', encoding='utf8')))
def test_get_tags(get_access_token1, request):
    get_url = request.param['url'] + get_access_token1
    name = request.param['result']['name']
    res = requests.get(get_url)
    res_json = res.json()
    assert res.status_code == 200
    assert name == res_json['tags'][0]['name']
    return res_json['tags'][-1]['id']


@pytest.mark.parametrize('update', yaml.safe_load(open('data/test_weixin_update_tag.yaml', 'r', encoding='utf8')))
def test_update_tag(get_access_token1, test_get_tags, update):
    url = update['url'] + get_access_token1
    data = update['data']
    code = update['result']['errcode']
    data['tag']['id'] = test_get_tags
    res = requests.post(url, json=data)
    assert res.status_code == 200
    # print(res.json())
    assert res.json()['errcode'] == code


@pytest.mark.parametrize('delete',
                         yaml.safe_load(open('data/test_weixin_delete_tag.yaml', 'r', encoding='utf8')))
def test_delete_tag(get_access_token1, delete, test_get_tags):
    url = delete['url'] + get_access_token1
    json_data = delete['data']
    json_data['tag']['id'] = test_get_tags
    result = delete['result']
    res = requests.post(url, json=json_data)
    assert res.status_code == 200
    assert res.json() == result
