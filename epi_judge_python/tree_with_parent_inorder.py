from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test

def traverse(tree: BinaryTreeNode, res: List):
    if not tree:
        return



def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    curr = tree
    res = []
    stack = []

    while curr or curr.parent:
        # print(curr)
        # go as far left as possible
        while curr.left:
            curr = curr.left

        if curr:
            res.append(curr.data)
            curr = curr.right
        else:
            curr = curr.parent

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
