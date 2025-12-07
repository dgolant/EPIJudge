from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
# 16 -> 1,2,3,5,7,11,13
# primes must have exactly two distinct divisors: 1 and itself
# we know 2 is prime, but we also know that no multiple of 2 is prime
# the task is to find all primes between 0 and N
# so, we create an array of potential primes, and we assume all are prime (optimistic, greedy), other than ones we know are false (0,1)
# for a number, check if it is prime. If NOT, skip
# if it is, add it to the primes array, and then take every multiple of the number between num*2 and n, and set it to FALSE (we know it can't be prime since its divisble by number)
# then move on to the next number
# continue until n
# to further optimize, rather than starting at num*2, we start sieving at num**2, because all numbers greater than num that are multiples of num* <num, are already sieved

def generate_primes(n: int) -> List[int]:
    primes = []
    is_prime = [False, False] + [True]*(n-1)
    for p in range(2,n+1):
      if is_prime[p]:
        primes.append(p)
        # key thing: we can set the iterator to p so it just all multiples of p
        for i in range(p**2, n+1, p):
            is_prime[i] = False
    return primes
            
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
