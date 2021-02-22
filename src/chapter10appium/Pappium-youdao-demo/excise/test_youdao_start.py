# Author: lindafang
# Date: 2020-08-12 09:20
# File: test_youdao_start.py
'''
1、连接手机（手机相关配置），启动手机app.
2、使用webdriver简单定位进行操作

'''
from utils.get_path import PATH

app_file = PATH("../Papp/ApiDemos-debug.apk")
print(app_file)
# desired_caps={
#     "platformName":"android",
#     # 在cmd使用adb devices返回的值写在下面
#     "deviceName":"emulator-5554",
#     # 这个是夜神的设备名
#     # "deviceName":"127.0.0.1:62001",
#     "platformVersion":"6.0",
#     # 你夜神的android版本
#     # "platformVersion":"5.1",
#     "automationName":"UiAutomator2",
#     # 值 是你app的地址
#     "app":app_file,
#
# }
#
#
#
# driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# el1 = driver.find_element_by_accessibility_id("Accessibility")
# el1.get_attribute("context-desc")
# el1.click()
# el2 = driver.find_element_by_accessibility_id("Accessibility Node Querying")
# el2.click()
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.CheckBox")
# el3.click()
# driver.save_screenshot("1.png")
