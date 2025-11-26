import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


# [0, 0, 0, 1, 2, 2]
# piv_index = 2, piv val = 1
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
  # two passes
  # first pass: everything smaller than piv goes to first half
  # second pass: everything larger than piv goes to second
  # 
  lpi = 0
  piv = A[pivot_index]
  for i in range(len(A)):
    if A[i] < piv:
        A[lpi], A[i] = A[i], A[lpi]
        lpi+=1
  
  gpi = len(A)-1
  # start from the end
  for i in reversed(range(len(A))):
      if A[i] > piv:
          A[gpi], A[i] = A[i], A[gpi]
          gpi-=1
  return
  





@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]
    
    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
