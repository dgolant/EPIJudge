from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    positions = {}
    min_dist = float("inf")
    for i in range(len(paragraph)):
        word = paragraph[i]
        if word not in positions:
            positions[word] = i
        else:
            distance = i - positions[word]
            min_dist = min(min_dist, distance)
            positions[word] = i
    if min_dist == float("inf"):
        return -1
    return min_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
