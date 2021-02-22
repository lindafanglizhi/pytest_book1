Feature: 黄瓜篮子
  As 我是菜农
  I 想要摘黄瓜到篮子中
  So 我不会把它们都扔了.

  @add
  Scenario Outline: 摘黄瓜到篮子
    Given 篮子原来有 "<initial>" 个黄瓜
    When 添加 "<some>" 个黄瓜到篮子中
    Then 篮子剩余 "<total>" 个黄瓜


    Examples: Amounts
      | initial | some | total |
      | 2       | 4    | 6     |
      | 0       | 3    | 3     |
      | 5       | 5    | 10    |
      | 0       | -1   | 0    |

  @remove
  Scenario: 从篮子中删除黄瓜
    Given 篮子原来有 "8" 个黄瓜
    When 从篮子中拿出 "3" 个黄瓜
    Then 篮子剩余 "5" 个黄瓜
