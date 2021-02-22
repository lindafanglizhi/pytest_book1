# Author: lindafang
# File: test_markers.py
"""
Markers 可以实现选择某个方法测试或不选择哪些方法测试。

命令行:

pytest -v test_markers.py
pytest -v -m 'p0' test_markers.py
pytest -v -m 'not p0' test_markers.py
pytest -v -m 'not p0 and not func' test_markers.py
pytest -v -m 'func or postgres' test_markers.py

"""
import pytest


# @pytest是一组装饰器的方法，用于在测试方法加一些功能，这将细节将在下一章中详细讲解
# 通过pytest中的mark标记标注每个测试方法的一些含义
@pytest.mark.p0
def test_something_p0():
    pass


@pytest.mark.func
def test_something_func():
    pass


@pytest.mark.postgres
def test_something_postgres():
    pass
