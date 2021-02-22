# Author: lindafang
# Date: 2020-05-13 23:29
# File: test_failed.py

import pytest


@pytest.mark.parametrize('num', [1, 2])
def test_failed(num):
    assert num == 1
