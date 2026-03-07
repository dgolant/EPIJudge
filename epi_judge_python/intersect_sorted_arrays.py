from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    a, b = 0, 0
    res = {}
    while  b < len(B) and a < len(A):
      while a < len(A) and A[a] < B[b]:
         a+=1
      while b < len(B) and a < len(A) and B[b] < A[a]:
         b+=1
      
      while a < len(A) and b < len(B) and A[a] == B[b]:
        res[A[a]] = True
        a+=1
        b+=1
      
    return list(res.keys())
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
