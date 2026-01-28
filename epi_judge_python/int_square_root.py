from test_framework import generic_test


def square_root(k: int) -> int:
    l = 0
    h = k-1
    cand = -1
    while l <= h:

    return cand


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
