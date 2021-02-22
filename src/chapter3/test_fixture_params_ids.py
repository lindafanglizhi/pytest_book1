# Author: lindafang
# Date: 2020-05-16 14:25
# File: test_fixture_params_ids.py
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(params=[0, 'a'], ids=['number', 'charactor'])
def a(request):
    return request.param


def test_a(a):
    print(a)
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    elif fixture_value == 1:
        return False
    elif fixture_value == 2:
        return None
    else:
        return fixture_value


@pytest.fixture(params=[0, 1, 2, 3], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    print(b)
    pass


class C:
    pass


@pytest.fixture(params=[(1, 2), {'d': 1}, C()])
def c(request):
    return request.param


def test_c(c):
    print(c)
    pass
