from typing import List

from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = []
    heapq.heapify(heap)
    for lst in sorted_arrays:
      [heapq.heappush(heap, child) for child in lst]
      
    # print(f"heap:{heap}")
    x = [heapq.heappop(heap) for _ in range(len(heap))]
    
    return x

    
         
            


       
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
