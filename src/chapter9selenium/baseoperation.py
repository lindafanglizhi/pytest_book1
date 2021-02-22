# Author: lindafang
# Date: 2020-10-03 10:00
# File: baseoperation.py

import time

from selenium import webdriver

# 1、打开浏览器（建立一个浏览器驱动），每个浏览器有不同驱动，驱动都是浏览器厂商提供
# 这个驱动版本要跟你浏览器版本配套。（有方法可实现自动下载驱动）
# 2、进入被测试系统 ，输入网址打开网页
# 死等2秒
# 3、输入用户名密码，（定位id,name,xpath,css，8种 操作：sendkey输入，click点击）
# 4、点击登陆
# 5、断言登陆成功


driver = webdriver.Chrome(executable_path=
                          '/Users/lindafang/PycharmProjects/pytest_book/src/chapter9selenium/driver/chromedriver')
driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/auth/login")
time.sleep(2)

# driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_name("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("root1234")
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
assert '欢迎Admin' == driver.find_element_by_id("welcome").text
assert 'Admin' in driver.find_element_by_id("welcome").text
time.sleep(2)
driver.close()
