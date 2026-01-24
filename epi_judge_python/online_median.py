from typing import Iterator, List
import heapq

from test_framework import generic_test
import bisect

def online_median(sequence: Iterator[int]) -> List[float]:
    # stores the lower numbers
    max_heap = []
    # stores the higher numbers
    min_heap = []
    # stores results
    medians = []

    for val in sequence:
        # by default, pop one from min heap every time we push a new one on
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, val))

        # arrays must be at MOST even in length, otherwise min_heap should be larger to simplify averaging
        # this is smart: rather than saying "check which one is longer, return its 0th element," instead just make sure one is longer, you're in control anyway.
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        medians.append((0.5 * (min_heap[0] + -max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])
    return medians
bisect.bisect_left()

def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
