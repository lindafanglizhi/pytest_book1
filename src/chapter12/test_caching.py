#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: linda

import logging

import pytest


def expensive_computation():
    print("运行一个大数据量的计算...")


@pytest.fixture
def mydata(request):
    # 从缓存中读取数据
    val = request.config.cache.get("bigdata/value", None)
    if val is None:
        val = 18
        # 如果缓存中没有，设置缓存中的值
        request.config.cache.set("bigdata/value", val)
    expensive_computation()
    return val


def test_function(mydata):
    logging.info("这是测试是否能写入文件")
    assert mydata == 18
