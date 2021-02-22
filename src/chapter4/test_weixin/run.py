# Author: lindafang
# Date: 2020-11-06 09:48
# File: run.py

import pytest

if __name__ == '__main__':
    pytest.main(['-s', 'test_weixin_create_tag.py'])
    pytest.main(['-s', 'test_weixin_get_update_delete_tag.py'])
    pytest.main(['-s', 'test_weixin_get_update_delete_tag.py::test_delete_tag'])
