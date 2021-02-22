# Author: lindafang
# Date: 2020-05-13 12:54
# File: test_invoke_via_main.py

import time


def test_one():
    time.sleep(10)


if __name__ == '__main__':
    import pytest

    ret = pytest.main(['-q', __file__])
    print("pytest.main() 返回 pytest.ExitCode.INTERRUPTED：", ret == pytest.ExitCode.INTERRUPTED)
