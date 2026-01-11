from test_framework import generic_test


# XXXX -> 40
def roman_to_integer(s: str) -> int:
    # first, we solve without exceptions
    T = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # iterate over, and as long as digits do not increase, add them up. If they increase, its an exception. 

    if len(s) < 1: 
        return 0
    sum = T[s[-1]]
    for i in reversed(range(len(s)-1)):
        if T[s[i]] < T[s[i+1]]:
            sum-=T[s[i]]
        else:
            sum+=T[s[i]]

    return sum


# def roman_to_integer(s: str) -> int:
#     T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

#     total = T[s[-1]]
#     for i in reversed(range(len(s) - 1)):
#         if T[s[i]] < T[s[i + 1]]:
#             total -= T[s[i]]
#         else:
#             total += T[s[i]]

#     return total

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
