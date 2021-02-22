# Author: lindafang
# Date: 2020-04-30 15:34
# File: test_assert_2.py
import pytest


def test_long_str_comparison():
    str3 = 'abcdef'
    str4 = 'adcdef'
    assert str3 == str4


def test_eq_list():
    assert [0, 1, 2] == [0, 1, 3]


def test_dict_comparison():
    dict1 = {
        'name': 'linda',
        'age': 18,
    }
    dict2 = {
        'name': 'linda',
        'age': 88,
    }
    assert dict1 == dict2


def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    print("比较")
    assert set1 == set2


if __name__ == '__main__':
    pytest.main(["-x", "test_assert_2.py"])
