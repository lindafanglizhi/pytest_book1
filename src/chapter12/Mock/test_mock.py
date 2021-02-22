# Author: lindafang
# Date: 2020-11-25 09:27
# File: test_mock.py
import mock


class MyClass(object):
    def __init__(self):
        print(f'建立 MyClass在{id(self)} 内存位置')


def create_instance():
    return MyClass()


@mock.patch('__main__.MyClass')
def create_instance2(MyClass):
    MyClass.return_value = 'foo'
    return create_instance()


print(create_instance2())

'''
patchMyClass以允许您控制所调用函数中类的用法的方式进行替换。修补类后，对该类的引用将完全由模拟实例替换。
mock.patch通常在测试要在测试内部创建类的新实例的东西时使用。 
mock.Mock实例更清晰，更可取。
如果您的self.sut.something方法创建了的实例MyClass而不是将实例作为参数接收，则mock.patch此处适当。
'''
