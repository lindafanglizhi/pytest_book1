# Author: lindafang
# Date: 2020-10-05 14:55
# File: test_attach_fixture_finalizer.py
import allure
import pytest


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('这个文本的附件是文件级的', '这可以是文件名字', allure.attachment_type.TEXT)

    def finalizer_module_scope_fixture():
        allure.attach('这个文本的附件是文件级的结束部分', '下面调用finializer',
                      allure.attachment_type.TEXT)

    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_fixture_with_finalizer):
    print("这是通过fixture调用上面的步骤，步骤中包含结束finalizer调用")
    pass
