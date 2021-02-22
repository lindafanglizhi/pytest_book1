# Author: lindafang
# Date: 2020-05-09 14:20
# File: test_windows_skip_1.py


'''
sys.platform返回值
系统	         返回值
window	：  ’win32‘
linux   ：	’linux‘
Windows/Cygwin	：‘cygwin’
Mac OS X	：‘darwin’  本机是这个

'''
import sys

import pytest


def test_login():
    pytest.skip("跳出", allow_module_level=True)
    assert 'linda' == 'linda'


# 如果参数换成win32就是mac不执行，windows执行。
# 大家更换一下试试。
# if not sys.platform.startswith("win32"):
#
#     print(sys.platform)
#     # pytest.skip("如果不是mac系统，就跳过不执行，"
#     #             "如果是mac，执行，因为后面参数是模块级所以是整个文件的用例", allow_module_level=True)
#     pytest.skip("如果不是win系统，就跳过不执行，"
#                 "如果是win，执行，因为后面参数是模块级所以是整个文件的用例", allow_module_level=True)


def f():
    print("\n" + sys.platform)
    return 3


def test_cakan():
    assert f() == 4


def test_2():
    print("看这个用例是不是也执行，当参数是win32时不执行")
    pass
