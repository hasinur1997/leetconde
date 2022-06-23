# Problem Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def substract_product_sum(n):
    product = 1
    summation = 0
    digits = []
    while n > 0:
        mod = int(n % 10)
        digits.append(mod)
        product *= mod
        summation += mod

        n = n // 10

    return product - summation

print(substract_product_sum(234))

