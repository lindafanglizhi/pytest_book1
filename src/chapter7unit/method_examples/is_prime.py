# Author: lindafang
# Date: 2020-09-03 14:20
# File: is_prime.py


def is_prime(number):
    """如果是质数，返回为True"""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def print_next_prime(number):
    """打印输入number数字最近的质数"""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
