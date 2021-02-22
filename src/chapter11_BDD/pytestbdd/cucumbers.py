# Author: lindafang
# Date: 2020-10-14 13:30
# File: cucumbers.py


class CucumberBasket:

    def __init__(self, initial_count=0, max_count=10):
        if int(initial_count) < 0:
            raise ValueError("未放物品，空篮子，不能是负值")
        if max_count < 0:
            raise ValueError(f"最大放{max_count}个 ，不能是负值")

        self._count = initial_count
        self._max_count = max_count

    @property
    def count(self):
        return self._count

    @property
    def full(self):
        return self.count == self.max_count

    @property
    def empty(self):
        return self.count == 0

    @property
    def max_count(self):
        return self._max_count

    def add(self, count=1):
        new_count = self.count + count
        if new_count > self.max_count:
            raise ValueError("超过篮子的最大值")
        self._count = new_count

    def remove(self, count=1):
        new_count = self.count - count
        if new_count < 0:
            raise ValueError("没有那么多的黄瓜")
        self._count = new_count
