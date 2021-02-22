import pytest


@pytest.mark.parametrize('input, expected', [(1, 2), (3, 4)],
                         ids=['first', 'second'])
def test_ids_with_ids1(input, expected):
    pass


@pytest.mark.parametrize('input, expected', [(1, 2), (3, 4)],
                         ids=['num', 'num'])
def test_ids_with_ids2(input, expected):
    pass


@pytest.mark.parametrize('input, expected', [
    pytest.param(1, 2, id='Windows'),
    pytest.param(3, 4, id='Windows'),
    pytest.param(5, 6, id='Non-Windows')
])
def test_ids_with_ids3(input, expected):
    pass


@pytest.mark.parametrize('input, expected', [(1, 2), (3, 4)],
                         ids=['num', '中文'])
def test_ids_with_ids4(input, expected):
    pass
