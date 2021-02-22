#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: lindafang
# Created Date: 2020-10-30 11:25:43


import warnings

import pytest


# pytestmark = pytest.mark.filterwarnings("error")

def api_v1():
    warnings.warn(UserWarning('请使用新版本的API。'))
    return 1


def api_v2():
    warnings.warn(UnicodeWarning('未转换成汉语'))
    return 2


def test_one():
    assert api_v1() == 1


@pytest.mark.filterwarnings('ignore::UserWarning')
# @pytest.mark.filterwarnings('ignore::UnicodeWarning')
def test_two():
    assert api_v1() == 1
    assert api_v2() == 2
