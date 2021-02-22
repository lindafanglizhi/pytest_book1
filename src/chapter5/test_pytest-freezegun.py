# Author: lindafang
# Date: 2020-07-14 16:08
# File: test_pytest-freezegun.py

import time
from datetime import datetime, date

import pytest


def test_frozen_date(freezer):
    now = datetime.now()
    time.sleep(1)
    later = datetime.now()
    assert now == later


def test_moving_date(freezer):
    now = datetime.now()
    freezer.move_to('2017-05-20')
    later = datetime.now()
    assert now != later


@pytest.mark.freeze_time('2017-05-21')
def test_current_date():
    assert date.today() == date(2017, 5, 21)


@pytest.fixture
def current_date():
    return date.today()


@pytest.mark.freeze_time
def test_changing_date(current_date, freezer):
    freezer.move_to('2017-05-20')
    assert current_date == date(2017, 5, 20)
    freezer.move_to('2017-05-21')
    assert current_date == date(2017, 5, 21)
