# Author: lindafang
# Date: 2020-08-11 14:10
# File: test_addfinalizer02.py
import pytest


@pytest.fixture()
def demo_fixture(request):
    print("\n这个fixture在每个case前执行一次")

    def demo_finalizer():
        print("\n在每个case完成后执行的teardown")

    def demo_finalizer2():
        print("\n在每个case完成后执行的teardown2")

    def demo_finalizer3():
        print("\n在每个case完成后执行的teardown3")

    # 注册demo_finalizer为终结函数
    request.addfinalizer(demo_finalizer)
    request.addfinalizer(demo_finalizer2)
    request.addfinalizer(demo_finalizer3)


def test_01(demo_fixture):
    print("\n===执行了case: test_01===")


def test_02(demo_fixture):
    print("\n===执行了case: test_02===")


def test_03(demo_fixture):
    print("\n===执行了case: test_03===")
