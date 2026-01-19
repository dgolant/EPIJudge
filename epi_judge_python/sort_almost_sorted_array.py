from typing import Iterator, List

from test_framework import generic_test
import heapq

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    
    heap = []
    res = []
    # Prefill the heap with k instances, since that's the max range we'll ever have to sort
    for i in range(k):
        num = next(sequence)
        heapq.heappush(heap, num)

    # then, keep pushing, and evict the smallest number each time. push each evicted number into the result
    for num in sequence:
        res.append(heapq.heappushpop(heap, num))
    # we may have to pop k times at the end too
    while heap:
        res.append(heapq.heappop(heap))
    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
