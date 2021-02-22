from appium import webdriver

from utils import desired_caps

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps.get_desired_caps())
# 进入时点的同意
el1 = driver.find_element_by_id("btn_ok")
# com.youdao.note:id/btn_ok
el1.click()

# time.sleep(2)
# driver.find_element_by_id("com.youdao.note:id/btn_ok").click()
#
# time.sleep(2)
# # 权限允许
# el2=driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el2.click()
# if el2 is not None:
#     el2.click()
# time.sleep(3)
# el3 = driver.find_element_by_id("com.youdao.note:id/add_note")
# el3.click()
# time.sleep(2)
# el4 = driver.find_element_by_id("com.youdao.note:id/add_icon")
# el4.click()
# time.sleep(3)
# # driver.back()
# el5 = driver.find_element_by_id("com.youdao.note:id/note_title")
# el5.send_keys("这是我的日志")
# time.sleep(5)
#
# # driver.press_keycode(66)
# # time.sleep(1)
# driver.find_elements_by_xpath('//android.widget.LinearLayout[@resourceid="com.youdao.note:id/note_content"]')[1].send_keys('七点半签到')

# time.sleep(3)
#
# el9 = driver.find_element_by_id("com.youdao.note:id/actionbar_complete_text")
# el9.click()
#
# driver.reset()
