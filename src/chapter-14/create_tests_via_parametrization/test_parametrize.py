# -*- coding: utf-8 -*-

import pytest

# 这是一个英国游戏，逢3就fizz,逢5就buzz，如果是3，5的倍数，则fizzbuzz
# 类似中国的逢3或3的倍数就敲一下桌子，其他就说出来1，2，敲，4，5，敲，7，8，敲，10，11，敲，敲，14
RULES = (
    (3 * 5, "FizzBuzz"),
    (3, "Fizz"),
    (5, "Buzz"),
)


def fizzbuzz(number):
    for div_number, substitution in RULES:
        if not number % div_number:
            return substitution
    return str(number)


@pytest.mark.parametrize(
    'number, word', [
        (1, '1'),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (16, '16')
    ]
)
def test_fizzbuzz(number, word):
    assert fizzbuzz(number) == word
