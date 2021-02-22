# Author: lindafang
# Date: 2020-11-25 13:50
# File: test_app_fixture.py
import pytest
import requests

# app.py 有 get_json()方法
import app


class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


def test_get_json(mock_response):
    result = app.get_json("https://172.10.1.125")
    assert result["mock_key"] == "mock_response"


import functools


def test_partial(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(functools, "partial", 3)
        assert functools.partial == 3


@pytest.fixture
def mock_test_user(monkeypatch):
    monkeypatch.setitem(app.DEFAULT_CONFIG, "user", "test_user")


@pytest.fixture
def mock_test_database(monkeypatch):
    monkeypatch.setitem(app.DEFAULT_CONFIG, "database", "test_db")


@pytest.fixture
def mock_missing_default_user(monkeypatch):
    monkeypatch.delitem(app.DEFAULT_CONFIG, "user", raising=False)


def test_connection(mock_test_user, mock_test_database):
    expected = "User Id=test_user; Location=test_db;"

    result = app.create_connection_string()
    assert result == expected


def test_missing_user(mock_missing_default_user):
    with pytest.raises(KeyError):
        _ = app.create_connection_string()
