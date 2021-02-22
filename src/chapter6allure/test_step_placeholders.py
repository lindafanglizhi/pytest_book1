# Author: lindafang
# Date: 2020-10-05 14:19
# File: test_step_placeholders.py
import allure


@allure.step('步骤可以有描述行, 位置参数显示输入参数: "{0}", 关键字显示输入参数: "{key}"')
def step_with_title_placeholders(arg1, key=None):
    pass


def test_steps_with_placeholders():
    step_with_title_placeholders(1, key='这是关键字参数')
    step_with_title_placeholders(2)
    step_with_title_placeholders(3, '这是位置参数')
