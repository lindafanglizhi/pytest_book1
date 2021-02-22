# Author: lindafang
# Date: 2020-05-13 21:03
# File: max.py

def max(values):
    _max = values[0]

    for val in values:
        if val > _max:
            _max = val

    return _max
