from typing import List

from test_framework import generic_test
import bisect

def search_first_of_k(A: List[int], k: int) -> int:
    l = 0
    h = len(A)-1
    first_k = -1

    while l <= h:
        midpoint = l+((h-l)//2)
        if A[midpoint]==k:
            first_k = midpoint
            h=midpoint-1
        elif k > A[midpoint]:
            l = midpoint+1
        elif k < A[midpoint]:
            h = midpoint-1
    return first_k


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
