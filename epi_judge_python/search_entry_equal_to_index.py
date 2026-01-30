import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def search_entry_equal_to_its_index(A: List[int]) -> int:
    l, r = 0, len(A)-1
    mp = -1
    while l <= r:
        mp = (l + r)//2
        print(f"--------------------------:{mp}")
        print(f"L:{l}, R: {r}")
        if A[mp] > mp:
            # move left, all values to right will inherently be greater than their index
            r = mp-1
        elif A[mp] < mp:
            # move right, inverse
            l = mp+1
        else:
            return mp

    return -1


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
