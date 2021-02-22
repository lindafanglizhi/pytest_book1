# Author: lindafang
# Date: 2020-05-05 19:03
# File: conftest.py
# from .test_fail_cus import Foo
#
# def pytest_assertrepr_compare(op, left, right):
#     if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
#         return [
#             "比较两个Foo实例:",  # 顶头写概要
#             "   值: {} != {}".format(left.val, right.val),  # 除了第一个行，其余都可以缩进
#         ]

# 配置test_module下所有以test_开关的python文件，以及test_assert开关的python文件不参与收集
# 也就是不执行
# collect_ignore_glob = ['test_module/test_*.py','test_assert*.py']
