# Author: lindafang
# Date: 2020-11-25 10:12
# File: client.py
import requests


# 该函数不属于测试范畴
# 是需要被模拟的 Python 对象
def send_request(url):
    r = requests.get(url)
    return r.status_code


# 待测试的单元
# 功能是访问 URL
# 存在两种结果：
#   访问成功：200
#   访问失败：404
def visit_baidu():
    return send_request('http://www.baidu.com')
