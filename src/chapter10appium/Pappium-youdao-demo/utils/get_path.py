# Author: lindafang
# Date: 2020-08-13 15:21
# File: get_path.py


import os


def PATH(file):
    # dirname是获得当前文件的相对目录.
    # join 把两个字符串组合在一起。
    # abspath获得绝对路径
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file))
