# Author: lindafang
# Date: 2020-10-07 22:41
# File: get_path.py

import os


def get_par_path():
    root_path = os.path.abspath(os.path.dirname(__file__)).split('Utils')[0]
    # 返回的就是根路径
    return root_path
