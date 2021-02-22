import allure

from .steps import imported_step


@allure.step
def passing_step():
    print("通过的步骤")
    pass


@allure.step
def step_with_nested_steps():
    print("带有嵌套的步骤nested")
    nested_step()


@allure.step
def nested_step():
    print("调用带有参数arg的步骤")
    nested_step_with_arguments(1, 'abc')


@allure.step
def nested_step_with_arguments(arg1, arg2):
    print("带有二个参数：", arg1, arg2)
    pass


def test_with_imported_step():
    passing_step()
    print("外部导入")
    imported_step()


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
