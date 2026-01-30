from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    l, h = 0, len(A)-1
    mp = -1
    while l < h:
        mp = (l + h )//2
        if A[mp] > A[h]:
            l = mp+1
        else:
            h=mp
    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
