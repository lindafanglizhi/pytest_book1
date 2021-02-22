# -*- coding: utf-8 -*-

FOSS_LICENSES = ['Apache 2.0', 'MIT', 'GPL', 'BSD']

PYTHON_PKGS = ['pytest-automationtest', 'requests-api', 'django-web', 'cookiecutter-项目模板']


class Package:
    def __init__(self, name, license):
        self.name = name
        self.license = license

    @property
    def is_open_source(self):
        return self.license in FOSS_LICENSES


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self._skills = ['eating', 'sleeping']

    def learn(self, skill):
        self._skills.append(skill)

    @property
    def looks_like_a_programmer(self):
        return any(
            package in self._skills
            for package in PYTHON_PKGS
        )


class Woman(Person):
    def __init__(self, name):
        super().__init__(name, '女')


class Man(Person):
    def __init__(self, name):
        super().__init__(name, '男')
