# Author: lindafang
# Date: 2020-05-13 17:47
# File: test_main_plugin.py
import pytest


class MyPlugin:
    def pytest_sessionfinish(self):
        import allure
        allure.title("我导入了allure")
        print("allure test run reporting finishing")


if __name__ == '__main__':
    # 静默执行，并且不显示测试用例的收集结果消息
    # 因为没选择要执行的文件，执行的范围是你配置的path所在的范围
    pytest.main(["-qq"], plugins=[MyPlugin()])
