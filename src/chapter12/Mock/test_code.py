# Author: lindafang
# Date: 2020-11-25 14:08
# File: test_code.py

import pytest

from code import get_os_user_lower


def test_upper_to_lower(monkeypatch):
    monkeypatch.setenv("USER", "TestingUser")
    assert get_os_user_lower() == "testinguser"


def test_raise_exception(monkeypatch):
    monkeypatch.delenv("USER", raising=False)

    with pytest.raises(OSError):
        _ = get_os_user_lower()
