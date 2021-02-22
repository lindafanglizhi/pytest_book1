# 比较
def test_lessmore():
    assert 1 <= 3
    assert 5 >= 1.3
    age = 28
    assert 20 < age < 80


# 真假
def test_true():
    assert (1 < 3) is True
    assert (5 > 3) is False


# 断言包含,当有'时用"号
def test_in_dict():
    x = 'linda1'
    assert x in "I'm linda"


# 断言不等，不在
def test_not_eq():
    assert 1 != 2
    assert ['linda'] not in ['linda', 'tom', 'seven']


# 断言长的列表中有哪些不同
def test_long_list():
    x = [str(i) for i in range(100)]
    y = [str(i) for i in range(0, 100, 2)]
    assert x == y


def test_long_copy():
    # 50个12，与50个11比对，pytest会更好的提示它们本质的区别
    assert [12] * 50 == [11] * 50
