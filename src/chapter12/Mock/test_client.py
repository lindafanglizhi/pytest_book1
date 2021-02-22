# Author: lindafang
# Date: 2020-11-25 10:13
# File: test_client.py
# filename: test_client.py

import mock

# sys.path.append('/Users/lindafang/PycharmProjects/pytest_book/src/chapter12/Mock')
import client


class TestClient():

    def test_success_request(self):
        # 测试访问生成的情况：
        #   实例化一个 Mock 对象，用于替换 client.send_request 函数
        #   这个 Mock 对象会返回 HTTP Code 200
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        assert client.visit_baidu() == '200'

    def test_fail_request(self):
        # 测试访问失败的情况：
        #   实例化一个 Mock 对象，用于替换 client.send_request 函数
        #   这个 Mock 对象会返回 HTTP Code 404
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        assert client.visit_baidu() == '404'
