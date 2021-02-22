# Author: lindafang
# Date: 2020-10-08 16:22
# File: test_create_tag.py
import allure
import pytest
import requests


@allure.feature("获得token")
@allure.step("获得所有接口的入门证书token")
def access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?' \
          'grant_type=client_credential&appid=wx7007dc5642cc0a80&secret=903b6bb501713b6e22db74342003a5a9'

    allure.attach("发送get请求")
    rep = requests.get(url)
    allure.attach("断言响应状态码为200")
    assert 200 == rep.status_code
    rep_json = rep.json()
    allure.attach("断言返回具体业务信息")
    assert 7200 == rep_json['expires_in']
    return rep_json['access_token']


# 正确的创建标签用例1
@allure.feature("正确的创建标签")
@allure.story("全正确创建")
@allure.testcase("用例1")
def test_createtag(get_access_token):
    url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=' + get_access_token
    allure.attach("数据准备")
    data = {"tag": {"name": "linda708090"}}
    allure.attach("发送post请求")
    rep = requests.post(url=url, json=data)
    allure.attach("断言响应状态码为200")
    assert 200 == rep.status_code
    # json_rep=rep.json()
    allure.attach("断言请求响应全部时间小于3秒")
    assert rep.elapsed.total_seconds() < 3
    allure.attach("断言返回具体业务信息")
    # assert 'linda708090' ==json_rep['tag']['name']


# 创建错误token用例7
@allure.feature("错误的创建标签")
@allure.story("错误token")
@allure.testcase("http://jira.com/weixin/tag/testcase/7", "用例7")
def test_createtag_F_errortoken():
    url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=1111'
    allure.attach("发送get请求")
    rep = requests.get(url)
    allure.attach("断言响应状态码为200")
    assert 200 == rep.status_code
    allure.attach("断言返回具体业务码")
    assert 40001 == rep.json()['errcode']


if __name__ == '__main__':
    pytest.main(['-s', 'test_create_tag.py'])
