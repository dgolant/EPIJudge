from typing import List

from test_framework import generic_test
import heapq

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    print(f"lenA:{len(A)}, A:{sorted(A)}, res: {A[len(A)-k]}")
    negk = len(A)-k
    max_heap = []
    i = 0
    while len(max_heap) < negk:
        heapq.heappush(max_heap, -A[i])
        i+=1
    return -heapq.heappop(max_heap)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
