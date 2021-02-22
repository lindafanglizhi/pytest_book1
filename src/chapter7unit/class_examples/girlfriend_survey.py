# Author: lindafang
# Date: 2020-10-05 08:41
# File: girlfriend_survey.py

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "你喜欢的女朋友有什么样的气质?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("输入'退出'，可退出问卷. \n")
while True:
    response = input("气质: ")
    if response == '退出':
        break
    my_survey.store_respond(response)

# 显示调查结果
print("\n感谢每位进行问卷调查的人员!")
my_survey.show_result()
