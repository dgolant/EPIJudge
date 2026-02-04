from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    presence = {}
    min_val = float("inf")
    max_val = -float("inf")
    max_run = 0
    # Build a dictionary tracking which keys are present, and the minimum and maximum values
    for val in A:
        presence[val] = True
        min_val = min(min_val, val)
        max_val = max(max_val, val)

    run = 0
    for i in range(min_val, max_val+1):
        if i not in presence:
            run = 0
        else:
            run+=1
        max_run = max(max_run, run)
    return max_run


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
