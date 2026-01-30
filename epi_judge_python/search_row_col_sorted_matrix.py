from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    # TODO - you fill in here.
    v, h = 0, len(A[0])-1

    while v < len(A) and h >= 0:
        if x > A[v][h]:
            v+=1
        elif x < A[v][h]:
            h-=1
        else:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
