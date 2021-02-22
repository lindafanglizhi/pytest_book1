# Author: lindafang
# Date: 2020-05-14 14:27
# File: test_xfail.py
import pytest


def valid_config():
    # 返回True是有效配置，返回False是无效配置
    return False


class Test_Pytest():

    @pytest.mark.xfail(reason='该功能有BUG')
    def test_one(self):
        print("----start------")
        # pytest.xfail(reason='该功能尚未完成')
        print("test_one方法执行")
        # assert 2 == 1
        assert 1 == 1

    def test_two(self):
        print("test_two方法执行")
        assert "o" in "love"

    def test_three(self):
        print("test_three方法执行")
        assert 3 - 2 == 1

    # def test_function(self):
    #     if not valid_config():
    #         pytest.xfail("这是个无效的配置，无法进行后续测试")
    #


# r参数是总结报告，s是输出控制台打印信息
if __name__ == "__main__":
    pytest.main(['-sr', 'test_xfail.py'])
