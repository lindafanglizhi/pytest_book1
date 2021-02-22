# -*- coding: utf-8 -*-

import operator

import pytest

from .foobar import Package, Woman, Man

PACKAGES = [
    Package('requests-api', 'Apache 2.0'),
    Package('django-web', 'BSD'),
    Package('pytest-automationtest', 'MIT'),
]


@pytest.fixture(params=PACKAGES, ids=(operator.attrgetter('name')))
def python_package(request):
    return request.param


@pytest.mark.parametrize('person', [
    Woman('lindafang'), Woman('nanzhang'),
    Man('wenli'), Woman('mingzhao'), Man('dongjin')
], ids=())
def test_become_a_programmer(person, python_package):
    person.learn(python_package.name)
    print(person._skills)
    assert person.looks_like_a_programmer


def test_is_open_source(python_package):
    assert python_package.is_open_source


if __name__ == '__main__':
    pytest.main()
