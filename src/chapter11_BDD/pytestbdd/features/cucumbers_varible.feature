Feature: 黄瓜篮子
  As 我是菜农
  I 想要摘黄瓜到篮子中
  So 我不会把它们都扔了.


  Scenario: 摘黄瓜到篮子
    Given 篮子原来有 "2" 个黄瓜
    When 添加 "4" 个黄瓜到篮子中
    Then 篮子剩余 "6" 个黄瓜

  Scenario: 从篮子中删除黄瓜
    Given 篮子原来有 "8" 个黄瓜
    When 从篮子中拿出 "3" 个黄瓜
    Then 篮子剩余 "5" 个黄瓜