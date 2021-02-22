# Author: lindafang
# Date: 2020-10-08 16:47
# File: test_tag_method.py

import pytest
import requests

from utils.read_yml import get_yaml_data

# 读取数据文件
create_tag_data = get_yaml_data("tag_data.yaml")


# 使用参数化方式执行多次
@pytest.mark.parametrize('value', create_tag_data)
def test_create_tag(get_access_token, value):
    url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=' \
          + get_access_token

    data = {"tag": {"name": value}}
    rep = requests.post(url=url, json=data)
    assert rep.status_code == 200
    assert rep.json()['tag']['name'] == value


@pytest.fixture()
def get_tag(get_access_token):
    url = 'https://api.weixin.qq.com/cgi-bin/tags/get?access_token=' \
          + get_access_token
    rep = requests.get(url=url)
    #     从这个返回中获取最后1个id号
    ids = rep.json()['tags'][-1]['id']
    # 获取倒数第2个id号
    ids1 = rep.json()['tags'][-2]['id']
    ides = []
    ides.append(ids)
    ides.append(ids1)
    assert rep.status_code == 200
    assert 'tags' in rep.text
    return ides


def test_update_tag(get_access_token, get_tag):
    url = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token=' \
          + get_access_token
    data = {"tag": {"id": get_tag[0], "name": "只觉388"}}
    data1 = {"tag": {"id": get_tag[1], "name": "zenm338"}}
    rep = requests.post(url=url, json=data)
    assert rep.status_code == 200
    assert rep.json()['errcode'] == 0
    rep1 = requests.post(url=url, json=data1)
    assert rep1.status_code == 200
    assert rep1.json()['errcode'] == 0


def test_udelete_tag(get_access_token, get_tag):
    url = 'https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=' \
          + get_access_token
    print(get_tag)
    data = {"tag": {"id": get_tag[0]}}
    data1 = {"tag": {"id": get_tag[1]}}
    rep = requests.post(url=url, json=data)
    assert rep.status_code == 200
    assert rep.json()['errcode'] == 0
    rep1 = requests.post(url=url, json=data1)
    assert rep1.status_code == 200
    assert rep1.json()['errcode'] == 0


if __name__ == '__main__':
    pytest.main()
