# Author: lindafang
# Date: 2020-08-13 11:56
# File: get_csvdata.py

import csv


def get_csv_data(file_name):
    rows = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows
