# Author: lindafang
# Date: 2020-11-25 13:19
# File: app.py

import requests


def get_json(url):
    # 返回响应json格式
    r = requests.get(url)
    return r.json()


DEFAULT_CONFIG = {"user": "user1", "database": "db1"}


def create_connection_string(config=None):
    config = config or DEFAULT_CONFIG
    return f"User Id={config['user']}; Location={config['database']};"
