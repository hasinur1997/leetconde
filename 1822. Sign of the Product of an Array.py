# Problem Link https://leetcode.com/problems/sign-of-the-product-of-an-array/

def array_sign(nums):
    product = 1

    for i in nums:
        product *= i

    return product


def sign_func(num):
    if num > 0:
        return 1

    if num == 0:
        return 0

    return -1


def multiply(a, b):
    return a * b


product = reduce()

print(sign_func(array_sign([1,5,0,2,-3])))