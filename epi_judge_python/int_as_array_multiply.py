from typing import List

from test_framework import generic_test

# [1,0] * [-2, 2] -> [-2, 2, 0]
# [-3,5,1] * [-7 , 8 , 9 ] -> [2,7,6, 9, 3, 9]
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
