# Author: lindafang
# Date: 2020-11-17 09:09
# File: test_markers.py
import pytest


@pytest.mark.web
def test_pass():
    print("web")
    assert 1


@pytest.mark.app
def test_new_pass():
    print("app")
    assert 1


@pytest.mark.p0
def test_new_mark():
    print("p0")
    assert 1
