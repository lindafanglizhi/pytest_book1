# Author: lindafang
# Date: 2020-10-07 23:09
# File: read_yml.py
import yaml


def get_yaml_data(yaml_file):
    with open(yaml_file, 'r', encoding="utf-8")as file:
        file_data = file.read()

    data = yaml.load(file_data)
    return data
