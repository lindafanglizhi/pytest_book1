# Author: lindafang
# Date: 2020-10-05 16:46
# File: test_feature_story_epic.py


import allure


def test_without_any_annotations_that_wont_be_executed():
    pass


@allure.epic('epic_1')
def test_with_epic_1():
    pass


@allure.feature('feature_1')
def test_with_feature_1():
    pass


@allure.story('story_1')
def test_with_story_1():
    pass


@allure.feature('feature_2')
@allure.story('story_1')
def test_with_story_1_and_feature_2():
    pass


@allure.feature('feature_2')
@allure.story('story_2')
def test_with_story_2_and_feature_2():
    pass
