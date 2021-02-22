# Author: lindafang
# Date: 2020-10-06 10:37
# File: test_reruns.py
import random
import time

import allure


@allure.step
def passing_step():
    pass


@allure.step
def flaky_broken_step():
    if random.randint(1, 5) != 1:
        raise Exception('Broken!崩溃了')


def test_broken_with_randomized_time():
    passing_step()
    time.sleep(random.randint(1, 3))
    flaky_broken_step()
