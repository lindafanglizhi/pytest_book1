# Author: lindafang
# Date: 2020-05-05 23:38
# File: test_nodeid.py

import pytest


def test_one():
    print('test_one')
    assert 1


class TestNodeId:
    def test_one(self):
        print('TestNodeId::test_one')
        assert 1

    # 这里是参数化，在第4章中详细讲
    # 循环执行两遍，第一遍取x=1  y=1，第二遍取x=3,y=4
    @pytest.mark.parametrize('x,y', [(1, 1), (3, 4)])
    def test_two(self, x, y):
        print(f'TestNodeId::test_two::{x} == {y}')
        assert x == y
