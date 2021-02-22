# Author: lindafang
# Date: 2020-10-05 16:29
# File: test_issue_testcase_link.py
import allure

TEST_CASE_LINK = 'http://81.70.24.116:8088/zentao/bug-view-26.html'


@allure.link('http://81.70.24.116:8088/zentao/testcase-browse-1.html')
def test_with_link():
    pass


@allure.link('http://81.70.24.116:8088/zentao/product-index-no.html', name='点击进入项目')
def test_with_named_link():
    pass


@allure.issue('http://81.70.24.116:8088/zentao/bug-view-26.html', '测试出现问题的结果')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, '测试登陆健壮性')
def test_with_testcase_link():
    pass
