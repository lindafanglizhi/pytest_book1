# Author: lindafang
# Date: 2020-10-09 11:42
# File: run_p0.py
import pytest

if __name__ == '__main__':
    # p0测试可以将所有测试用例中正确的用例执行一遍,可以多个文件
    pytest.main(['-s', 'test_create_tag.py', '--allure-features', '正确的创建标签'])
    # 健壮性测试加上负面的测试用例和异常的用例。
    # pytest.main(['-s','test_create_tag.py','--allure-features','错误的创建标签'])
