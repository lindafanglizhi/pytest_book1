# Author: lindafang
# Date: 2020-05-09 16:22
# File: test_module_skip_2.py

import sys

import pytest

minversion = pytest.mark.skipif(sys.version_info < (3, 8),
                                reason='请使用 python 3.8 或者更高的版本。')


@minversion
def test_one():
    assert True
