import functools
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook
import random


def random_sampling(k: int, A: List[int]) -> None:
    # problem: given a list of integers and a size K, move a random, unique subset of k integers into the first k digits of the list
    # solution: set i to 0, loop while i < k
    # generate a random number, and mod it over (n-i) to get an index in the list, call that r
    # move L[r] into L[i]
    # increment i   
    i = 0
    while i < k:
        # pick a random index we haven't picked from yet
        rand = random.randint(i, len(A)-1)
        r = rand
        print(f"random index is ${r}")
        # Swap it into the lowest index
        A[i], A[r] = A[r], A[i]
        i+=1
    print(f"result is {A}")
    return A


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
