# Author: lindafang
# Date: 2020-10-05 15:27
# File: test_describe_html.py

import allure


@allure.description_html("""
<h1>测试带有一些复杂的描述</h1>
<table style="width:100%">
  <tr>
    <th>名</th>
    <th>姓</th>
    <th>年龄</th>
  </tr>
  <tr align="center">
    <td>小明</td>
    <td>李</td>
    <td>50</td>
  </tr>
  <tr align="center">
    <td>小三</td>
    <td>唐</td>
    <td>94</td>
  </tr>
</table>
""")
def test_html_description():
    print("测试通过网页描述")
    assert True


@allure.description("""
这是一个多功能描述，计算
""")
def test_description_from_decorator():
    assert 42 == int(6 * 7)


def test_unicode_in_docstring_description():
    """Unicode 描述使用不同国家语言.

    Этот тест проверяет юникод.
    こんにちは、友達。

    你好伙计。
    """
    assert 42 == int(6 * 7)


@allure.description("""
这段描述将在测试结束后被替换
""")
def test_dynamic_description():
    assert 42 == int(6 * 7)
    allure.dynamic.description('这是最后的描述，替换前的描述！')
