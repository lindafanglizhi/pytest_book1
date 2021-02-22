# Author: lindafang
# Date: 2020-11-25 13:59
# File: conftest.py
import pytest


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")
