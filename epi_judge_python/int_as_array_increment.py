from typing import List

from test_framework import generic_test

# [1] -> [2]
# [9] -> [1,0]
# [1,2,9] -> [1,3,0]
# [9,9,9] -> [1,0,0,0]
def plus_one(A: List[int]) -> List[int]:
    # start at last index
    # add 1
    # if new val != 0, return
    # if new val == 0, continue
    # if idx == 0 and new_val == 1, return [1]+[array]
    
    # but this only happens if every value is 9, so just check that first
    if A[0] == 9 and all(x == A[0] for x in A):
        A[:] = [0]*len(A)
        A.append(1)
        A.reverse()
        print(f"A is {A}")
        return A
    
    for i in reversed(range(len(A))):
        v = A[i]
        if v == 9:
            A[i] = 0
        else:
            A[i]+=1
            break
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
