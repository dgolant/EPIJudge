from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # But we never set the first list node's value.... weird (oh, it doesnt, we just return the next of the dummy_head)
    L3Head = L3 = ListNode()
    # Check if L1 and L2 are not None
    while L1 and L2:
        # print(f"L1: {L1.data}, L2: {L2.data}, L3: {L3Head}")
        # Check which is smaller L1 or L2
        # Set that as head of L3
        if L1.data <= L2.data:
            L3.next, L1 = L1, L1.next
        else:
            L3.next, L2 = L2, L2.next
    # appends the rest of any list that may remain.
    L3.next = L1 or L2
    return L3Head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
