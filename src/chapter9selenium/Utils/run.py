# Author: lindafang
# Date: 2020-08-09 15:40
# File: run.py

import pytest

# shell:
# pytest test_selenium_driver.py  --driver Chrome --driver-path /Users/lindafang/PycharmProjects/SeleniumAutoDemo/driver/chromedriver

if __name__ == '__main__':
    pytest.main(['test_selenium_driver.py', '--driver', 'Chrome', '--driver-path',
                 '/Users/lindafang/PycharmProjects/SeleniumAutoDemo/driver/chromedriver'])
    # pytest.main(['test_selenium_driver.py','--driver','Safari','--driver-path','/Users/lindafang/PycharmProjects/SeleniumAutoDemo/driver/safaridriver'])
    # Safari的可执行文件位于/usr/bin/safaridriver。
    # Safari对开发人员的WebDriver支持默认情况下处于关闭状态。如何启用它取决于您的操作系统。
    # 请使“开发”菜单可用。选择Safari>首选项，然后在“高级”选项卡上，选择“在菜单栏中显示开发菜单”。有关详细信息，请参见Safari帮助。
    # 选择“开发>允许远程自动化”。
