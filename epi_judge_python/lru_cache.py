from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class LruCache:
    def __init__(self, capacity: int) -> None:
        # TODO - you fill in here.
        self.capacity = capacity
        self.data = {}
        self.lru = deque()
        return

    def lookup(self, isbn: int) -> int:
        if isbn not in self.data:
            return -1
        val, pos = self.data[isbn]
        self.lru.
        return val

    def insert(self, isbn: int, price: int) -> None:
        self.lru.append(isbn)
        if len(self.lru) > self.capacity:
            self.lru.popleft()
        self.data[isbn] = (price, self.lru.length-1)
        return

    def erase(self, isbn: int) -> bool:
        # TODO - you fill in here.
        return True


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
