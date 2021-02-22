# Author: lindafang
# File: test_assert_skip_2.py
import sys

import pytest

environment = 'android'


@pytest.mark.skipif('environment=="android"', reason='android平台没有这个功能')
def test_cart_3():
    pass


@pytest.mark.skipif(sys.platform == 'win32', reason='不在windows下运行')
@pytest.mark.skipif(sys.version_info < (3, 6), reason='3.6版本以下不执行，您需要更高版本')
def test_cart():
    print("python版本大于等于3.6执行，windows下不执行")
    pass
