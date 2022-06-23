# Problem Link https://leetcode.com/problems/sqrtx/
import math
def my_sqrt(x):
    l = 0
    h = x

    while l <= h:
        mid = l + (h-l) // 2

        if mid * mid == x:
            return mid

        if mid*mid > x:
            h = mid - 1

        else:
            l = mid + 1

    return h

print(my_sqrt(144))
