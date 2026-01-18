import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def leaf(tree: BinaryTreeNode) -> bool:
    return not tree.left and not tree.right

def add_leaves(tree: BinaryTreeNode, res: List[int]):
    if not tree:
        return None
    if not tree.left and not tree.right:
        res.append(tree)
    
    add_leaves(tree.left, res)
    add_leaves(tree.right, res)


def build_edge(tree: BinaryTreeNode, res: List[int], direction_left: bool):
    if not tree:
        return None
    
    if not leaf(tree):
      print(f"Not leaf {tree.data}")
      res.append(tree)

    if direction_left:
        next = tree.left if tree.left else tree.right
        build_edge(next, res, direction_left)
    else:
        next = tree.right if tree.right else tree.left
        build_edge(next, res, direction_left)

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    res = []
    if tree:
      build_edge(tree, res, True)
      add_leaves(tree, res)
      right_edge = []
      build_edge(tree, right_edge, False)
      right_edge.reverse()
      right_edge.pop()
      res.extend(right_edge)

    return res


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
