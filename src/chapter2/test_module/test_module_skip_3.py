# Author: lindafang
# Date: 2020-05-09 20:45
# File: test_module_skip_3.py

import pytest

# pytestmark = pytest.mark.skip('作用于模块中的每一个用例，所以 pytest 共收集到两个 SKIPPED 的用例。')

pytest.skip('在用例收集阶段就已经跳出了，所以不会收集到任何用例。', allow_module_level=True)


def test_one():
    assert True


def test_two():
    assert True
