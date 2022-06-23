# Problem link https://leetcode.com/problems/self-dividing-numbers/

def extract_digits(number):

    digits = []

    while number > 0:
        mod = int(number % 10)
        digits.append(mod)
        number = number // 10

    return digits


def is_self_dividing(number):
    n = number
    while n > 0:
        digit = int(n % 10)

        if digit == 0 or number % digit != 0:
            return False
        n = n // 10

    return True


def self_dividing_number(left, right):
    numbers = []
    for i in range(left, right+1):
        if is_self_dividing(i):
            numbers.append(i)

    return numbers


print(self_dividing_number(1, 22))
