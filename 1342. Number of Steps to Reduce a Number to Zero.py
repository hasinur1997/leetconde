# Problem Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def number_steps(n):
    steps = 0

    while n > 0:

        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
        steps += 1

    return steps

print(number_steps(123))