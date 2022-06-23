# Problem link https://leetcode.com/problems/count-primes/
import math


def is_prime(number):
    if number == 0 or number == 1:
        return False

    if number == 2:
        return True
    print(int(math.sqrt(number)))
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False

    return True


def count_primes(n):
    counter = 0
    for i in range(n):
        if is_prime(i):
            counter += 1

    return counter

print(is_prime(9))

# print(int(math.sqrt(10)))