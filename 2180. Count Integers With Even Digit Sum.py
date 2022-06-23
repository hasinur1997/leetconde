# Problem Link https://leetcode.com/problems/count-integers-with-even-digit-sum/

"""
Algorithms:
1. Get digits sum
2. Check even or odd
3. Count 1 to n if digits sum is even or not
"""


def digit_sum(number):
    if number < 10:
        return number

    summation = 0
    while number > 0:
        digit = int(number % 10)
        summation += digit
        number = number // 10

    return summation


def is_even(number):
    if number % 2 == 0:
        return True

    return False


def count_even(num):
    counter = 0

    for i in range(1, num+1):
        temp = list(str(i))
        digits = [int(x) for x in temp]

        if sum(digits) % 2 == 0:
            counter += 1

    return counter


print(count_even(30))

