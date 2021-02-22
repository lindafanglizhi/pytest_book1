#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: lindafang

import pytest


def api_call_v1():
    # warnings.warn('v1版本已废弃，请使用v2版本的api；', DeprecationWarning)
    return 200


def test_deprecation():
    assert pytest.deprecated_call(api_call_v1) == 200


def test_deprecation1():
    with pytest.warns(Warning) as records:
        rsp = api_call_v1()
        if not records:
            pytest.fail('期望 api_call_v1 触发一个警告，实际上没有；')
        assert rsp == 200
