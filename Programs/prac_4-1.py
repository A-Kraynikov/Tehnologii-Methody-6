from abc import ABC, abstractmethod
from typing import List


class cookieItem:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"печенье под номером: {self.number}"

class Iterator(ABC):
    @abstractmethod
    def next(self) -> cookieItem:
        ...

    @abstractmethod
    def has_next(self) -> bool:
        ...

class cookienumIterator(Iterator):
    def __init__(self, cookie: List[cookieItem]):
        self._cookie = cookie
        self._index = 0

    def next(self) -> cookieItem:
        cookie_item = self._cookie[self._index]
        self._index += 1
        return cookie_item

    def has_next(self) -> bool:
        return False if self._index >= len(self._cookie) else True

class cookieAggregate:
    def __init__(self, amount_num: int = 10):
        self.num = [cookieItem(it+1) for it in range(amount_num)]
        print(f"Взяли банку печенья "
              f"на {amount_num} печенек")

    def amount_num(self) -> int:
        return len(self.num)

    def iterator(self) -> Iterator:
        return cookienumIterator(self.num)


if __name__ == "__main__":
    cookie = cookieAggregate(5)
    iterator = cookie.iterator()
    while iterator.has_next():
        item = iterator.next()
        print("Это " + str(item))