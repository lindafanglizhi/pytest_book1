import pytest


@pytest.mark.parametrize('test_input', [1, 2, 3])
@pytest.mark.parametrize('test_output, expected', [(1, 2), (3, 4)])
def test_multi(test_input, test_output, expected):
    pass
