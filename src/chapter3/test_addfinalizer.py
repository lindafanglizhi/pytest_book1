# Author: lindafang
# Date: 2020-08-11 13:54
# File: test_addfinalizer.py

import pytest


@pytest.fixture()
def demo_fixture(request):
    print("\n这个fixture在每个case前执行一次")

    def demo_finalizer():
        print("\n在每个case完成后执行的teardown")

    # 注册demo_finalizer为终结函数
    request.addfinalizer(demo_finalizer)


def test_01(demo_fixture):
    print("\n===执行了case: test_01===")


def test_02(demo_fixture):
    print("\n===执行了case: test_02===")


def test_03(demo_fixture):
    print("\n===执行了case: test_03===")
