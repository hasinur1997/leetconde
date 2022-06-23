# Problem link https://leetcode.com/problems/number-of-1-bits/

def hamming_weight(n):
    counter = 0

    while n:
        counter += n&1
        n >>= 1

    return counter


print(hamming_weight(1011))