# Author: lindafang
# Date: 2020-05-09 16:48
# File: test_importorskip.py
import pytest

docutils = pytest.importorskip("docutils")


@docutils
def test_importorskip():
    pass


def test_severn():
    print("7")
