# Author: lindafang
# Date: 2020-11-25 13:06
# File: test_module.py
from pathlib import Path


def getssh():
    # 返回home/.ssh路径
    return Path.home() / ".ssh"


def test_getssh(monkeypatch):
    # 模拟返回路径
    def mockreturn():
        return Path("/abc")

    # monkeypatch设置path属性
    monkeypatch.setattr(Path, "home", mockreturn)

    x = getssh()
    assert x == Path("/abc/.ssh")
