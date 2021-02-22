@interface_api @lindafang
Feature: lindafang测试必应搜索
  As 一个测试人员,
  I 想要通过REST API的调用进行测试
  So 能获得正确的返回


  Scenario Outline: 测试必应搜索
    Given 查询关键字 "<phrase>"
    Then 响应状态码是 "200"
    And 结果包含 "<phrase>"

    Examples: 关键字
      | phrase   |
      | python   |
      | java     |
      | selenium |
