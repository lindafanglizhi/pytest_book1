# Author: lindafang
# Date: 2020-10-05 09:11
# File: test_survey.py
import pytest

from .survey import AnonymousSurvey


class TestAnonymousSurvey(object):
    """针对AnonymousSurvey类的测试"""
    """使用fixture自动应用的方式加载初始化数据和对象"""

    @pytest.fixture(autouse=True)
    def setUp_object_data(self):
        """
        创建一个调查对象和一组答案，共使用的测试方法使用
        """
        question = "你喜欢的女朋友有什么样的气质?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['温柔', '聪明', '美丽']

    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        self.my_survey.store_respond(self.responses[0])
        assert self.responses[0] in self.my_survey.responses

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_respond(response)
        for response in self.responses:
            assert response in self.my_survey.responses
