from test_framework import generic_test


def next_number(s: str) -> str:
  result, i = [], 0
  while i < len(s):
    count = 1
    #  from each char, move forward while it is the same as the next
    while i+1 < len(s) and s[i] == s[i+1]:
       i+=1
       count+=1
    # when we hit a break (chars don't match), append the count and the char we just tracked to result
    result.append(str(count) + s[i])
    # move to the next char (first to not match)
    i+=1
  
  return ''.join(result)

def look_and_say(n: int) -> str:
    s = '1'
    for _ in range(1,n):
       s = next_number(s)
    return s
       


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
