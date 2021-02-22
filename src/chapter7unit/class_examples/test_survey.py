# Author: lindafang
# Date: 2020-10-05 09:11
# File: test_survey.py
from .survey import AnonymousSurvey


class TestAnonymousSurvey(object):
    """针对AnonymousSurvey类的测试"""

    def test_single_response(self):
        """测试单个答案会被妥善的存储"""
        question = "你喜欢的女朋友有什么样的气质?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_respond('温柔')

        assert '温柔', my_survey.responses

    def test_store_three_response(self):
        """测试三个答案会被被妥善地存储"""
        question = "你喜欢的女朋友有什么样的气质?"
        my_survey = AnonymousSurvey(question)
        responses = ['温柔', '聪明', '美丽']
        for response in responses:
            my_survey.store_respond(response)
            # print(my_survey.responses)
            assert (response in my_survey.responses)
