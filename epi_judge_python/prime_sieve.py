from test_framework import generic_test
import math


# Given n, return all primes up to and including n.
def generate_primes(n):
    candidates = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if candidates[i]:
            if is_prime(i):
                primes.append(i)
                remove_prime_multiples(candidates, i, n)

    return primes


def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def remove_prime_multiples(candidates, i, n):
    k = 2 * i
    while k <= n:
        candidates[i] = False
        k += i


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
