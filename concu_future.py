# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:01:14 2020

@author: jk
"""

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    print("start", n, "*")
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    print("end", n, "#")
    return True


def main():
    with concurrent.futures.ThreadPoolExecutor(2) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


main()