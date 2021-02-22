import pytest


# scope=function


def f():
    return 3


@pytest.mark.skip
def test_cakan():
    pass
    assert f() == 4


@pytest.mark.skip(reason="当前没有办法执行这个")
def test_the_unknown():
    ...


def valid_config():
    #    返回1表示有效的配置，返回0表示无效
    # 这里可以是从配置文件中读取的数值，与系统返回的值比对。
    # 比如读回是32位系统，但配置是64位的配置，比较后所以返回0
    # 这个可能测试不同配置在不同环境下是否配置成功
    return 0


def test_function():
    if not valid_config():
        pytest.skip("不支持此项配置")
