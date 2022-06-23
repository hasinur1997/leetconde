# 6039. Maximum Product After K Increments
# Problem link https://leetcode.com/contest/weekly-contest-288/problems/maximum-product-after-k-increments/
import math
def maximum_product(nums, k):
    ans = []
    for i in range(len(nums)):
        nums[i] += k
        ans.append(math.prod(nums))
        nums[i] -= k
        print(nums)

    return max(ans)


print(maximum_product([0, 4], 5))
