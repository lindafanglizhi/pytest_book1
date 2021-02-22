#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def test_output(capsys):
    print('hello')
    print('world', file=sys.stderr, end='&')  # 标准错误输出，修改结束符
    captured = capsys.readouterr()
    assert captured.out == 'hello\n'  # print() 默认的结束符是换行符
    assert captured.err == 'world&'
    print('next')
    captured = capsys.readouterr()
    assert captured.out == 'next1\n'


def test_binary_output(capsysbinary):
    print('hello')
    captured = capsysbinary.readouterr()
    assert captured.out == b'hello1\n'


def test_disabling_capturing(capsys):
    print("hello")
    with capsys.disabled():
        print("world")
    captured = capsys.readouterr()
    assert captured.out == "hello2\n"
