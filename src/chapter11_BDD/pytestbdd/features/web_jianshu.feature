@web @lindafang
Feature: lindafang 浏览自己分享的信息
  As 在互联网上
  I 发现一个自己分享的信息
  So 我看到自己在网站的文章


  Background:
    Given LindaFang简书页


  Scenario: 搜索LindaFang的文章
    When 搜索"接口测试"的文章
    Then 显示"接口测试"的文章


  Scenario: 搜索任何LindaFang的文章
    When 搜索任何一个"<phrase>"的文章
    Then 显示这个"<phrase>"所包含的文章

    Examples: 单词
      | phrase      |
      | test        |
      | interface   |
      | APP         |
