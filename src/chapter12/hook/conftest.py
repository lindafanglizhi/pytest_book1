# Author: lindafang
# Date: 2020-11-25 15:08
# File: conftest.py
import time


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print('------------------------------------')
#
#     # 获取钩子方法的调用结果
#     out = yield
#     print('用例执行结果', out)
#
#     # 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#
#     print('测试报告:%s' % report)
#     print('步骤:%s' % report.when)
#     print('nodeid:%s' % report.nodeid)
#     print('description:%s' % str(item.function.__doc__))
#     print(('运行结果: %s' % report.outcome))
#
# @pytest.fixture(scope="session", autouse=True)
# def fix_a():
#     print("\nsetup 前置操作")
#     yield
#     print("\nteardown 后置操作")

#
# def pytest_collection_modifyitems(session, items):
#     print("收集到的测试用例:%s"%items)

# def pytest_collection_modifyitems(session, items):
#     print(type(items))
#     print("收集到的测试用例:%s" % items)
#     # sort排序，根据用例名称item.name 排序
#     items.sort(key=lambda x: x.name)
#     print("排序后的用例:%s" % items)
#     for item in items:
#         print("用例名:%s" % item.name)

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    print(terminalreporter.stats)
    print("total:", terminalreporter._numcollected)
    print('passed:', len(terminalreporter.stats.get('passed', [])))
    print('failed:', len(terminalreporter.stats.get('failed', [])))
    print('error:', len(terminalreporter.stats.get('error', [])))
    print('skipped:', len(terminalreporter.stats.get('skipped', [])))
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times:', duration, 'seconds')
