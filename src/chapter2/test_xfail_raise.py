import pytest


# @pytest.mark.xfail(raises=Exception)
@pytest.mark.xfail(raises=IndexError)
def test_xfail():
    print(broken_fixture())
    print("如果没有异常或异常引起的不同才执行这个")


def broken_fixture():
    raise Exception("Sorry, it's 中断异常.")

# # 如果python3.6以上才标记该测试用例，如果用例返回失败刚显示xfail，如果用例返回正确显示xpass
# @pytest.mark.xfail(sys.version_info >= (3, 6), reason="python3.6 api变更了",run=False)
# def test_function():
#     print("不同版本下执行不同测试用例")
#     assert 2==1
