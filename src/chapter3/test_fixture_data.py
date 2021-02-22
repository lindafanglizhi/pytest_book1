# Author: lindafang
# Date: 2020-05-07 14:25
# File: test_fixture_data.py
import csv

import pytest


@pytest.fixture()
def data():
    test_data = {'name': 'linda', 'age': 18}
    return test_data


def test_login(data):
    name = data['name']
    age = data['age']
    print("我的名字叫：{}，今年{}。".format(name, age))


@pytest.fixture()
def read_data():
    with open('userinfo.csv') as f:
        row = csv.reader(f, delimiter=',')
        next(row)  # 读取首行
        users = []
        for r in row:
            users.append(r)  # 读取的字段均为str类型
    return users


def test_logins(read_data):
    name = read_data[0][0]
    age = read_data[0][1]
    print("我的名字叫：{}，今年{}。".format(name, age))
