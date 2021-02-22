import pytest


@pytest.fixture(scope='module')
def test_input(request):
    pass


@pytest.fixture(scope='module')
def expected(request):
    pass


@pytest.mark.parametrize('test_input, expected', [(1, 2), (3, 4)],
                         indirect=True)
def test_scope1(test_input, expected):
    pass


@pytest.mark.parametrize('test_input, expected', [(1, 2), (3, 4)],
                         indirect=True)
def test_scope2(test_input, expected):
    pass
