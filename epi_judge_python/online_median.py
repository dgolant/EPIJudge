from typing import Iterator, List

from test_framework import generic_test




def online_median(sequence: Iterator[int]) -> List[float]:
    one_half = [next(sequence)]
    two_half = [next(sequence)]
    res = [one_half[0], (one_half[0]+two_half[0])/2]

    for num in sequence:



def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
