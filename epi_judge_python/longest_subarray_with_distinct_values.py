from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    l, r = 0, 0
    max_len = 0
    positions = {}
    while r < len(A):
        char = A[r]

        if char in positions and positions[char] >= l:
            l = positions[char]+1

        positions[char] = r


        max_len = max(max_len, (r - l)+1)
        r+=1
    return max_len




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
