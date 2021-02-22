# Author: lindafang
# Date: 2020-10-06 10:17
# File: test_severity.py
import allure

'''
    BLOCKER = 'blocker'   
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'
    TRIVIAL = 'trivial'
    
Bug的严重程度（Severity）
1.Blocker:
 即系统无法执行、崩溃或严重资源不足、应用模块无法启动或异常退出、无法测试、造成系统不稳定。
严重花屏
内存泄漏
用户数据丢失或破坏
系统崩溃/死机/冻结
模块无法启动或异常退出
严重的数值计算错误
功能设计与需求严重不符
其它导致无法测试的错误, 如服务器500错误
2.Critical：
即影响系统功能或操作，主要功能存在严重缺陷，但不会影响到系统稳定性。

功能未实现
功能错误
系统刷新错误
数据通讯错误
轻微的数值计算错误
影响功能及界面的错误字或拼写错误
安全性问题
3. Major：
即界面、性能缺陷、兼容性。

操作界面错误（包括数据窗口内列名定义、含义是否一致）
边界条件下错误
提示信息错误（包括未给出信息、信息提示错误等）
长时间操作无进度提示
系统未优化（性能问题）
光标跳转设置不好，鼠标（光标）定位错误
兼容性问题
4.Minor/Trivial:
即易用性及建议性问题。

界面格式等不规范
辅助说明描述不清楚
操作时未给用户提示
可输入区域和只读区域没有明显的区分标志
个别不影响产品理解的错别字
文字排列不整齐等一些小问题
'''


def test_with_no_severity_label():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity(object):

    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass
