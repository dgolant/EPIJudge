from typing import List

from test_framework import generic_test

# 5x5 
# 1,2,3,4,5
# 6,7,8,9,0
# 1,2,3,4,5 center element is at floor(n/2),floor(n/2) in odd arrangement
# 6,7,8,9,0
# 1,2,3,4,5

# get next direction to go when we reach the edge
def next_steps(dir: List[int]) -> tuple[List[int], int]:
    if dir == [0,1]:
      return [1,0], 0
    if dir == [1,0]:
      return [0,-1], 0
    if dir == [0, -1]:
      return [-1,0], 0
    if dir == [-1,0]:
      #  Once we do a full turn, we count the number of completed turns
       return [0,1], 1

def proceed(matrix: List[List[int]], pos: List[int], res: List[int], dir: List[int], steps: int):
  for i in range(steps):
    res.append(matrix[pos[0]][pos[1]])
    pos[0]+=dir[0]
    pos[1]+=dir[1]



def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # traverse clockwise
    # move in direction for n-1-i
    # when no further movement in a direction is possible, change direction of traversal and increment i
    # when n-1-i == 0, return (if array is odd, append center index after terminating)
    n = len(square_matrix)
    pos = [0,0]
    res = []
    direction = [0,1]
    steps = n-1

    if n==1:
      return square_matrix[0]

    while steps > 0:
      proceed(square_matrix, pos, res, direction, steps)
      print(f"res is {res}, pos is {pos}\n")
      if direction == [-1,0]:
        # if we just finished the upward pass, we move to the right because we are starting a new loop
        pos[0]+=1
        pos[1]+=1
      direction, decr = next_steps(direction)
      steps-=decr
      if n%2 != 0 and len(res) == (n**2)-1:
        break
    
    if n%2 != 0:
      # add the center element if odd
      res.append(square_matrix[n//2][n//2])
    return res
    
# [[1, 4, 7], 
#  [9, 8, 2], 
#  [3, 5, 6]]
#
#

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
