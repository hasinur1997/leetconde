# Problem Link https://leetcode.com/problems/happy-number/

def is_happy(n):
    while n != 1 and n != 4:
        n = calculate_digit_sum(n)
        print(n)
    return n == 1

def calculate_digit_sum(n):
    summation = 0

    while n > 0:
        mode = n % 10
        summation += mode ** 2
        n = n // 10

    return summation


print(is_happy(5))


