# Author: lindafang
# Date: 2020-10-07 22:37
# File: log.py
import sys

from logbook import Logger, StreamHandler


class conf():
    @staticmethod
    def logcon():
        log = Logger('HRM系统测试自动化⽇志')
        StreamHandler(sys.stdout).push_application()
        # FileHandler("logs/pytest_log.log").push_application()
        return log
