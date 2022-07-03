# Problem Link https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
import collections


def digit_count(num):
    digits = {}
    for i in range(len(num)):
        digits[i] = num.count(str(i))
    print(digits)
    for i in range(len(num)):
        if num.count(str(i)) != digits[i]:
            return False

    return True


print(digit_count("030"))
