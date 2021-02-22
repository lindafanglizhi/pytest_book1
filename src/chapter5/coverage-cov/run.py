# Author: lindafang
# Date: 2020-07-14 10:24
# File: run.py

import pytest

if __name__ == '__main__':
    pytest.main(["--cov=/Users/lindafang/PycharmProjects/pytest_book/src/chapter5/coverage-cov", "--cov-report=html",
                 "--cov-config=/Users/lindafang/PycharmProjects/pytest_book/src/chapter5/coverage-cov/.coveragerc"])
