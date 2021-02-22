# Author: lindafang
# Date: 2020-05-09 16:48
# File: test_import_minversion.py
import pytest

csv1 = pytest.importorskip("csv", minversion="2.0")


@csv1
def test_import_minversion():
    pass
