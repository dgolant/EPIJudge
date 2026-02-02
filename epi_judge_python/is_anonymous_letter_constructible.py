from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    magazine_counts = Counter(magazine_text)
    letter_counts = Counter(letter_text)
    letter_counts = letter_counts - magazine_counts
    print(f"letter_counts:{letter_counts}")
    if letter_counts.keys():
        return False
    return True




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
