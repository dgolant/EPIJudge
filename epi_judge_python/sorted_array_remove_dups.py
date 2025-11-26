import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# <2,3,5,7,11,13,11,11,13>
# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    # naive solution: delete the value, shift left. However, this resizes the array alot, which is... n^2?
    # robust solution: swap dupes to end of array... still resizes
    # what if instead, we just count uniques, and then write them back in, and then drop the end of the array, since nothing matters after the last valid index?

    if not A:
        return 0
    
    # Write head is always > 0 since 0 cannot be repeated
    write_head = 1
    for i in range(1,len(A)): 
        # First NON-dupe char we see
        if A[write_head-1] != A[i]:
            # write it into the write head
            A[write_head] = A[i]
            write_head+=1
  
    return write_head
    
        


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
