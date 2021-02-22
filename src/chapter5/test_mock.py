# Author: lindafang
# Date: 2020-11-26 08:58
# File: test_mock.py

import os

import mock


class UnixFS:

    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')


def test_foo(mocker):
    # all valid calls
    mocker.patch('os.remove')
    mocker.patch.object(os, 'listdir', autospec=True)
    mocked_isfile = mocker.patch('os.path.isfile')


def test_spy(mocker):
    class Foo(object):
        def bar(self, v):
            return v * 2

    foo = Foo()
    spy = mocker.spy(foo, 'bar')
    assert foo.bar(21) == 42

    spy.assert_called_once_with(21)
    assert spy.spy_return == 42


def test_stub(mocker):
    def foo(on_something):
        on_something('foo', 'bar')

    stub = mocker.stub(name='on_something_stub')

    foo(stub)
    stub.assert_called_once_with('foo', 'bar')


def test_unix_fs1():
    with mock.patch('os.remove'):
        UnixFS.rm('file')
        os.remove.assert_called_once_with('file')
        expected = ''
        with mock.patch('os.listdir'):
            assert UnixFS.ls('dir') == expected

    with mock.patch('shutil.copy'):
        UnixFS.cp('src', 'dst')


import contextlib


def test_unix_fs2():
    with contextlib.ExitStack() as stack:
        stack.enter_context(mock.patch('os.remove'))
        UnixFS.rm('file')
        os.remove.assert_called_once_with('file')

        stack.enter_context(mock.patch('os.listdir'))
        assert UnixFS.ls('dir') == expected
        # ...

        stack.enter_context(mock.patch('shutil.copy'))
        UnixFS.cp('src', 'dst')
