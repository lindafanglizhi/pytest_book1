# Author: lindafang
# Date: 2020-10-21 10:14
# File: test_publish_article.py

from pytest_bdd import scenario, given, when, then


@scenario('../features/publish_article.feature', '发布文章')
def test_publish():
    pass


@given("我是一个作者")
def author_user():
    author = "linda"
    return author


@given("我有一篇文章", target_fixture="article")
def article():
    article_name = "测试BDD"
    return article_name


@when("转到文章页面时")
def go_to_article(article, author_user):
    print("作者：", author_user)
    print("文章标题：" + article, "文章内容：略过一万字")


@when("我按了发布按钮")
def publish_article():
    print("提交")


@then("我应该不会看到错误消息")
def no_error_message():
    print("没有错误信息")


@then("应该发布该文章")
def article_is_published(article):
    print("刷新网页")
    print("断言发布成功")
    assert article == "测试BDD"
