# Author: lindafang
# Date: 2020-05-09 16:22
# File: test_module_skip_2.py

from .test_module_skip_1 import minversion


@minversion
def test_two():
    assert True
