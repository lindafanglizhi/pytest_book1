# Author: lindafang
# Date: 2020-11-17 16:35
# File: test_ids.py

import pytest


@pytest.mark.parametrize('input, expected', [
    pytest.param(1, 2, id='Windows'),
    pytest.param(3, 4, id='Windows'),
    pytest.param(5, 6, id='Non-Windows')
])
def test_ids_with_ids(input, expected):
    pass


# 不好用，都执行。
if __name__ == '__main__':
    pytest.main(['-k', 'Non-Windows', 'test_ids.py'])
