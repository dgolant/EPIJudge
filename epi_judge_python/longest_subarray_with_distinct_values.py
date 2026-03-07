from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    
    max_len = 0
    last_position = {}
    l, r = 0,0
    while r < len(A):
        char = A[r]
        if char not in last_position:
            last_position[char] = r
            max_len = max(max_len, (r-l)+1)
        else:
          l = max(last_position[char]+1, l)
          last_position[char]=r
          max_len = max(max_len, (r-l)+1)
        r+=1
    return max_len

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))

