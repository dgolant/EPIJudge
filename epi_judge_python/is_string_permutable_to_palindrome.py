from test_framework import generic_test
import collections

def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    counts = collections.Counter(s)
    odds_exist = False
    print(f"counts: {counts}")
    for char in counts.keys():
        count = counts[char]
        if char == " ":
            continue
        if count % 2 == 1:
            if odds_exist:
                print(f"char:{char}, count:{count}")
                return False
            else:
                print(f"char:{char}, count:{count}")
                odds_exist = True
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
