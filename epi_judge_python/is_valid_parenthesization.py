from test_framework import generic_test


matches = {
  "]": "[",
  "}": "{",
  ")": "("
}

def is_well_formed(s: str) -> bool:
    stack = []
    for char in s:
        if char in ["{", "[", "("]:
            stack.append(char)
        else:
            if not stack:
                return False
            last = stack.pop()
            if char in matches and matches[char] == last:
                pass
            else:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
