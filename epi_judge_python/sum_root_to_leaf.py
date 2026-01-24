from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_children(tree: BinaryTreeNode, sums: list, running_total: int):
    if not tree:
        return
    running_total*=10
    running_total+=tree.data
    if tree.right or tree.left:
        for child in [tree.right, tree.left]:
                sum_children(child, sums, running_total)
    else:
        sums.append(running_total)
    running_total//=10
    return



def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    sums = []
    sum_children(tree, sums, 0)
    total = 0
    for num in sums:
         total += int(str(num), 2)
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
