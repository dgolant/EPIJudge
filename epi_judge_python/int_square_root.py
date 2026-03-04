from test_framework import generic_test


def square_root(k: int) -> int:
    l = 0
    h = k
    res = -1
    while l <= h:
        med = l+int((h-l)/2)
        if med**2 > k:
            h=med-1
        else:
            res = med
            l = med+1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
