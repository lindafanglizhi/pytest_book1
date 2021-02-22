# Author: lindafang
# Date: 2020-08-14 11:28
# File: test_data_drvien.py
import pytest

from utils.get_csvdata import get_csv_data
from utils.get_path import PATH

datafile = PATH("../Testdatas/addnotedata.csv")
data_test = get_csv_data(datafile)


@pytest.fixture(autouse=True)
def data_addnote(*data_test):
    # print("这是",data_test)
    print(type(data_test))
    return data_test


@pytest.mark.parametrize("title,text", data_addnote)
def test_param(title, text):
    print(title, "----")
    print(text, "---")


if __name__ == '__main__':
    pytest.main()
