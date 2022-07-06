# Problem Link https://leetcode.com/problems/product-of-the-last-k-numbers/
import math
class ProductOfNumbers:
    def __init__(self):
        self.nums = []

    def add(self, num):
        self.nums.append(num)

    def get_products(self, k):
       return math.prod(self.nums[:-k])


obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)

print(obj.nums)