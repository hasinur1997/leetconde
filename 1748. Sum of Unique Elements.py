# Problem Link https://leetcode.com/problems/sum-of-unique-elements/
import collections

def sum_of_unique(nums):
    nums = collections.Counter(nums)

    summation = 0

    for i in nums:
        if nums[i] < 2:
            summation += i

    return summation

print(sum_of_unique([1,1,1,1,1]))
