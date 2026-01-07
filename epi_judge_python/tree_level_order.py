from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    # take an array (res) and two queues (turns 0 and 1)
    # start with tree node 0 in turn 0 queue
    # in each turn, sequentially pop off a node, and put its CHILDREN into the OTHER TURN
    # push this node into res[curr_level]
    # when you run out of nodes in the current turns' queue, add a new array to res, increment turn, and proceed
    # terminate when both turns are empty
    if not tree:
        return []
    res = [[]]
    turns = [deque(), deque()]
    turns[0].append(tree)
    turn = 0
    while len(turns[0]) or len(turns[1]):
        while len(turns[turn]):
            curr = turns[turn].popleft()
            res[-1].append(curr.data)
            if curr.left:
                # Add this to the NEXT "level/turn"
                turns[turn-1].append(curr.left)
            if curr.right:
                turns[turn-1].append(curr.right)
        res.append([])
        turn = 1 if turn == 0 else 0

    res.pop()
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
