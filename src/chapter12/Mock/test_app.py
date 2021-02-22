# Author: lindafang
# Date: 2020-11-25 13:22
# File: test_app.py
import pytest
import requests

import app


# 这是模拟类，返回响应
class MockResponse:

    # 模拟返回方法及返回值
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):
    # 任何参数都会返回这个模拟类
    def mock_get(*args, **kwargs):
        return MockResponse()

    # 应用 monkeypatch 替换requests.get为 模拟 mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, 包括 requests.get, 应用 monkeypatch
    result = app.get_json("https://172.10.1.125")
    assert result["mock_key"] == "mock_response"


def test_connection(monkeypatch):
    # 为测试设置默认值
    monkeypatch.setitem(app.DEFAULT_CONFIG, "user", "test_user")
    monkeypatch.setitem(app.DEFAULT_CONFIG, "database", "test_db")

    # 基于模拟设置预期结果
    expected = "User Id=test_user; Location=test_db;"

    # 调用，断言
    result = app.create_connection_string()
    assert result == expected


def test_missing_user(monkeypatch):
    # user这个默认的配置属性删除
    monkeypatch.delitem(app.DEFAULT_CONFIG, "user", raising=False)
    # Key error expected because a config is not passed, and the
    # default is now missing the 'user' entry.
    # expected = "User Id=test_user; Location=test_db;"
    with pytest.raises(KeyError):
        _ = app.create_connection_string()
    # result=app.create_connection_string()
    # assert result == expected
