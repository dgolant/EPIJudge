import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def get_ancestry(stack: list, root: BinaryTreeNode, target: BinaryTreeNode) -> bool:
    if not root:
        return False

    stack.append(root)

    if root is target:
        return True
    if get_ancestry(stack, root.left, target):
        return True
    if get_ancestry(stack, root.right, target):
        return True

    stack.pop()
    return False

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not tree:
        return tree
    ancestry0 = []
    get_ancestry(ancestry0, tree, node0)
    ancestry1 = []
    get_ancestry(ancestry1, tree, node1)

    i = min(len(ancestry0), len(ancestry1)) - 1
    while i > 0:
        if ancestry0[i] == ancestry1[i]:
            return ancestry0[i]
        i-=1

    return tree


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
