# Author: lindafang
# Date: 2020-11-18 13:38
# File: test_tmpdir_Factory.py
import pyautogui
import pytest


@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    img = pyautogui.screenshot(region=[0, 0, 100, 100])  # x,y,w,h
    fn = tmpdir_factory.mktemp("data").join("img.png")
    img.save(str(fn))
    return fn


def test_histogram(image_file):
    print(image_file)


def test_histogram1(image_file):
    print(image_file)
