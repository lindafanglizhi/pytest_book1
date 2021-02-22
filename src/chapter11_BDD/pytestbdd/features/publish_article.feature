Feature: 博客
    一个可以在其中发布文章的网站。

    Scenario: 发布文章
        Given 我是一个作者
        And 我有一篇文章

        When 转到文章页面时
        And 我按了发布按钮

        Then 我应该不会看到错误消息
        And 应该发布该文章