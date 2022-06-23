# Problem Link https://leetcode.com/problems/missing-number/

def missing_numbers(nums):
    nums = set(nums)
    n = len(nums)

    for i in range(n+1):
        if i not in nums:
            return i


print(missing_numbers([0,1]))
