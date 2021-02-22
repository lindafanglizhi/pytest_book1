# Author: lindafang
# Date: 2020-05-15 12:57
# File: test_xml_report.py
import pytest


# def test_record_property(record_property):
#     record_property("test_id", 10010)
#     assert 1

# def test_record_property2(record_xml_attribute):
#     record_xml_attribute('test_id', 10010)
#     record_xml_attribute('classname', 'custom_classname')
#     assert 1

@pytest.fixture(scope="session")
def log_global_env_facts(record_testsuite_property):
    record_testsuite_property("EXECUTOR", "lindafang")
    record_testsuite_property("LOCATION", "HRB")


def test_record_property3(log_global_env_facts):
    assert 1
