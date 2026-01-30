from test_framework import generic_test
import math


def square_root(x: float) -> float:
    l, r = (0, x) if x >= 1.0 else (x, 1.0)
    mp = -1

    while not math.isclose(l, r):
        mp = (l + r)/2
        sq = mp**2
        if sq > x:
            r = mp
        else:
            l = mp
    return mp


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
